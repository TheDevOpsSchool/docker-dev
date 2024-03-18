import socket

# Define host and port
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8184        # Port to listen on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))
    
    # Start listening for incoming connections
    server_socket.listen()
    
    print(f"Server listening on {HOST}:{PORT}")
    
    # Accept incoming connection
    conn, addr = server_socket.accept()
    with conn:
        print('Connected by', addr)
        
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            
            # Echo back the received data
            conn.sendall(data)
