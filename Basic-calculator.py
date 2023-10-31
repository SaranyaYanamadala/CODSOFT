from tkinter import *


#clicking function
def click(event) :
   global value
   text = event.widget.cget("text")
   print(text)
   if text == "=" : 
      if value.get().isdigit() :
         resvalue = int(value.get()) #converting the value to integer
      else :
         resvalue = eval(entry.get()) #else evaluating the expression
      value.set(resvalue)
      entry.update() #updating the entry screen

   elif text == "C" :
      value.set("")
      entry.update() #updating the entry screen with blanck space

   else :
      value.set(value.get() + text)
      entry.update() #updating the screen with the corresponding value


root = Tk()

#define the size of the layout 
root.geometry("400x500")
root.minsize(200, 300)
root.maxsize(600, 650)
root.title("Simple Calculator")
root.iconbitmap("calculator-icon_34473.ico")

value = StringVar() #creating object for Stringvar class
value.set("")
entry = Entry(root, textvar = value, font = "Ariel 30 bold")
entry.pack(pady = 15) #placing the entry box


#Adding buttons to the frame 
buttons_list = ['7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-', 
                '0', '.', '=', '+',
                'C'] #List of buttons that are basic 

#Creating buttons in each row
for i in range(0, len(buttons_list), 4) :
   frame = Frame(root, bg = "grey")
   frame.pack(side = "top")

   for button in buttons_list[i : i+4] :
      button = Button(frame, text = button, padx = 15, pady = 15, font = "Ariel 20 bold")
      button.bind("<Button-1>", click)
      button.pack(side = "left", padx = 2, pady = 2)
   

root.mainloop()