#A beginner project
#This simple program converts the text into speech
#created by stark


import win32com.client

v = win32com.client.Dispatch("SAPI.SpVoice")



print('Press "q" to Quit')
name = input("May i know your name? ")



if name == "Stark" or "nirbhay":
    print("Welcome Sir!")
    v.Speak("Welcome Sir")
else:
    print(f"Hello! {name}")
    v.Speak(f"Hello!{name}")
    print("I am a text to speech program created by Stark \nWhat do you want me to speak?")
    v.Speak("I am a text to speech program created by Stark. What do you want me to speak?")

while True:
    text = input("Enter a Text:")
     
    if text == "q":
            v.Speak("Bye bye")
            print("Bye! bye!")
            break

    if text == "who created you":
        print("Created by Stark")
        v.Speak("I am a Text to speech program Created by mister Stark")
        
        continue

    if text == "whats your instagram":
        print(contact)
        v.Speak(contact)
        continue


    v.Speak(text)
