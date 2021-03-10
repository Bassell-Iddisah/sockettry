import socket, os, os.path as path, tqdm

# device's IP address
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5001
# Receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = '<SEPARATOR>'

# Creating our TCP socket
sock = socket.socket()

# Bind the hostname and port to the socket
sock.bind((SERVER_HOST, SERVER_PORT))

# listen for any connections
sock.listen(5)
print(f'[+] Listening as {SERVER_HOST}:{SERVER_PORT}')

client_socket, address = sock.accept()

print(f"[+] {address} is connected.")

# Get file name and size
received = client_socket.recv(BUFFER_SIZE).decode()
# split name and size into respective containers
filename, filesize = received.split(SEPARATOR)


# Get only name of file
filename = path.basename(filename)

#Convert name to int
filesize = int(filesize)


# Now to  receive the file
# Start receiving the file from the socket and writing to the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit='B', unit_scale=True, unit_divisor=1024)
with open(filename, 'wb') as f:
    while True:
        # Read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break

        f.write(bytes_read)

        # Update the progressbar
        progress.update(len(bytes_read))

# close the client socket
client_socket.close()

# Close the server socket
sock.close()
