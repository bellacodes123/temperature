from tkinter import *
from functools import partial  # to prevent unwanted windows
import random
import re


class Convertor:
    def __init__(self, parent):
        
        # Formatting variables
        background_color = "light blue"

        # Initialiseing list to holed calculation history
        self.all_calc_list = []

        # Converter frame
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10, padx=90)
        self.converter_frame.grid()

        # Tempreature Conversion Heading (Row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Tempreature Convertor",
                                        font=("Arial", "16", "bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions(row 1)
        self.temp_instructions = Label(self.converter_frame,
                                       text="Type in the amount to be converted, then press one of the buttons below",
                                       font=("Arial", "14"), wrap=250,
                                       justify=LEFT,
                                       padx=10, pady=10, bg=background_color)
        self.temp_instructions.grid(row=1)

        # Tempreature entry box
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)
        
        # Conversion buttons frame (row 3), orchid3 | khaki1
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

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     font="Arial 14 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                     text="Calculation History", width=15,
                                     padx=5, pady=5, command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5,
                                  padx=5, pady=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box"
                                          " then push one of the buttons to "
                                          " convert the number to either C or "
                                          "degrees F. "
                                          " The calculation History area shows up "
                                          "the seven most recent calculations."
                                          " You can also export your calculation history "
                                          "to a text file if desired.")

    def history(self, calc_history):
        History(self, calc_history)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"  # pale pink background when entry box has errors

        # Retrive amount entered into Entry Field
        
        to_convert = self.to_convert_entry.get()
            
        # Check amount is a valid number
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = f"{to_convert} degrees C is {fahrenheit} degrees F"

            # Convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = f"{to_convert} degrees F is {celsius} degrees C"

            else:
                # input is invalid (too cold)
                answer = "Too Cold!"
                has_errors = "yes"

            # Display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add answer to list for history
            if answer != "Too Cold":
                self.all_calc_list.append(answer)
                self.history_button.config(state=NORMAL)
                print(self.all_calc_list)

        # Add answer to list for history
        except ValueError:
            print("oops")
            self.converted_label.configure(text="Enter a number:", fg="red")
            self.to_convert_entry.configure(bg=error)

    # round!
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)

        else:
            rounded = round(to_round, 1)

        return rounded


class Help:
    def __init__(self, partner):

        background = "orange"

        # disbable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window help box
        self.help_box = Toplevel()
        # If users press cross at to, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help Text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="orange",
                                  font="arial 10 bold",
                                  command=partial(self.close_help,partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class History:
    def __init__(self, partner, calc_history):
        background = "#a9ef99"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window
        self.history_box = Toplevel()

        # If users press cross at to it closes history and 'realeses' history
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="Arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # History text (label, row 1)
        self.history_text = Label(self.history_frame, text="",
                                  justify=LEFT, width=40, bg=background,
                                  wrap=250)
        self.history_text.grid(row=1)

        # history text
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent"
                                        " calculations. Please use the"
                                        " export button to create a text"
                                        " file of all your calculations for this session",
                                  wrap=250, font="arial 10 italic", justify=LEFT, bg=background,
                                  fg="maroon", padx=10, pady=10)
        self.history_text.grid(row=1)

        # history output

        # Generate string from list of calculations
        history_string = ""

        if len(calc_history) >=7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)- item - 1] +"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item)
                                               -1] + "\n"
                self.history_text.config(text ="Here is your calculation history. "
                                                "You can use the export button "
                                                "to save this data to a file if desired.")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export /dismiss button
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font= "Arial 12 bold",
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):
        background = "Orchid1"
        print(calc_history)

        # disable history button
        partner.export_button.config(state=DISABLED)

        # sets up child window
        self.export_box = Toplevel()

        # If users press cross at to it closes history and 'realeses' history
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set up history heading
        self.how_heading = Label(self.export_frame, text="Export Files",
                                 font="Arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below"
                                                         " and press the save button to save as a text file ",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning label
        self.export_text = Label(self.export_frame, text="If the filename you enter already exists, it's contents will"
                                                          " be replaced with your calculation history.",
                                 justify=LEFT, width=40, bg="maroon", wrap=225, fg="white")
        self.export_text.grid(row=2)

        # Entry box :)
        self.export_entry = Entry(self.export_frame, width=20,
                                  font="Arial 14 bold", justify=CENTER)
        self.export_entry.grid(row=3, pady=20, padx=10)

        # error label
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # save cancel frame
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        # Regular expression to check filename
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.export_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue
            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed".format(letter))
                break
        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # change entry box background pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # if there are no errors generate text file add txt suffix
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

            self.close_export(partner)



    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Tempreature Convertor")
    something = Convertor(root)
    root.mainloop()
