import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text=input("Text:")
    speak.Speak(text)
    if text == 'quit':
        break
