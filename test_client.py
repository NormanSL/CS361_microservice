# Lauren Norman Schueneman
# CS361 project team 57
# Quick client program to test login_server.py

# ---------------------------------------#
# imports and globals
# ---------------------------------------#

import socket   # using sockets for communication between server and client
import time

# variable to define max buffer size, defaulting to 1kb
max_buffer = 1024

# variable to define port, using 12345 as placeholder
port_number = 12345

# variable to define scheme for encoding/decoding byte literals
decoder = 'utf-8'


def send_line(client_socket, msg):
    line = msg + '\n'
    client_socket.sendall(line.encode(decoder))

# ---------------------------------------#
# logic for login, add, update and delete requests
#----------------------------------------#


def login_verification(client_socket):
    """takes user input, sends to server and returns determination"""
    # get input
    userid = input('Enter userid: ')
    password = input('Enter password: ')

    # pass input to the server
    send_line(client_socket, 'LOGIN')
    send_line(client_socket, userid)
    send_line(client_socket, password)

    # receive and display result
    response = client_socket.recv(max_buffer).decode(decoder)
    print(response)


def add_credentials(client_socket):
    """send ADD request and user input, prints response"""
    # get input
    userid = input('Enter new userid: ')
    password = input('Enter new password: ')

    # send ADD request and input
    client_socket.sendall(b'ADD')
    time.sleep(1)
    client_socket.sendall(userid.encode(decoder))
    time.sleep(1)
    client_socket.sendall(password.encode(decoder))

    # receive response and print
    response = client_socket.recv(max_buffer).decode(decoder)
    print(response)


def update_credentials(client_socket):
    """send UPDATE request and user input, print response"""
    # get input
    userid = input('Enter userid to update: ')
    new_password = input('Enter new password: ')

    # send UPDATE request and input
    client_socket.sendall(b'UPDATE')
    time.sleep(1)
    client_socket.sendall(userid.encode(decoder))
    time.sleep(1)
    client_socket.sendall(new_password.encode(decoder))

    # receive response and print
    response = client_socket.recv(max_buffer).decode(decoder)
    print(response)


def delete_credentials(client_socket):
    """send DELETE request and user input, print response"""
    # get input
    userid = input('Enter userid to delete: ')

    # send the DELETE request and input
    client_socket.sendall(b'DELETE')
    time.sleep(1)
    client_socket.sendall(userid.encode(decoder))

    # receive response and print
    response = client_socket.recv(max_buffer).decode(decoder)
    print(response)


# ---------------------------------------#
# main function to create socket and
# define basic UI
# ---------------------------------------#

def main():

    # # establish TCP socket
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # # connection address
    # server_address = ('localhost', port_number)
    # client_socket.connect(server_address)

    # start the UI
    while True:
        print('\nAvailable commands:')
        print('1. Login Verification')
        print('2. Add Credentials')
        print('3. Update Credentials')
        print('4. Delete Credentials')
        print('5. Exit')

        # get input
        command = input('Enter a number from the menu above: ')

        # establish TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

            # connection address
            server_address = ('localhost', port_number)
            client_socket.connect(server_address)

            # direct to corresponding logic for specified command
            if command == '1':
                login_verification(client_socket)

            elif command == '2':
                add_credentials(client_socket)

            elif command == '3':
                update_credentials(client_socket)

            elif command == '4':
                delete_credentials(client_socket)

            elif command == '5':
                break

            else:
                print('Invalid command, give it another go.')



if __name__ == '__main__':
    main()




































