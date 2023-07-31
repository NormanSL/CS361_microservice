# Lauren Norman Schueneman
# CS361 project team 57
# Quick client program to test login_server.py

# ---------------------------------------#
# imports and globals
# ---------------------------------------#

import socket   # using sockets for communication between server and client

# variable to define max buffer size, defaulting to 1kb
max_buffer = 1024

# variable to define port, using 12345 as placeholder
port_number = 12345

# variable to define scheme for encoding/decoding byte literals
decoder = 'utf-8'

# ---------------------------------------#
# logic for login, add, update and delete requests
#----------------------------------------#


def login_verification(client_socket):
    """takes user input, sends to server and returns determination"""
    # get input
    userid = input('Enter userid: ')
    password = input('Enter password: ')

    # pass input to the server
    client_socket.sendall(userid.encode('utf-8'))
    client_socket.sendall(password.encode('utf-8'))

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
    client_socket.sendall(userid.encode(decoder))
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
    client_socket.sendall(userid.encode(decoder))
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
    client_socket.sendall(userid.encode(decoder))

    # receive response and print
    response = client_socket.recv(max_buffer).decode(decoder)
    print(response)


# ---------------------------------------#
# main function to create socket and
# define basic UI
# ---------------------------------------#




































