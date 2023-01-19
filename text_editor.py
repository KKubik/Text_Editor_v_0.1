from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('Text editor')
size = '600x450'
root.geometry(size)


def save_button(name):
    text_to_save = T.get('1.0', END)
    with open(name, 'w') as f:
        f.write(text_to_save)


def clear():
    T.delete('1.0', END)


def search(main_text):
    global pop
    pop = Toplevel(root)  # our popup window for search
    pop.title("Search")
    pop.geometry("350x250")
    global search_text
    search_text = Text(pop, height=10, width=30)
    search_button_pop = Button(pop, text='Search', padx=20, pady=10,
                               command=lambda: find_text(main_text))
    search_text.pack()
    search_button_pop.pack()


def find_text(txt):
    search_text_string = str(search_text.get('1.0', END))  # Text we typed and trying to find
    search_text_string = search_text_string.strip()
    word_length = len(search_text_string)
    line_number = 1
    for line_txt in txt:
        start_location = line_txt.find(search_text_string)
        if start_location != -1:
            end_location = str(start_location + word_length)
            start_location = str(line_number) + '.' + str(start_location)
            end_location = str(line_number) + '.' + end_location

            T.tag_add("start", start_location, end_location)
            T.tag_config("start", background="black", foreground="white")

            pop.destroy()
            break
        line_number += 1

    if start_location == -1:
        not_found()


def not_found():
    not_pop = Toplevel(pop)
    not_pop.title("Words not found!")
    not_pop.geometry('250x100')
    not_label = Label(not_pop, text="Couldn't find words in text!")
    not_button = Button(not_pop, text="Ok", padx=20, pady=10, command=not_pop.destroy)
    not_label.pack()
    not_button.pack()


# very simple printing, instant
def print_text():
    # p = win32print.OpenPrinter("Samsung ML-2010")
    os.startfile('our_text.txt', 'print')


T = Text(root, height=20, width=50, borderwidth=1)

# Create label
lab = Label(root)

# browse for file to open
file_name = filedialog.askopenfilename(initialdir='/',
                                       title="Select a text file to open",
                                       filetypes=(('Text files',
                                                   '*.txt*'),
                                                  ('all files',
                                                   '*.*')))
with open(file_name, 'r') as file:
    text_read = file.readlines()

# load all the lines from file into text window
for line in text_read:
    T.insert(END, line)

add_button = Button(root, text='Save', padx=20, pady=10, command=lambda: save_button(file_name))
clear_button = Button(root, text='Clear', padx=20, pady=10, command=clear)
search_button_main = Button(root, text='Search', padx=20, pady=10, command=lambda: search(text_read))
print_button = Button(root, text='Print', padx=20, pady=10, command=print_text)

lab.pack()
lab.focus_force()  # focus on this window so that you can edit text (don't really know why)
T.place(x=10, y=50)
add_button.place(x=10, y=5)
clear_button.place(x=100, y=5)
search_button_main.place(x=200, y=5)
print_button.place(x=300, y=5)

root.mainloop()
