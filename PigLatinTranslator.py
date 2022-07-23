# This program translates english into pig latin
# and also creates a GUI to perform this task
import tkinter as tk
from tkinter import ttk
import time

# Defines variables for consonants and vowels
con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

# A couple of examples
example1 = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question.']
example2 = ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog.']

# The tkinter my_gui class
class pigLatinTranslatorGUI:
    def __init__(self):
         # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title('Pig Latin Translator')
        self.tabs = ttk.Notebook()

        # Create the tab frames
        self.help_tab = tk.Frame(self.tabs)
        self.main_tab = tk.Frame(self.tabs)

        self.tabs.add(self.help_tab, text ='HELP')
        self.tabs.add(self.main_tab, text ='MAIN')

        self.tabs.pack(expand = 1, fill = 'both')

        # The StringVar for updating labels
        self.varStr = tk.StringVar()

        # The frames
        self.frm_buttons = tk.Frame(self.main_tab, relief=tk.RAISED, bd=2)

        # The label
        self.l1 = tk.Label(self.main_tab, text = "Here Is the full Translation: ")
        self.l2 = tk.Label(self.main_tab, textvariable = self.varStr)

        # The variable and label for the help page
        self.help_text = "\
                        This is a pig latin translator. It can only convert English to Pig\n\
                        Latin at this current point. In order to translate your text simply\n\
                        go to the 'MAIN' tab and type your text into the box. Then press\n\
                        Translate. Your translated text will appear below.\n\
                            \n\
                        LIMITATIONS:\n\
                        There are a few limitations to this program. For one it can only actually\n\
                        handle three types of punctuation: period(.), comma(,) and appostrophe(').\n\
                        If it handles any other type of punctuation it is entirely coincidental.\n\
                        And also, this program can't handle more than one sentence sucessfully, so\n\
                        please keep that in mind. Thanks for downloading!\n\
                        \n\
                        And don't forget, 'Avehay ayay eatgray imetay!"

        self.help_label = tk.Label(self.help_tab, text = self.help_text)

        # Basic entry box
        self.entry1 = tk.Text(self.main_tab)

        # The buttons
        self.translate_button = tk.Button(self.frm_buttons, text = 'Translate', command = self.quickTranslate)

        # Building the grid
        self.entry1.grid(row = 0, column = 1, sticky = tk.W, pady = 2)
        self.l1.grid(row = 1, column = 1, sticky = tk.S, pady = 2)
        self.l2.grid(row = 2, column = 1, sticky = tk.S, pady = 2)
        self.help_label.grid(row = 1, column = 0, sticky = tk.N, pady = 2)
        self.translate_button.grid(row = 0, column = 0, sticky = tk.NW, pady = 2)
        self.frm_buttons.grid(row = 0, column = 0)

        # Start the mainloop
        tk.mainloop()

    def quickTranslate(self):
        # Translate the text and output it
        text = self.entry1.get(1.0, "end-1c")

        listX = text.split()

        for i in range(0, len(listX)):
            listX[i] = translate(listX[i])

        # The following lines do some work to make the
        # sentence into a sentence
        newText = listX.pop(0)
        newText = newText.capitalize()
        space = " "

        for i in listX:
            newText = newText + space
            newText = newText + i

        if newText[-1] != '.':
            newText += '.'

        self.varStr.set(newText)


# The main function
def main():
    latin_gui = pigLatinTranslatorGUI()
        

# Translate takes a string or and returns the pig latin equivalent
def translate(text):
    # Define some variables
    tempText = text.lower() # A variable to hold the text, but all lowercase
    i = 0   # An iteration variable
    tempList = breakString(text.lower())    # Break the string into a list
    has_comma = 0       # Variable to store if there is a comma
    has_period = 0      # Variable to store if there is a period

    # Remove comma or period
    if tempList[-1] == ',':
        has_comma = 1
        tempList[-1] = ''
        tempText = tempText[:-1]

    if tempList[-1] == '.':
        has_period = 1
        tempList[-1] = ''
        tempText = tempText[:-1]

    # Perform the pig latin translation
    if tempList[0] in vowels:
        tempText += 'yay'
    else:
        while tempList[i] not in vowels:
            temp = tempList[i]
            tempList[i] = ''
            tempList.append(temp)
            i += 1

        # Add the final 'ay'
        tempList.append('ay')

        # Change the list back into a string
        tempText = ''
        for i in tempList:
            tempText += i

    # Replace comma, if it had one
    if has_comma == 1:
        tempText += ','
    if has_period == 1:
        tempText += '.'

    # Return tempText
    return tempText

# breakString is used to break the string into a list of characters
def breakString(text):
    list1 = []
    for i in text:
        list1.append(i)
    return list1

# Call the main function
main()