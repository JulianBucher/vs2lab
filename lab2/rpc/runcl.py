import rpc
import logging
import time
from context import lab_logging

#def print_result(result):
#    """
#    Callback function to process and display the server response.
#    """
#    print("Final result from server:", result.value)

#if __name__ == "__main__":
#    lab_logging.setup(stream_level=logging.INFO)
#    
#    client = rpc.Client()
#    client.run()
#
 #   base_list = rpc.DBList({'foo'})
 #   client.append('bar', base_list, callback=print_result)
#
    # Main thread remains active


def print_result(result):
    # Callback function to process and display the server response.
    #print("Final result from server:", result.value)
  print("Result: {}".format(result.value))


lab_logging.setup(stream_level=logging.INFO)

cl = rpc.Client()
cl.run()

base_list = rpc.DBList({'foo'})
cl.append('bar', base_list, print_result)
for i in range (0, 10):
  print("does other work")
  time.sleep(2)

#print("Result: {}".format(result_list.value))
cl.stop()
