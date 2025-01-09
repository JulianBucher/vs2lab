import logging
import random
import time

from constMutex import ENTER, RELEASE, ALLOW, ACTIVE


class Process:
    """
    Implements access management to a critical section (CS) via fully
    distributed mutual exclusion (MUTEX).

    Processes broadcast messages (ENTER, ALLOW, RELEASE) timestamped with
    logical (lamport) clocks. All messages are stored in local queues sorted by
    logical clock time.

    Processes follow different behavioral patterns. An ACTIVE process competes 
    with others for accessing the critical section. A PASSIVE process will never 
    request to enter the critical section itself but will allow others to do so.

    A process broadcasts an ENTER request if it wants to enter the CS. A process
    that doesn't want to ENTER replies with an ALLOW broadcast. A process that
    wants to ENTER and receives another ENTER request replies with an ALLOW
    broadcast (which is then later in time than its own ENTER request).

    A process enters the CS if a) its ENTER message is first in the queue (it is
    the oldest pending message) AND b) all other processes have sent messages
    that are younger (either ENTER or ALLOW). RELEASE requests purge
    corresponding ENTER requests from the top of the local queues.

    Message Format:

    <Message>: (Timestamp, Process_ID, <Request_Type>)

    <Request Type>: ENTER | ALLOW  | RELEASE

    """

    def __init__(self, chan):
        self.channel = chan  # Create ref to actual channel
        self.process_id = self.channel.join('proc')  # Find out who you are
        self.all_processes: list = []  # All procs in the proc group
        self.other_processes: list = []  # Needed to multicast to others
        self.queue = []  # The request queue list
        self.clock = 0  # The current logical clock
        self.peer_name = 'unassigned'  # The original peer name
        self.peer_type = 'unassigned'  # A flag indicating behavior pattern
        self.logger = logging.getLogger("vs2lab.lab5.mutex.process.Process")

        self.failed_processes = set()
        self.response_tracker = {}  # Track responses from peer

    # detect crash after intervall
    def __detect_crash(self):
        # Remove any unresponsive peers from `other_processes`
        for peer in self.other_processes:
            if self.response_tracker.get(peer, 0) < self.clock - 3:  # Threshold for crash
                self.logger.warning(f"Detected crash of {self.__mapid(peer)}")
                self.failed_processes.add(peer)
                # self.all_processes.remove(peer)
                self.other_processes.remove(peer)

                print(f" somesbit {self.failed_processes}")
                print(f" someshit {self.other_processes}")



    def __mapid(self, id='-1'):
        # format channel member address
        if id == '-1':
            id = self.process_id
        return 'Proc-'+str(id)

    

    def __cleanup_queue(self):
        if len(self.queue) > 0:
            # self.queue.sort(key = lambda tup: tup[0])
            self.queue.sort()
            # There should never be old ALLOW messages at the head of the queue
            while self.queue and (self.queue[0][1] in self.failed_processes or self.queue[0][2] == ALLOW):
                del (self.queue[0])
                if len(self.queue) == 0:
                    break

    def __request_to_enter(self):
        self.clock = self.clock + 1  # Increment clock value
        request_msg = (self.clock, self.process_id, ENTER)
        self.queue.append(request_msg)  # Append request to queue
        self.__cleanup_queue()  # Sort the queue
        self.channel.send_to(self.other_processes, request_msg)  # Send request

    def __allow_to_enter(self, requester):
        self.clock = self.clock + 1  # Increment clock value
        msg = (self.clock, self.process_id, ALLOW)
        self.channel.send_to([requester], msg)  # Permit other

    def __release(self):
        # need to be first in queue to issue a release
        assert self.queue[0][1] == self.process_id, 'State error: inconsistent local RELEASE'

        # construct new queue from later ENTER requests (removing all ALLOWS)
        tmp = [r for r in self.queue[1:] if r[2] == ENTER]
        self.queue = tmp  # and copy to new queue
        self.clock = self.clock + 1  # Increment clock value
        msg = (self.clock, self.process_id, RELEASE)
        # Multicast release notification
        # self.channel.send_to(self.other_processes, msg)
        # Only send to processes not marked as failed
        try:
        # Only send to processes not marked as failed
            active_processes = [p for p in self.other_processes if p not in self.failed_processes]
            self.channel.send_to(active_processes, msg)
        except Exception as e:
            self.logger.error(f"Failed to send message: {e}")
    
    
    def __allowed_to_enter(self):
        # See who has sent a message (the set will hold at most one element per sender)
        processes_with_later_message = set(
            req[1] for req in self.queue[1:] if req[1] not in self.failed_processes)
        # Access granted if this process is first in queue and all others have answered (logically) later
        first_in_queue = self.queue[0][1] == self.process_id
        all_have_answered = len(self.other_processes) == len(processes_with_later_message)
        return first_in_queue and all_have_answered

    def __receive(self):
        if self.other_processes:  # Check if other_processes is not empty
            _receive = self.channel.receive_from(self.other_processes, 3)

            if _receive:
                msg = _receive[1]
                sender = msg[1]

                self.response_tracker[sender] = self.clock  # Update the tracker

                self.clock = max(self.clock, msg[0])  # Adjust clock value...
                self.clock = self.clock + 1  # ...and increment

                self.logger.debug(f"{self.__mapid()} received {msg[2]} from {self.__mapid(sender)}")
     
                if msg[2] == ENTER:
                    self.queue.append(msg)  # Append an ENTER request
                # and unconditionally allow (don't want to access CS oneself)
                    self.__allow_to_enter(msg[1])
                elif msg[2] == ALLOW:
                    self.queue.append(msg)  # Append an ALLOW
                elif msg[2] == RELEASE:
                # assure release requester indeed has access (his ENTER is first in queue)
                    assert self.queue[0][1] == msg[1] and self.queue[0][2] == ENTER, 'State error: inconsistent remote RELEASE'
                    del (self.queue[0])  # Just remove first message

                self.__cleanup_queue()  # Finally sort and cleanup the queue
            else:
                self.__detect_crash()
                self.logger.info(f"{self.__mapid()} timed out on RECEIVE. Local queue: {self.queue}")

        else:
        # Handle the case where there are no other processes
        # You might want to sleep for a short time or do something else
            time.sleep(1)  # Sleep for 1 second to avoid busy-waiting
            self.logger.info(f"{self.__mapid()} no other processes to receive from.")

            # self.logger.info("{} timed out on RECEIVE. Local queue: {}".
            #                  format(self.__mapid(),
            #                         list(map(lambda msg: (
            #                             'Clock '+str(msg[0]),
            #                             self.__mapid(msg[1]),
            #                             msg[2]), self.queue))))

    def init(self, peer_name, peer_type):
        self.channel.bind(self.process_id)

        self.all_processes = list(self.channel.subgroup('proc'))
        # sort string elements by numerical order
        self.all_processes.sort(key=lambda x: int(x))


        self.other_processes = []
        for proc in self.all_processes:
            if proc != self.process_id:
                if proc not in self.failed_processes:
                    self.other_processes.append(proc)
        # self.other_processes = list(self.channel.subgroup('proc'))
        # self.other_processes.remove(self.process_id)

        self.peer_name = peer_name  # assign peer name
        self.peer_type = peer_type  # assign peer behavior

        self.logger.info("{} joined channel as {}.".format(
            peer_name, self.__mapid()))

    def run(self):
        while True:
            if len(self.all_processes) > 1 and self.peer_type == ACTIVE and random.choice([True, False]):
                self.__request_to_enter()
                while not self.__allowed_to_enter():
                    self.__receive()
            
                sleep_time = random.randint(0, 2000)
                self.logger.debug(f"{self.__mapid()} enters CS for {sleep_time} milliseconds")
                print(f" CS <- {self.__mapid()}")
                time.sleep(sleep_time / 1000)
                print(f" CS -> {self.__mapid()}")
                self.__release()
            elif random.choice([True, False]):
                self.__receive()
        # while True:
        #     # Enter the critical section if
        #     # 1) there are more than one process left and
        #     # 2) this peer has active behavior and
        #     # 3) random is true
        #     if len(self.all_processes) > 1 and \
        #             self.peer_type == ACTIVE and \
        #             random.choice([True, False]):
        #         self.logger.debug("{} wants to ENTER CS at CLOCK {}."
        #                           .format(self.__mapid(), self.clock))

        #         self.__request_to_enter()
        #         while not self.__allowed_to_enter():
        #             self.__receive()

        #         # Stay in CS for some time ...
        #         sleep_time = random.randint(0, 2000)
        #         self.logger.debug("{} enters CS for {} milliseconds."
        #                           .format(self.__mapid(), sleep_time))
        #         print(" CS <- {}".format(self.__mapid()))
        #         time.sleep(sleep_time/1000)

        #         # ... then leave CS
        #         print(" CS -> {}".format(self.__mapid()))
        #         self.__release()
        #         continue

        #     # Occasionally serve requests to enter (
        #     if random.choice([True, False]):
        #         self.__receive()