import pyttsx3
import subprocess

def initialize_tts():
    engine = pyttsx3.init()
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Slower speech rate
    engine.setProperty('volume', 0.9)  # Slightly reduced volume
    return engine

def speak_response(engine, text):
    """Speak text and print it to console"""
    print("Response:", text)
    engine.say(text)
    engine.runAndWait()

def execute_command(command):
    """Execute command and return output"""
    try:
        result = subprocess.run(command, shell=True, 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip() or "Command executed successfully"
        else:
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        return f"Execution failed: {str(e)}"

def main_loop():
    engine = initialize_tts()
    speak_response(engine, "Command executor ready. Enter 'exit' to quit.")
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter command: ").strip()
            
            # Exit condition
            if user_input.lower() in ('exit', 'quit'):
                speak_response(engine, "Goodbye!")
                break
                
            if not user_input:
                speak_response(engine, "Please enter a valid command")
                continue
                
            # Execute command
            speak_response(engine, f"Executing: {user_input}")
            output = execute_command(user_input)
            
            # Speak output (limited to 300 characters to avoid overly long responses)
            response = output[:300] + ("..." if len(output) > 300 else "")
            speak_response(engine, response)
            
        except KeyboardInterrupt:
            speak_response(engine, "Interrupted by user. Goodbye!")
            break
        except Exception as e:
            speak_response(engine, f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main_loop()