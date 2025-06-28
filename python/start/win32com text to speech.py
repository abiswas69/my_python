import win32com.client

def text_to_speech_windows(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

# Example usage
text_to_speech_windows("Hello, this is Windows text to speech.")