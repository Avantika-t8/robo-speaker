#import os

#if __name__ == '__main__':
#   print("Welcome to RoboSpeaker, created by Avantika")
#   while True:
#        x=input("What do you want me to speak? ")
 #       if x=="z":
  #          os.system("say 'Goodbye see you never' ")
   #         break
    #    command = f"say {x}"
     #   os.system(command)

import os
if __name__ == '__main__':
    print("RoboSpeaker...")
    print("Write :q to exit")
    try:
        while True:
            txt = input("Enter anything to speak it:  ")
            if txt == "z":
                cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye Bye')"
                os.system(cmd)
                break
            cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{txt}')"
            os.system(cmd)
    except Exception as e :
        print(f"Error is -> {e}")
