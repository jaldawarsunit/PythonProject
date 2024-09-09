# import os
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker")
#     x = input("Enter what you want me to speak : " )
#     command = f"say {x}"
#
#     os.system(command)
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
print("Welcome to RoboSpeaker")
while(True):
    x = input("Enter what you want me to speak : " )
    speak.Speak(x)
    if x== "quit":
        x="bye byee"
        speak.Speak(x)
        exit()