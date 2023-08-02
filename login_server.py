# Lauren Norman Schueneman
# CS361 project team 57
# simple microservice that stores, allows CRUD of and authenticates user login info

# ---------------------------------------#
# imports and globals
# ---------------------------------------#

import socket   # using sockets for communication between server and client

# variable to define max buffer size, defaulting to 1kb
max_buffer = 1024

# variable to define port, using 12345 as placeholder
port_number = 12345

# variable to define scheme for decoding byte literals
decoder = 'utf-8'

# using a dictionary to store k:v pairs of userid:password
# NB this hard-coded plaintext approach lacks security and would not be used in production
valid_credentials = {'example_user1': 'example_password', 'example_user2': 'password', 'Lauren': 'Norman'}

line_buffer = []

def receive_message(client_socket):
    """receive message from socket, and print it for debugging help"""

    # If the buffer is empty, we need to read from the socket
    if len(line_buffer) == 0:

        msg = client_socket.recv(max_buffer).decode(decoder)
        print(msg)

        line_buffer.extend(msg.splitlines())

    # Return (and remove) the first line in the buffer
    return line_buffer.pop(0).rstrip('\n')


# ---------------------------------------#
# logic for login, add, update and delete requests
#----------------------------------------#


def authenticate_login(userid, password):
    """takes user input login info and verifies whether they exist in the dictionary of valid credentials"""
    """returns True for valid login, False for invalid login"""

    # return whether password matches
    return valid_credentials.get(userid) == password


def add_credentials(userid, password):
    """method to update valid_credentials with new users"""

    valid_credentials[userid] = password


def update_credentials(userid, updated_password):
    """method to update existing entries in valid_credentials"""

    login_error = 'Userid not found'

    if userid in valid_credentials:

        valid_credentials[userid] = updated_password

    else:

        print(login_error)


def delete_credentials(userid):
    """method to delete a user from valid_credentials"""

    login_error = 'Userid not found'

    if userid in valid_credentials:

        del valid_credentials[userid]

    else:

        print(login_error)


def client_handler(client_socket):
    """uses socket to receive user input strings"""

    # first input string
    userid = receive_message(client_socket)

    # second input string
    password = receive_message(client_socket)

    # authenticate user
    if authenticate_login(userid, password):

        client_socket.sendall(b'Login successful')

    else:

        client_socket.send(b'Invalid login')

    client_socket.close()


# ---------------------------------------#
# main function to define the socket
# and request reception
# ---------------------------------------#


def main():
    """establish socket and define logic for requests"""

    # TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        # bind to address and port using 12345 as a placeholder
        server_address = ('localhost', port_number)

        server_socket.bind(server_address)

        # listen method takes an int that represents the maximum backlog queue before the server stops accepting requests
        server_socket.listen(1)

        print('Server listening on {}:{}'.format(*server_address))

        try:

            while True:

                # establish a connection
                client_socket, client_address = server_socket.accept()
                print('Received connection from:', client_address)

                # handle the request
                request = receive_message(client_socket)

                # login request
                if request == 'LOGIN':
                    client_handler(client_socket)

                # add user request
                elif request == 'ADD':
                    userid = receive_message(client_socket)
                    password = receive_message(client_socket)

                    add_credentials(userid, password)

                    if valid_credentials[userid] == password:

                        client_socket.send(b'User successfully added!')

                    else:

                        client_socket.send(b'Error!  User not added.')

                    client_socket.close()

                # update user request
                elif request == 'UPDATE':
                    userid = receive_message(client_socket)
                    new_password = receive_message(client_socket)

                    update_credentials(userid, new_password)

                    client_socket.send(b'User successfully updated!')
                    client_socket.close()

                # delete request
                elif request == 'DELETE':
                    userid = receive_message(client_socket)

                    delete_credentials(userid)

                    client_socket.send(b'User successfully deleted!')
                    client_socket.close()

                else:
                    client_socket.send(b'Invalid request.')
                    client_socket.close()

        # use ctrl+c to kill the server neatly
        except KeyboardInterrupt:
            print('Server terminated.')


if __name__ == '__main__':

    main()


