import tkinter
from tkinter import *
import pandas as pd
import random
import datetime as dt
import time

BACKGROUND_COLOR = "#16425d"


correctly_typed = []
wrong = []
countdown_ended = False
paragraph = ""
paragraph_letters = []
current_letter_index = 0
round_active = False
current_word_start = 0
current_word_end = 0
current_word_correct = []
round_num = 1
current_word = ""

start_time = 0.0
elapsed_time = 0.0


def update_timer():
    global start_time, elapsed_time, round_active

    # Critical Safeguard: If time calculation breaks or hasn't started, exit early
    if not round_active or start_time == 0.0:
        return

    # Accurate current runtime measurement
    elapsed_time = time.time() - start_time

    # :.1f restricts output strictly to one decimal position (e.g., 4.2s)
    timer_label.config(text=f"Time: {elapsed_time:.1f}s")

    # Queue up the next visual refresh
    window.after(100, update_timer)

def load_paragraph():
    global paragraph, paragraph_letters
    paragraph = ""
    paragraph_letters = []
    df = pd.read_csv('paragraphs.csv')
    para_num = random.randint(0,len(df.paragraph)-1)
    paragraph = df["paragraph"][para_num]

    for letter in paragraph:
        paragraph_letters.append(letter)
    return paragraph_letters

def display_paragraph():
    global paragraph, round_num
    if round_num > 1:
        global text_box
        text_box.config(state="normal")
        text_box.delete("1.0", "end")
        text_box.insert(tkinter.END, paragraph)
        text_box.config(state="disabled")
        highlight_letter(current_letter_index, True)
    else:
        text_box = Text(window, height = 10, width = 70, state="normal", font=("Times New Roman", 20, "normal"), tabs=("4c", "8c"))
        text_box.insert(tkinter.END, paragraph)
        text_box.config(state="disabled")
        return text_box

def display_results():
    global correctly_typed, wrong, paragraph_letters, paragraph, round_num, elapsed_time

    text_box.tag_delete("my_highlight")
    total_words = len(correctly_typed) + len(wrong)
    accuracy_val = round((len(correctly_typed) / total_words) * 100, 2) if total_words > 0 else 0

    # Convert stopwatch seconds into minute fractions for standard WPM formula
    time_elapsed_minutes = elapsed_time / 60
    if time_elapsed_minutes == 0:
        time_elapsed_minutes = 0.001  # Prevent crash on instant completion

    words_per_minute = round(len(correctly_typed) / time_elapsed_minutes, 1)
    wpm_label.config(text=f"WPM: {words_per_minute}")
    accuracy_label.config(text=f"Accuracy: {accuracy_val}%")



    restart()


def restart():
    global text_box, round_num, round_active
    round_active = False
    round_num += 1
    text_box.config(state = "normal")
    text_box.delete("1.0", "end")
    text_box.insert(tkinter.END, "Press Enter to Restart")
    text_box.config(state="disabled")





def on_key_press(event):
    global round_active, current_letter_index, wrong, correctly_typed, paragraph_letters
    if round_active:
        current_user_char = event.char

        compare(current_user_char, event.keysym)

def compare(current_user_char, keysym):
    global round_active, current_letter_index, wrong, correctly_typed, paragraph_letters, current_word_start, current_word_end, current_word_correct, current_word
    if keysym == "Caps_Lock":
        return None
    else:
        if current_user_char == " " and paragraph_letters[current_letter_index] == " ":

                current_word = ""
                current_word_end = current_letter_index
                correct_list = current_word_correct[current_word_start:current_word_end]

                for index in range(current_word_start,current_word_end):
                    current_word = current_word+paragraph_letters[index]
                correct = True
                for value in correct_list:
                    if value=="False":
                        correct = False

                if correct:
                    correctly_typed.append(current_word)
                    current_word_start = current_word_end + 1


                else:
                    wrong.append(current_word)



        if current_user_char == paragraph_letters[current_letter_index]:

            current_word_correct.append("True")
            current_letter_index += 1
            if current_letter_index == len(paragraph_letters):
                round_active = False
                display_results()
            else:
                highlight_letter(current_letter_index,True )

        else:

            current_word_correct.append("False")
            highlight_letter(current_letter_index, False)




def operator(event):
    global round_active, current_letter_index, wrong, correctly_typed, round_num, paragraph_letters, paragraph, current_letter_index, current_word_start, current_word_start, current_word_correct, current_word_end, start_time

    if not round_active:

        round_active = True
        current_letter_index = 0
        wrong = []
        correctly_typed = []
        current_letter_index = 0
        current_word_start = 0
        current_word_end = 0
        current_word_correct = []

        if round_num > 1:

            paragraph_letters = load_paragraph()

            display_paragraph()
        wpm_label.config(text="WPM: 0.0")
        accuracy_label.config(text="Accuracy: --%")
        start_time = time.time()
        update_timer()


def highlight_letter(letter_index, right):
    global text_box,paragraph_letters
    if right:
        text_box.tag_delete("my_highlight")
        text_box.tag_config("my_highlight", background="blue", foreground=None)
        text_box.tag_add("my_highlight", f"1.{letter_index}")
    else:
        text_box.tag_delete("my_highlight")
        text_box.tag_config("my_highlight", background="red", foreground=None)
        text_box.tag_add("my_highlight", f"1.{letter_index}")
paragraph_letters = load_paragraph()

#GUI
window = tkinter.Tk()
window.geometry("1000x800")
window.title("Typing Speed Test")
window.configure(background=BACKGROUND_COLOR, pady=20)

# Configure column sizes so grid positioning matches layout widths
window.grid_columnconfigure(0, weight=1)

# Header Title
header = tkinter.Label(window, text="Typing Speed Test", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 40, "bold"))
header.grid(row=0, column=0, pady=20)

# Metrics Display Frame (organizes the variables cleanly side-by-side)
stats_frame = tkinter.Frame(window, background=BACKGROUND_COLOR)
stats_frame.grid(row=1, column=0, pady=10)

timer_label = tkinter.Label(stats_frame, text="Time: 0.0s", background=BACKGROUND_COLOR, foreground="yellow", font=("Helvetica", 20, "bold"))
timer_label.pack(side=LEFT, padx=20)

wpm_label = tkinter.Label(stats_frame, text="WPM: 0.0", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 20, "bold"))
wpm_label.pack(side=LEFT, padx=20)

accuracy_label = tkinter.Label(stats_frame, text="Accuracy: --%", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 20, "bold"))
accuracy_label.pack(side=LEFT, padx=20)

# Text Box Layout
text_box = Text(window, height=10, width=70, state="normal", font=("Times New Roman", 20, "normal"), tabs=("4c", "8c"), bg="#222")
text_box.insert(tkinter.END, paragraph)
text_box.config(state="disabled")
text_box.grid(row=2, column=0, pady=40, padx=20)

#Highlighting First Letter
highlight_letter(current_letter_index, True)
#Key listner

window.bind("<Return>", operator )
window.bind("<Key>", on_key_press)








window.mainloop()



