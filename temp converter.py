from tkinter import *
from functools import partial  #to prevent unwanted windows
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
        self.temp_heading_label = Label (self.converter_frame,
                                         text="Tempreature Convertor",
                                         font=("Arial", "16", "bold"),
                                         bg=background_color,
                                         padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        #User instructions(row 1)
        self.temp_instructions = Label(self.converter_frame,
                                       text="Type in the amount to be converted, then press one of the buttons below",
                                       font=("Arial", "14"), wrap=250,
                                       justify=LEFT,
                                       padx=10, pady=10, bg=background_color)
        self.temp_instructions.grid(row=1)

        #Tempresture entry box
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)
        
        #Conversion buttons frame (row 3), orchid3 | khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)
        
        self.to_c_button = Button(self.conversion_buttons_frame,
                                  highlightbackground='Khaki1',
                                  text="To Centigrade", font="Arial 10 bold",
                                  padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  highlightbackground="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        #Answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     font="Arial 14 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        #History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15,
                                       padx=5, pady=5)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5,
                                  padx=5, pady=5)
        self.help_button.grid(row=0, column=1)


    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"  #pale pink background when entry box has errors

        #Retrive amount enytered into Entry Field
        
        to_convert = self.to_convert_entry.get()
            
        #Check amount is a valid number
        try:
            convert = float(to_convert)
            has_errors = "no"

            #Convert to F
            if low == -273 and convert >= low:
                farenheit = (convert * 9/5) + 32
                rounded_convert = self.round_it(convert)
                farenheit = self.round_it(farenheit)
                answer = f"{convert} degrees C is {farenheit} degrees F"

            #Convert to C
            elif low == -459 and convert >= low:
                celsius = (convert - 32) * 5/9
                rounded_convert = self.round_it(convert)
                celsius = self.round_it(celsius)
                answer = f"{convert} degrees C is {celsius} degrees F"

            else:
                #input is invalid (too cold)
                answer = "Too Cold!"
                has_errors = "yes"

            #Display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)


        #Add answer to list for history
        except ValueError:
            print("oops")
            self.converted_label.configure(text="Enter a number:", fg="red")
            self.to_convert_entry.configure(bg=error)

    #round!
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)

        else:
            rounded = round(to_round, 1)

            return rounded

    
#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
