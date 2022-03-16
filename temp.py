from tkinter import *

from functools import partial #to prvent unwanted windows
import random

class Convertor:
    def __init__(self, parent):
        
        #Formatting variables
        background_color = "light blue"

        #converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        #Tempreature Conversion Heading (Row)
        self.temp_converter_label = Label (text="Tempreature Convertor",
                                           font=("Arial", "16", "bold"),
                                           padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        
#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
