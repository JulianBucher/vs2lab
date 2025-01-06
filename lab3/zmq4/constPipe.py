# Hosts und Ports für Splitter
SPLITTER_HOST = "127.0.0.1"
SPLITTER_PORT = "5555"  # Port, an dem der Splitter die Mapper bedient

# Ports für Mapper
MAPPER_PORTS = "5556"
                #, "5557", "5558"]  # Ports für drei Mapper

# Ports für Reducer
REDUCER_PORTS = ["5560", "5561"]  # Ports für zwei Reducer  File "/workspaces/vs2lab/lab3/zmq4/reducer.py", line 22, in <module>
    word = pull_socket.recv_string()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vscode/.local/share/virtualenvs/vs2lab-uWc7IIUF/lib/python3.11/site-packages/zmq/sugar/socket.py", line 931, in recv_string
    msg = self.recv(flags=flags)
          ^^^^^^^^^^^^^^^^^^^^^^
  File "_zmq.py", line 1156, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1191, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1278, in zmq.backend.cython._zmq._recv_copy
  File "_zmq.py", line 160, in zmq.backend.cython._zmq._check_rc
KeyboardInterrupt

vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ pipenv run python reducer.py 0
Reducer 0 ist bereit, Wörter zu empfangen.
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 1 Total: 1
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 1 Total: 2
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 1 Total: 3
Reducer 0 hat Wort 'Ziel' erhalten. Aktueller Zähler: 1 Total: 4
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 2 Total: 5
Reducer 0 hat Wort ',' erhalten. Aktueller Zähler: 1 Total: 6
Reducer 0 hat Wort 'zu' erhalten. Aktueller Zähler: 1 Total: 7
Reducer 0 hat Wort 'ermitteln' erhalten. Aktueller Zähler: 1 Total: 8
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 1 Total: 9
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 1 Total: 10
^CTraceback (most recent call last):
  File "/workspaces/vs2lab/lab3/zmq4/reducer.py", line 22, in <module>
    word = pull_socket.recv_string()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vscode/.local/share/virtualenvs/vs2lab-uWc7IIUF/lib/python3.11/site-packages/zmq/sugar/socket.py", line 931, in recv_string
    msg = self.recv(flags=flags)
          ^^^^^^^^^^^^^^^^^^^^^^
  File "_zmq.py", line 1156, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1191, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1278, in zmq.backend.cython._zmq._recv_copy
  File "_zmq.py", line 160, in zmq.backend.cython._zmq._check_rc
KeyboardInterrupt

vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ pipenv run python reducer.py 0
Reducer 0 ist bereit, Wörter zu empfangen.
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 1 Total: 1
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 1 Total: 2
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 1 Total: 3
Reducer 0 hat Wort 'Ziel' erhalten. Aktueller Zähler: 1 Total: 4
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 2 Total: 5
Reducer 0 hat Wort ',' erhalten. Aktueller Zähler: 1 Total: 6
Reducer 0 hat Wort 'zu' erhalten. Aktueller Zähler: 1 Total: 7
Reducer 0 hat Wort 'ermitteln' erhalten. Aktueller Zähler: 1 Total: 8
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 1 Total: 9
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 1 Total: 10
^CTraceback (most recent call last):
  File "/workspaces/vs2lab/lab3/zmq4/reducer.py", line 22, in <module>
    word = pull_socket.recv_string()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vscode/.local/share/virtualenvs/vs2lab-uWc7IIUF/lib/python3.11/site-packages/zmq/sugar/socket.py", line 931, in recv_string
    msg = self.recv(flags=flags)
          ^^^^^^^^^^^^^^^^^^^^^^
  File "_zmq.py", line 1156, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1191, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1278, in zmq.backend.cython._zmq._recv_copy
  File "_zmq.py", line 160, in zmq.backend.cython._zmq._check_rc
KeyboardInterrupt

vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ pipenv run python reducer.py 0
Reducer 0 ist bereit, Wörter zu empfangen.
Reducer 0 hat Wort 'Ziel' erhalten. Aktueller Zähler: 1 Total: 1
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 1 Total: 2
Reducer 0 hat Wort ',' erhalten. Aktueller Zähler: 1 Total: 3
Reducer 0 hat Wort 'zu' erhalten. Aktueller Zähler: 1 Total: 4
Reducer 0 hat Wort 'ermitteln' erhalten. Aktueller Zähler: 1 Total: 5
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 2 Total: 6
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 1 Total: 7
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 1 Total: 8
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 1 Total: 9
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 1 Total: 10
^CTraceback (most recent call last):
  File "/workspaces/vs2lab/lab3/zmq4/reducer.py", line 22, in <module>
    word = pull_socket.recv_string()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vscode/.local/share/virtualenvs/vs2lab-uWc7IIUF/lib/python3.11/site-packages/zmq/sugar/socket.py", line 931, in recv_string
    msg = self.recv(flags=flags)
          ^^^^^^^^^^^^^^^^^^^^^^
  File "_zmq.py", line 1156, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1191, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1278, in zmq.backend.cython._zmq._recv_copy
  File "_zmq.py", line 160, in zmq.backend.cython._zmq._check_rc
KeyboardInterrupt

vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ pipenv run python reducer.py 0
Reducer 0 ist bereit, Wörter zu empfangen.
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 1 Total: 1
Reducer 0 hat Wort 'Ziel' erhalten. Aktueller Zähler: 1 Total: 2
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 2 Total: 3
Reducer 0 hat Wort ',' erhalten. Aktueller Zähler: 1 Total: 4
Reducer 0 hat Wort 'zu' erhalten. Aktueller Zähler: 1 Total: 5
Reducer 0 hat Wort 'ermitteln' erhalten. Aktueller Zähler: 1 Total: 6
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 1 Total: 7
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 1 Total: 8
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 1 Total: 9
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 1 Total: 10
^CTraceback (most recent call last):
  File "/workspaces/vs2lab/lab3/zmq4/reducer.py", line 22, in <module>
    word = pull_socket.recv_string()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vscode/.local/share/virtualenvs/vs2lab-uWc7IIUF/lib/python3.11/site-packages/zmq/sugar/socket.py", line 931, in recv_string
    msg = self.recv(flags=flags)
          ^^^^^^^^^^^^^^^^^^^^^^
  File "_zmq.py", line 1156, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1191, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1278, in zmq.backend.cython._zmq._recv_copy
  File "_zmq.py", line 160, in zmq.backend.cython._zmq._check_rc
KeyboardInterrupt

vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ pipenv run python reducer.py 0
Reducer 0 ist bereit, Wörter zu empfangen.
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 1 Total: 1
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 1 Total: 2
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 1 Total: 3
Reducer 0 hat Wort 'Ziel' erhalten. Aktueller Zähler: 1 Total: 4
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 2 Total: 5
Reducer 0 hat Wort ',' erhalten. Aktueller Zähler: 1 Total: 6
Reducer 0 hat Wort 'zu' erhalten. Aktueller Zähler: 1 Total: 7
Reducer 0 hat Wort 'ermitteln' erhalten. Aktueller Zähler: 1 Total: 8
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 1 Total: 9
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 1 Total: 10
^CTraceback (most recent call last):
  File "/workspaces/vs2lab/lab3/zmq4/reducer.py", line 22, in <module>
    word = pull_socket.recv_string()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vscode/.local/share/virtualenvs/vs2lab-uWc7IIUF/lib/python3.11/site-packages/zmq/sugar/socket.py", line 931, in recv_string
    msg = self.recv(flags=flags)
          ^^^^^^^^^^^^^^^^^^^^^^
  File "_zmq.py", line 1156, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1191, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1278, in zmq.backend.cython._zmq._recv_copy
  File "_zmq.py", line 160, in zmq.backend.cython._zmq._check_rc
KeyboardInterrupt

vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ pipenv run python reducer.py 0
Reducer 0 ist bereit, Wörter zu empfangen.
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 1 Total: 1
Reducer 0 hat Wort 'Ziel' erhalten. Aktueller Zähler: 1 Total: 2
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 2 Total: 3
Reducer 0 hat Wort ',' erhalten. Aktueller Zähler: 1 Total: 4
Reducer 0 hat Wort 'zu' erhalten. Aktueller Zähler: 1 Total: 5
Reducer 0 hat Wort 'ermitteln' erhalten. Aktueller Zähler: 1 Total: 6
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 3 Total: 7
Reducer 0 hat Wort 'Ziel' erhalten. Aktueller Zähler: 2 Total: 8
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 4 Total: 9
Reducer 0 hat Wort ',' erhalten. Aktueller Zähler: 2 Total: 10
Reducer 0 hat Wort 'zu' erhalten. Aktueller Zähler: 2 Total: 11
Reducer 0 hat Wort 'ermitteln' erhalten. Aktueller Zähler: 2 Total: 12
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 1 Total: 13
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 1 Total: 14
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 2 Total: 15
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 2 Total: 16
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 1 Total: 17
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 1 Total: 18
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 2 Total: 19
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 2 Total: 20
^CTraceback (most recent call last):
  File "/workspaces/vs2lab/lab3/zmq4/reducer.py", line 22, in <module>
    word = pull_socket.recv_string()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vscode/.local/share/virtualenvs/vs2lab-uWc7IIUF/lib/python3.11/site-packages/zmq/sugar/socket.py", line 931, in recv_string
    msg = self.recv(flags=flags)
          ^^^^^^^^^^^^^^^^^^^^^^
  File "_zmq.py", line 1156, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1191, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1278, in zmq.backend.cython._zmq._recv_copy
  File "_zmq.py", line 160, in zmq.backend.cython._zmq._check_rc
