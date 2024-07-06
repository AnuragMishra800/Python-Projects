# import os 
# if __name__ == '__main__':
#     print("Welcome To Robot3.0")
#     while True:
#         x = input("Enter what you want to speak through Robot:")
#         command = f"say {x}" 
#         os.system(command) 

import pyttsx3 as pt
text_to_speech = pt.init()
print("Welcome To Robot3.0, Created By Anurag Mishra.") 
print("Enter q to Quit.")
while(True):
    word = input("Enter what you want to speak through Robot:")
    if word == 'q':
        break
    text_to_speech.say(word)
    text_to_speech.runAndWait()