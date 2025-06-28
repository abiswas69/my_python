import socket
import threading
from datetime import datetime

class ChatServer:
    COLOR_CODES = {
        'SYSTEM': '\033[93m',  # Yellow
        'ERROR': '\033[91m',   # Red
        'USER': '\033[94m',    # Blue
        'MESSAGE': '\033[92m', # Green
        'ENDC': '\033[0m'      # Reset
    }
    
    def __init__(self, host='0.0.0.0', port=5555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.nicknames = []
        self.lock = threading.Lock()
        
    def color_print(self, text, color_type):
        """Print colored text to console"""
        print(f"{self.COLOR_CODES[color_type]}{text}{self.COLOR_CODES['ENDC']}")
        
    def broadcast(self, message, sender=None, color_type='MESSAGE'):
        """Send message to all clients with color coding"""
        with self.lock:
            timestamp = datetime.now().strftime("%H:%M:%S")
            formatted_msg = f"[{timestamp}] {message}"
            
            # Print to server console with color
            self.color_print(formatted_msg, color_type)
            
            # Send to all clients (without color codes)
            for client in self.clients:
                try:
                    client.send(formatted_msg.encode('utf-8'))
                except:
                    self.remove_client(client)
    
    def handle_client(self, client):
        """Handle individual client connections"""
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message.startswith('/nick '):
                    new_nick = message[6:].strip()
                    index = self.clients.index(client)
                    old_nick = self.nicknames[index]
                    self.nicknames[index] = new_nick
                    self.broadcast(f"{old_nick} changed nickname to {new_nick}", color_type='SYSTEM')
                else:
                    index = self.clients.index(client)
                    nickname = self.nicknames[index]
                    self.broadcast(f"{nickname}: {message}")
            except:
                self.remove_client(client)
                break
    
    def remove_client(self, client):
        """Remove a client from the server"""
        with self.lock:
            if client in self.clients:
                index = self.clients.index(client)
                nickname = self.nicknames[index]
                self.clients.remove(client)
                self.nicknames.pop(index)
                client.close()
                self.broadcast(f"{nickname} left the chat", color_type='SYSTEM')
    
    def start(self):
        """Start the chat server"""
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.color_print(f"Server started on {self.host}:{self.port}", 'SYSTEM')
        
        try:
            while True:
                client, address = self.server.accept()
                
                client.send("NICK".encode('utf-8'))
                nickname = client.recv(1024).decode('utf-8')
                
                with self.lock:
                    self.nicknames.append(nickname)
                    self.clients.append(client)
                
                self.broadcast(f"{nickname} joined the chat", color_type='SYSTEM')
                client.send("Connected to server! Type /nick to change nickname".encode('utf-8'))
                
                thread = threading.Thread(target=self.handle_client, args=(client,))
                thread.start()
        except KeyboardInterrupt:
            self.broadcast("Server is shutting down...", color_type='ERROR')
            with self.lock:
                for client in self.clients:
                    client.close()
            self.server.close()

if __name__ == "__main__":
    server = ChatServer()
    server.start()