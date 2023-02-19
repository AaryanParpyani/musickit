# from tkinter import *

# root = Tk()
# root.geometry('300x300')
# root.title("Drumkit")
# root.iconbitmap(r'drumkit.ico')

# root.mainloop()
from tkinter import *

# bottom=Tk()
#   bottom.geometry('')

root = Tk()
root.geometry('1024x2000')
root.title("DrumKit")
root.iconbitmap(r'drumkit.ico')

text = Label(root, text='Lets make some noise!')
text.pack()

photo = PhotoImage(file='drums.png')
photo = PhotoImage(file='Drumkit_2.png')
labelphoto = Label(root, image = photo)
labelphoto.pack()

root.mainloop()
