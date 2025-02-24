# Chat Server Implementations

This repository contains different implementations of chat servers using Python. The purpose of these implementations is to demonstrate various techniques for handling client-server communication in a networked environment.

## Project Overview

The project includes the following chat server implementations:
1. Blocking Chat Server
2. Non-Blocking Chat Server
3. Server to Client - Client to Server Communication
4. Server to Client Communication

## Setup and Running the Project

To set up and run any of the chat server implementations, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Konseptt/CN-lab.git
   cd CN-lab
   ```

2. Navigate to the desired chat server implementation directory:
   ```bash
   cd <implementation-directory>
   ```

3. Run the server script:
   ```bash
   python server.py
   ```

4. In a separate terminal, run the client script:
   ```bash
   python client.py
   ```

## Examples

### Blocking Chat Server

1. Navigate to the blocking chat server directory:
   ```bash
   cd chat\ server/blocking
   ```

2. Run the server script:
   ```bash
   python server.py
   ```

3. In a separate terminal, run the client script:
   ```bash
   python client.py
   ```

### Non-Blocking Chat Server

1. Navigate to the non-blocking chat server directory:
   ```bash
   cd chat\ server/non_blocking
   ```

2. Run the server script:
   ```bash
   python server.py
   ```

3. In a separate terminal, run the client script:
   ```bash
   python client.py
   ```

### Server to Client - Client to Server Communication

1. Navigate to the server to client-client to server directory:
   ```bash
   cd Server\ to\ client-client\ to\ server
   ```

2. Run the server script:
   ```bash
   python server.py
   ```

3. In a separate terminal, run the client script:
   ```bash
   python client.py
   ```

### Server to Client Communication

1. Navigate to the server to client directory:
   ```bash
   cd Server\ to\ client
   ```

2. Run the server script:
   ```bash
   python server1.py
   ```

3. In a separate terminal, run the client script:
   ```bash
   python client1.py
   ```

### Running the `cases` Directory Scripts

The `cases` directory contains scripts for a simple client-server communication example. Follow these steps to run the scripts:

1. Navigate to the `cases` directory:
   ```bash
   cd cases
   ```

2. Run the server script:
   ```bash
   python server.py
   ```

3. In a separate terminal, run the client script:
   ```bash
   python client.py
   ```

#### Details about the `cases/client.py` and `cases/server.py` Scripts

- `cases/client.py`: This script creates a client that connects to the server on port 12000, sends a lowercase message, receives the uppercase response from the server, and then closes the connection.
- `cases/server.py`: This script creates a server that listens on port 12000, accepts a connection from a client, receives a message, converts it to uppercase, sends the uppercase message back to the client, and then closes the connection.

#### Example for Running the `cases` Directory Scripts

1. Navigate to the `cases` directory:
   ```bash
   cd cases
   ```

2. Run the server script:
   ```bash
   python server.py
   ```

3. In a separate terminal, run the client script:
   ```bash
   python client.py
   ```
