import socket, os, os.path as path, tqdm

SEPARATOR = '<SEPARATOR>'

BUFFER_SIZE = 4096  # Send 4096 bytes each step

# Specifying the host
host = '192.168.43.9'

# Specifying the port
port = 5001

# Specifying the file to be sent
file = 'tryfile.txt'

# Now get the file size
filesize = path.getsize(file)

# Now, creating the TCP socket

sock = socket.socket()

# Connecting to the server
print(f'[+] Connecting to {host}:{port}')
sock.connect((host, port))
print(f'[+] Connection successful')

# Now send the name and size of the file

sock.send(f"{file}{SEPARATOR}{filesize}".encode())






# Lets start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {file}", unit='B', unit_scale=True, unit_divisor=1024)
with open(file, 'rb') as f:
    while True:
         bytes_read = f.read(BUFFER_SIZE)  # Read the bytes from the file
         if not bytes_read:
             break

         sock.sendall(bytes_read)  # Send the file

         progress.update(len(bytes_read)) # Update the progress bar

# Close the socket
sock.close()
