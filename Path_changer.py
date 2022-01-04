#Import modules 
import pyperclip

path = pyperclip.paste()

new_path = path.replace("\\","/")

new_path = f'"{new_path}"'

pyperclip.copy(new_path)

