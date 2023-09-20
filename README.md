# Installation:

```
git clone https://github.com/hesam-zahiri/p2p_vpn.git
```
```
pip install torch
````
# How to use:

1- Create a VPN server:

To create a VPN server, use the PyTorch library and the UDP protocol. To do this, open a UDP server and create a UDP channel for each user. Then, for each user, generate a public key and a private key and send the public key to the user.
```
cd p2p_vpn
```
```
python key.py
```

```python
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
```
2- Create a VPN client:

To create a VPN client, use the PyTorch library and the UDP protocol. To do this, establish a UDP channel with the VPN server and send your public key to the server. Then, use the server's public key to encrypt your data.

```
python p2p_vpn.py
```

```python
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
```
```
python p2p_vpn.py
```
- This is a simple example of a VPN with P2P capability. However, to use this app for P2P, you need to invite other users to join your network and share their public key with you. Also, to use this app as a VPN, you need to use stronger encryption protocols.
