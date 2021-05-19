#Import modules 
import pyperclip

path = pyperclip.paste()

new_path = path.replace("\\","/")

pyperclip.copy(new_path)

