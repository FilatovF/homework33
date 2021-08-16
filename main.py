

import threading
from datetime import time


class Counter(threading.Thread):
    counter = 0
    rounds = 1000000

    def run(self):
        for i in range(self.rounds):
            Counter.counter += 1





import socket
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)


class H_con(threading.Thread):
    def __init__(self, connection, client_address):
        super().__init__()
        self.connection = connection
        self.client_address = client_address

    def run(self):
        for i in range(100, 0, -1):
            self.connection.sendall(f'Осталось{i} секунд'.encode())
            import time
            time.sleep(1.0)
        self.connection.close()


if __name__ == '__main__':

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        worker = H_con(connection, client_address)
        worker.start()



