import torch
import socket

# Create a UDP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345))

# Generate a public-private key pair for each user
users = {}
for i in range(10):
    private_key = torch.rand(128)
    public_key = private_key * torch.rand(128)
    users[i] = {'private_key': private_key, 'public_key': public_key}

# Wait for incoming connections
while True:
    data, address = server_socket.recvfrom(1024)
    user_id, public_key = data.split(':')
    user_id = int(user_id)
    public_key = torch.tensor(list(map(float, public_key.split(','))))
    users[user_id]['peer_address'] = address
    users[user_id]['peer_public_key'] = public_key
