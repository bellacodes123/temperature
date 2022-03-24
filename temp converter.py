from tkinter import *

from functools import partial #to prvent unwanted windows
import random

class Convertor:
    def __init__(self, parent):
        
        #Formatting variables
        background_color = "light blue"

        #Converter frame
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        #Tempreature Conversion Heading (Row 0)
        self.temp_heading_label = Label (self.converter_frame, text="Tempreature Convertor",
                                           font=("Arial", "16", "bold"), bg=background_color,
                                           padx=10, pady=10)
        self.temp_heading_label.grid(row=1)

        #User instructions(row 1)
        self.temp_instructions = Label(self.converter_frame, text="Type in the amount to be convertred, then press one of the buttons below",
                                        font=("Arial", "14"), wrap=250, justify=LEFT, padx=10, pady=10, bg=background_color)
        self.temp_instructions.grid(row=1)

        #Tempresture entry box
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)
        
        #Conversion buttons frame (row 3), orchid3 | khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)
        
        self.to_c_button = Button(self.conversion_buttons_frame,
                                       text="To Centigrade", font="Arial 10 bold",
                                       highlightbackground='Khaki1', padx=10, pady=10)
        
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                       text="To Fahrenheit", font="Arial 10 bold",
                                       highlightbackground="Orchid1", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)
        

        #Answer label (row 4)
        self.converted_label = Label(self.converter_frame,font="Arial 14 bold",
                                     fg="purple", bg=background_color, pady=10, padx=10)
        self.converted_label.grid(row=4)

        #History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15)

        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)


    def to_f(from_c):
        farenheit = (from_c * 9/5) + 32
        return fahrenheit
   

    
        
#main routine

tempreatures = []
converted = []
for item in tempreatures:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statement)
print(converted)
    
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
