import socket
import threading
import pyttsx3
import time
from datetime import datetime

class ChatClient:
    COLOR_CODES = {
        'SYSTEM': '\033[93m',  # Yellow
        'ERROR': '\033[91m',   # Red
        'USER': '\033[94m',    # Blue
        'MESSAGE': '\033[92m', # Green
        'ENDC': '\033[0m'      # Reset
    }
    
    def __init__(self, host='127.0.0.1', port=5555):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = None
        self.engine = pyttsx3.init()
        self.configure_voice()
        self.running = True
        
    def configure_voice(self, rate=150, volume=0.8):
        """Configure text-to-speech settings"""
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
    
    def color_print(self, text, color_type):
        """Print colored text to console"""
        print(f"{self.COLOR_CODES[color_type]}{text}{self.COLOR_CODES['ENDC']}")
    
    def speak(self, text):
        """Convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()
    
    def receive(self):
        """Handle incoming messages from server"""
        while self.running:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    # Print with color coding
                    if "joined the chat" in message or "left the chat" in message:
                        self.color_print(message, 'SYSTEM')
                    elif "ERROR" in message:
                        self.color_print(message, 'ERROR')
                    else:
                        self.color_print(message, 'MESSAGE')
                    
                    # Speak system messages and mentions
                    if self.nickname.lower() in message.lower():
                        self.speak(f"You were mentioned in chat: {message}")
                    elif "joined" in message or "left" in message:
                        self.speak(message)
            except:
                self.color_print("Disconnected from server", 'ERROR')
                self.speak("Disconnected from server")
                self.running = False
                break
    
    def write(self):
        """Handle user input and send to server"""
        while self.running:
            try:
                message = input("")
                if message.lower() == '/quit':
                    self.running = False
                    self.client.close()
                    break
                self.client.send(message.encode('utf-8'))
            except:
                self.running = False
                break
    
    def start(self):
        """Start the chat client"""
        try:
            self.client.connect((self.host, self.port))
            
            # Get nickname
            self.nickname = input("Choose your nickname: ")
            while not self.nickname.strip():
                self.nickname = input("Nickname cannot be empty. Choose your nickname: ")
            
            # Start threads
            receive_thread = threading.Thread(target=self.receive)
            receive_thread.start()
            
            write_thread = threading.Thread(target=self.write)
            write_thread.start()
            
            # Welcome message
            self.speak(f"Welcome to the chat room {self.nickname}")
            self.color_print("\nType /quit to exit\n", 'SYSTEM')
            
            # Keep main thread alive
            while self.running:
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.speak("Closing chat client")
            self.running = False
            self.client.close()
        except Exception as e:
            self.color_print(f"Connection error: {str(e)}", 'ERROR')
            self.speak("Failed to connect to server")
            self.running = False

if __name__ == "__main__":
    client = ChatClient()
    client.start()