import pygments
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Open the Python file and read its contents
with open("meu_codigo.py") as f:
    code = f.read()

# Use Pygments to generate HTML code from the Python code
html = pygments.highlight(code, PythonLexer(), HtmlFormatter())



import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Tinder App")
window.geometry("500x500")

# Create the profile image
profile_image = tk.PhotoImage(file="profile.png")
image_label = tk.Label(image=profile_image)
image_label.pack()

# Create the user's name label
name_label = tk.Label(text="John Doe")
name_label.pack()

# Create the "Like" and "Dislike" buttons
like_button = tk.Button(text="Like")
like_button.pack(side="left")
dislike_button = tk.Button(text="Dislike")
dislike_button.pack(side="right")

# Start the main event loop
window.mainloop()