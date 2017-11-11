from tkinter import *
from PIL import Image, ImageTk
from threading import Timer
import random
import time
import xlwt
root = Tk()
class C:
    a = 0
    b = 0
    z = 0
    f = 0
    row1 = 0
    counter = 0
    currenttime = time.time()
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Python Sheet 1")
arr = ['1.jpg', '2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg']
arr_machine = ['Bulbasaur.gif', 'tank1.png', 'tank2.png', 'tank3.png', 'tank4.png', 'tank5.gif', 'tank6.png', 'tank7.png', 'tank8.png', 'tank9.png', 'tank10.png']
for i in arr:
    img = Image.open(i)
    resized_img = img.resize((800, 500), Image.ANTIALIAS)
    resized_img.save(i)
for i in arr_machine:
    img = Image.open(i)
    resized_img = img.resize((100, 100), Image.ANTIALIAS)
    resized_img.save(i)
C.a = random.randrange(1, 800)
C.b = random.randrange(1, 500)
img = [ImageTk.PhotoImage(Image.open(arr[0])),ImageTk.PhotoImage(Image.open(arr[1])),ImageTk.PhotoImage(Image.open(arr[2])),ImageTk.PhotoImage(Image.open(arr[3])),ImageTk.PhotoImage(Image.open(arr[4])),ImageTk.PhotoImage(Image.open(arr[5])),ImageTk.PhotoImage(Image.open(arr[6]))]
tanks = [ImageTk.PhotoImage(Image.open(arr_machine[0])),ImageTk.PhotoImage(Image.open(arr_machine[1])),ImageTk.PhotoImage(Image.open(arr_machine[2])),ImageTk.PhotoImage(Image.open(arr_machine[3])),ImageTk.PhotoImage(Image.open(arr_machine[4])),ImageTk.PhotoImage(Image.open(arr_machine[5])),ImageTk.PhotoImage(Image.open(arr_machine[6])),ImageTk.PhotoImage(Image.open(arr_machine[7])),ImageTk.PhotoImage(Image.open(arr_machine[8])),ImageTk.PhotoImage(Image.open(arr_machine[9]))]
canvas = Canvas(root,width=800,height=500)
but = Button(root,text="Next")
var=StringVar()
var.set(0)
lab = Label(root, textvariable=var)
canvas.grid(row = 0, column = 0,rowspan = 3)
but.grid(row = 0, column = 1)
lab.grid(row = 1, column = 1)
class perpetualTimer():
   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()
def printer():
    while(C.counter < 15):
        C.z = time.time() - C.currenttime
        var.set("%.3f" % C.z)
t = perpetualTimer(0,printer)
t.start()
canvas.create_image(0,0,image=img[C.a%7], anchor = NW)
canvas.create_image(C.a,C.b,image=tanks[C.a%10], anchor = NW)

def on_click(event):
    if event.x >= C.a and event.y >= C.b and event.x <= C.a + 100 and event.y <= C.b + 100:
        C.currenttime = time.time()
        canvas.delete("all")
        C.a = random.randrange(100, 700)
        C.b = random.randrange(100, 400)
        canvas.create_image(0, 0, image=img[C.a%7], anchor=NW)
        canvas.create_image(C.a, C.b, image=tanks[C.a%10], anchor=NW)
        C.f = C.f + 1
        sheet1.write(C.row1, 0, "Спроба № " + str(C.f))
        sheet1.write(C.row1, 1, "Літачок знайдено ")
        sheet1.write(C.row1, 2, "Затрачений час " + str("%.2f" % C.z))
        C.row1 = C.row1 + 1
        C.counter = C.counter + 1
        C.z = 0
        if C.counter > 14:
            t.cancel()
            book.save("spreadsheet.xls")
            root.destroy()
def on_click_listener(event):
    C.currenttime = time.time()
    canvas.delete("all")
    C.a = random.randrange(100, 700)
    C.b = random.randrange(100, 400)
    canvas.create_image(0, 0, image=img[C.a%7], anchor=NW)
    canvas.create_image(C.a, C.b, image=tanks[C.a%10], anchor=NW)
    C.f = C.f + 1
    sheet1.write(C.row1, 0, "Спроба № " +  str(C.f))
    sheet1.write(C.row1, 1, "Літачок не знайдено ")
    sheet1.write(C.row1, 2, "Затрачений час " + str("%.2f" % C.z))
    C.row1 = C.row1 + 1
    C.counter = C.counter + 1
    C.z = 0
    if C.counter > 14:
        t.cancel()
        book.save("spreadsheet.xls")
        root.destroy()
canvas.bind('<1>', on_click)
but.bind('<1>', on_click_listener)
root.minsize(width=1000, height=500)
root.maxsize(width=1000, height=500)
root.mainloop()
