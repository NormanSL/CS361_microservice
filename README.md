# CS361_microservice

# Server Program README

## Description

The server program is a simple microservice that handles user login authentication and allows CRUD (Create, Read, Update, Delete) operations for user credentials. It is intended to be used as part of a client-server application, where clients can connect to the server to perform login verification, add new users, update existing user credentials, or delete user accounts.

This microservice is written in Python and uses socket communication to interact with clients over the network. It provides a basic implementation of the required functionality for example purposes but lacks security features that would be essential for a production environment.

## Features

- User Login Verification: The server allows clients to verify their login credentials. It checks the provided username and password against a predefined hard-coded dictionary of valid credentials.  

- Adding Users: Clients can request to add new users by providing a username and password. The server updates the dictionary of valid credentials to include the new user.

- Updating User Credentials: Existing users can request to update their password. The server updates the corresponding entry in the dictionary of valid credentials.

- Deleting Users: Clients can request to delete a user account by providing the username. The server removes the corresponding entry from the dictionary of valid credentials.

- Graceful Termination: The server can be gracefully terminated by using `Ctrl + C` (KeyboardInterrupt), ensuring that resources are released correctly.

## Prerequisites

- Python (version 3.11.XX or later)


## Getting Started

1. Clone the repository to your local machine.

2. Run the server program by executing the `login_server.py` file

3. The server will start listening on the specified address and port (by default, `localhost:12345`).

## Usage

Clients can connect to the server using the provided client application or any custom client that follows the protocol described in the server code.

- To test the server using the provided client, run the `client.py` file:

- Follow the prompts to select the desired action (e.g., login verification, add user, update user, delete user) and provide the necessary information.

- The client will send the request to the server using socket connection to transmit a request keyword such as LOGIN, ADD, etc., followed by the relevant input strings, and the server will respond with the result.

## Security Considerations

It's important to note that this microservice lacks several essential security features and is intended for educational/demonstration purposes only. In a real-world application, you should consider implementing some or all of the following security measures:

- Password Encryption: Store user passwords securely by encrypting them before storing in the database.

- Salt and Pepper: user-unique (Salt) or database-common (Pepper) values added to user information prior to hashing to provide an additional "lock" requiring another "key" to be opened.

- Secure Communication: Use secure socket layers (SSL/TLS) for encrypted communication between the client and server.

- Input Validation: Implement robust input validation to prevent malicious input and potential security vulnerabilities.

- Database Integration: Store user credentials in a secure database instead of a hard-coded dictionary.

## Acknowledgments

Special thanks to Stuart Ballard @SAB39 for superb rubber ducking

## Contact

Email me at NormanSL@OregonState.edu



[Sequence diagram.pdf](https://github.com/NormanSL/CS361_microservice/files/12245393/Sequence.diagram.pdf)
