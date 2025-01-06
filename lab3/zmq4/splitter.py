import zmq
import constPipe

#def splitter(file_path="text.txt"):

file_path="text.txt"
context = zmq.Context()

    # PUSH-Sockets für die Mapper erstellen
#
push_socket = context.socket(zmq.PUSH)
#[context.socket(zmq.PUSH) for _ in constPipe.MAPPER_PORTS]
#address1 = "tcp://" + constPipe.SRC1 + ":" + constPipe.PORT1  # 1st task src
#address2 = "tcp://" + constPipe.SRC2 + ":" + constPipe.PORT2  # 2nd task src

#for i, socket in enumerate(push_sockets):
#    
push_socket.bind(f"tcp://{constPipe.SPLITTER_HOST}:{constPipe.MAPPER_PORTS}")

print("Splitter ist bereit, Sätze an die Mapper zu senden.")

    # Datei zeilenweise einlesen
with open(file_path, "r") as file:
        sentences = file.readlines()
    
    # Sätze abwechselnd an die Mapper senden
for i, sentence in enumerate(sentences):
    #target_mapper = i % len(push_sockets)  # Round-Robin-Zuordnung
    
    push_socket.send_string(sentence.strip())
    print(f"Splitter: '{sentence.strip()}")

print("Splitter hat alle Sätze gesendet.")