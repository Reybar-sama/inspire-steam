from tkinter import *

def wahgwaan():
    print("Tell your girl I said wagwannn!!!")


root = Tk()
root.geometry("640x480")
frame_one = Frame(root)
frame_one.pack()

button_one = Button(frame_one, text="Say wah gwaan!", command = wahgwaan)
button_one.pack()
root.mainloop()


