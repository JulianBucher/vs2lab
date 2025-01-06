import zmq
import sys
import hashlib
import constPipe

#def mapper():
# Mapper-ID aus den Kommandozeilenargumenten
mapper_id = int(sys.argv[1])
#print(mapper_id)
# Kontext und PULL-Socket erstellen
context = zmq.Context()
pull_socket = context.socket(zmq.PULL)
pull_socket.connect(f"tcp://{constPipe.SPLITTER_HOST}:{constPipe.MAPPER_PORTS}")
    
# PUSH-Sockets für Reducer erstellen
reducer_sockets = [context.socket(zmq.PUSH) for _ in constPipe.REDUCER_PORTS]
for i, socket in enumerate(reducer_sockets):
    print( constPipe.SPLITTER_HOST, constPipe.REDUCER_PORTS[i] )
    socket.connect(f"tcp://{constPipe.SPLITTER_HOST}:{constPipe.REDUCER_PORTS[i]}")
    
print(f"Mapper {mapper_id} ist bereit, Sätze zu empfangen.")
    
while True:
    # Satz vom Splitter empfangen
    sentence = pull_socket.recv_string()
    print(f"Mapper {mapper_id} hat den Satz empfangen: '{sentence}'")

    # Satz in Wörter zerlegen
    words = sentence.split()
     
    # Wörter an Reducer senden (basierend auf Hash)
    for word in words:
        target_reducer = int(hashlib.md5(word.encode()).hexdigest(), 16) % len(constPipe.REDUCER_PORTS)
        reducer_sockets[target_reducer].send_string(word)
        print(f"Mapper {mapper_id} sendet Wort '{word}' an Reducer {target_reducer}")