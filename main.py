from tkinter import *
from tkinter.filedialog import askopenfile
from gtts import gTTS
import pdfplumber
from tkinter.messagebox import showinfo

LIGHT_BLUE = "#a4ebf3"
BLUE = "#0a043c"
ORANGE = "#ff6701"


def to_speech(filename):
    text = ""
    file_list = filename.split("/")
    last_name = file_list[-1]
    old_path = file_list[:-1]
    new_path = "/".join(old_path)
    with pdfplumber.open(filename) as data:
        for page in data.pages:
            text += f"\n{page.extract_text()}"

    tts = gTTS(text)
    tts.save(f"{new_path}/audio_{last_name}.mp3")

    showinfo(message=f"Your file has been converted 'audio_{last_name}'.",
             title="Your files are ready!")


def upload():
    filename = askopenfile(filetypes=(("pdf file", "*.pdf"), ("all files", "*.*")))
    to_speech(filename.name)


window = Tk()
window.title("Pdf to Speech Converter")
window.config(bg=LIGHT_BLUE, pady=20, padx=50)
window.minsize(width=500, height=300)

welcome_label = Label(text="PDF to Audio book", bg=LIGHT_BLUE, fg=BLUE, font=("Arial", 20), pady=10)
welcome_label.grid(row=0, column=0)

instructions = Label(text="Converting PDF to Audio book")
instructions.config(fg="#1b1a17", bg=LIGHT_BLUE, font=("Arial", 12), pady=10)
instructions.grid(row=1, column=0)

select_button = Button(text="Upload PDF", command=upload, bg=ORANGE, font=("Courier", 10), pady=5, padx=5)
select_button.grid(row=2, column=0)

window.mainloop()