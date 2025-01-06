import zmq
import sys
import constPipe
from collections import defaultdict

#def reducer():
# Reducer-ID aus den Kommandozeilenargumenten
reducer_id = int(sys.argv[1])
    
# Kontext und PULL-Socket erstellen
context = zmq.Context()
pull_socket = context.socket(zmq.PULL)
pull_socket.bind(f"tcp://{constPipe.SPLITTER_HOST}:{constPipe.REDUCER_PORTS[reducer_id]}")
    
print(f"Reducer {reducer_id} ist bereit, Wörter zu empfangen.")
    
# Wörter und deren Häufigkeiten speichern
word_count = defaultdict(int)
word_total = 0
while True:
       # Wort vom Mapper empfangen
    word = pull_socket.recv_string()
    word_count[word] += 1
    word_total += 1
    print(f"Reducer {reducer_id} hat Wort '{word}' erhalten. Aktueller Zähler: {word_count[word]} Total: {word_total}")

