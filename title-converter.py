import pyperclip

text = pyperclip.paste()
text = (((input("Input Text >> ")).lower()).replace(" ", "-")) if text == "" else ((text.lower()).replace(" ", "-"))
pyperclip.copy(text)
print(f"'{text}' copied to clipboard")