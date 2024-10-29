import tkinter as tk
import ttkbootstrap as ttk #Is a more customisable library than tkinter 

def convert(): # The conversion function 
    mile_input = entry_int.get()
    km_output = mile_input * 1.609
    output_string.set(km_output)

#window
window = ttk.Window(themename = 'darkly') # Setting a theme to the application window (Tkinter approved themes only)
window.title("Any Title") # Setting a title for the application window 

#title costomisation
title_label = ttk.Label(master = window,  # Use of function master not required 
                        text = 'miles to kilometers', # not same as window title, the words entered here will appear in the main operating area of the application 
                        font = 'Arial 26 bold') 
title_label.pack()

#input -- The main frame of the application window where all the interaction is done
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame,  
                  textvariable = entry_int)
button = ttk.Button(master = input_frame,
                    text = 'Convert',
                    command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left') # setting location of button in the window 
input_frame.pack(pady= 10) # setting location of frame in the window 

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window,
                         font = 'Arial 24',
                         textvariable = output_string)
output_label.pack()

#run
window.mainloop()