KeyboardInterrupt

vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ ^C
vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ pipenv run python reducer.py 0
Reducer 0 ist bereit, Wörter zu empfangen.
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 1 Total: 1
Reducer 0 hat Wort 'Ziel' erhalten. Aktueller Zähler: 1 Total: 2
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 2 Total: 3
Reducer 0 hat Wort ',' erhalten. Aktueller Zähler: 1 Total: 4
Reducer 0 hat Wort 'zu' erhalten. Aktueller Zähler: 1 Total: 5
Reducer 0 hat Wort 'ermitteln' erhalten. Aktueller Zähler: 1 Total: 6
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 1 Total: 7
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 1 Total: 8
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 1 Total: 9
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 1 Total: 10
^CTraceback (most recent call last):
  File "/workspaces/vs2lab/lab3/zmq4/reducer.py", line 22, in <module>
    word = pull_socket.recv_string()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vscode/.local/share/virtualenvs/vs2lab-uWc7IIUF/lib/python3.11/site-packages/zmq/sugar/socket.py", line 931, in recv_string
    msg = self.recv(flags=flags)
          ^^^^^^^^^^^^^^^^^^^^^^
  File "_zmq.py", line 1156, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1191, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1278, in zmq.backend.cython._zmq._recv_copy
  File "_zmq.py", line 160, in zmq.backend.cython._zmq._check_rc
KeyboardInterrupt

vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ pipenv run python reducer.py 0
Reducer 0 ist bereit, Wörter zu empfangen.
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 1 Total: 1
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 1 Total: 2
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 1 Total: 3
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 1 Total: 4
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 1 Total: 5
Reducer 0 hat Wort 'Ziel' erhalten. Aktueller Zähler: 1 Total: 6
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 2 Total: 7
Reducer 0 hat Wort ',' erhalten. Aktueller Zähler: 1 Total: 8
Reducer 0 hat Wort 'zu' erhalten. Aktueller Zähler: 1 Total: 9
Reducer 0 hat Wort 'ermitteln' erhalten. Aktueller Zähler: 1 Total: 10
^CTraceback (most recent call last):
  File "/workspaces/vs2lab/lab3/zmq4/reducer.py", line 22, in <module>
    word = pull_socket.recv_string()
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vscode/.local/share/virtualenvs/vs2lab-uWc7IIUF/lib/python3.11/site-packages/zmq/sugar/socket.py", line 931, in recv_string
    msg = self.recv(flags=flags)
          ^^^^^^^^^^^^^^^^^^^^^^
  File "_zmq.py", line 1156, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1191, in zmq.backend.cython._zmq.Socket.recv
  File "_zmq.py", line 1278, in zmq.backend.cython._zmq._recv_copy
  File "_zmq.py", line 160, in zmq.backend.cython._zmq._check_rc
KeyboardInterrupt

vscode ➜ /workspaces/vs2lab/lab3/zmq4 (Manuel) $ pipenv run python reducer.py 0
Reducer 0 ist bereit, Wörter zu empfangen.
Reducer 0 hat Wort 'ist' erhalten. Aktueller Zähler: 1 Total: 1
Reducer 0 hat Wort 'soll' erhalten. Aktueller Zähler: 1 Total: 2
Reducer 0 hat Wort 'zählen' erhalten. Aktueller Zähler: 1 Total: 3
Reducer 0 hat Wort 'mehrmals' erhalten. Aktueller Zähler: 1 Total: 4
Reducer 0 hat Wort 'vor' erhalten. Aktueller Zähler: 1 Total: 5
Reducer 0 hat 