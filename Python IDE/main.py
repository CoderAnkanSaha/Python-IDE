from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import subprocess

path = ''
def SaveAs(event = None):
    global path
    path= filedialog.asksaveasfilename(filetypes= [('Python Files', '*.py')], defaultextension = ('.py'))
    if path != "":
        file = open(path,'w')
        file.write(textarea.get(1.0,END))
        file.close()
        messagebox.showinfo('Success',"File Successfully Saved")

def openfile(event = None):
    global path
    path = filedialog.askopenfilename(filetypes=[('Python Files', '*.py')], defaultextension=('.py'))
    if path != '':
        file = open(path,'rt')
        data = file.read()
        textarea.delete(1.0,END)
        textarea.insert(1.0,data)
        file.close()

def Save(event = None):
    global path
    if path == '':
        SaveAs()
    else:
        file =  open(path,'w')
        file.write(textarea.get(1.0,END))
        file.close()

def New(event = None):
    global path
    path = ''
    textarea.delete(1.0,END)
    Outputarea.delete(1.0,END)

def ProgExit(event = None):
    result = messagebox.askyesno('Confirm', 'Do You Want to Exit')
    if result:
        root.destroy()
    else:
        pass

def theme():
    if check.get() == 'light':
        textarea.config(bg='white',fg='black')
        Outputarea.config(bg='white',fg='black')
    
    if check.get() == 'dark':
        textarea.config(bg='gray20',fg='white')
        Outputarea.config(bg='gray20',fg='white')

def clear():
    textarea.delete(1.0,END)
    Outputarea.delete(1.0,END)

def run_code(event = None):
    if path == '':
        messagebox.showerror('Error', 'Please save the file before running it')
    else:
        command = f'python {path}'
        runfile = subprocess.Popen(command, stdout=subprocess.PIPE, stderr= subprocess.PIPE, shell=True)
        output,error = runfile.communicate()
        Outputarea.delete(1.0, END)
        Outputarea.insert(1.0,output)
        Outputarea.insert(1.0,error)

def font_up(event = None):
    global font_size
    if font_size>=32:
        pass
    else:
        font_size=font_size+1
    textarea.config(font=('arial',font_size,'bold'))

def font_down(event = None):
    global font_size
    if font_size>=11:
        font_size=font_size-1
    else:
        pass
    textarea.config(font=('arial',font_size,'bold'))


font_size= 18

root = Tk()
root.geometry('1270x680+0+0')
root.title(("Python Editor"))

check = StringVar()
check.set('light')
myMenu = Menu()
# fileMenu = Menu(myMenu) -----> will tear off file menu , by default tearoff is taken as true
fileMenu = Menu(myMenu,tearoff=False)
fileMenu.add_command(label='New File', accelerator= 'Ctrl+N',command= New)
fileMenu.add_command(label='Open File',accelerator= 'Ctrl+O', command= openfile)
fileMenu.add_command(label='Save',accelerator= 'Ctrl+S',command= Save)
fileMenu.add_command(label='Save As',accelerator= 'Ctrl+G', command= SaveAs)
fileMenu.add_command(label='Exit',accelerator= 'Ctrl+E',command=ProgExit)

myMenu.add_cascade(label='File',menu=fileMenu)


themeMenu = Menu(myMenu,tearoff=False)
themeMenu.add_radiobutton(label='Light', variable= check, value= 'light', command=theme)
themeMenu.add_radiobutton(label='Dark', variable= check, value= 'dark', command=theme)
myMenu.add_cascade(label='Themes',menu=themeMenu)

myMenu.add_command(label='Clear',command=clear)

myMenu.add_command(label='Run',accelerator= 'Ctrl+R',command=run_code)

editFrame = Frame(root, bg='white')
editFrame.place(x=0,y=0,height=500, relwidth=1)

scroll_bar= Scrollbar(editFrame,orient=VERTICAL)
scroll_bar.pack(side=RIGHT,fill=Y)
textarea = Text(editFrame,font=('arial', font_size,'bold'),yscrollcommand=scroll_bar.set)
textarea.pack(fill=BOTH)
scroll_bar.config(command=textarea.yview)

OutputFrame = LabelFrame(root, bg='grey',text="Output",font=('arial', 12,'bold'))
OutputFrame.place(x=0,y=501,height=270, relwidth=1)

scroll_bar1= Scrollbar(OutputFrame,orient=VERTICAL)
scroll_bar1.pack(side=RIGHT,fill=Y)
Outputarea = Text(OutputFrame,font=('arial', font_size,'bold'),yscrollcommand=scroll_bar1.set)
Outputarea.pack(fill=BOTH)
scroll_bar1.config(command=Outputarea.yview)

root.config(menu= myMenu)

root.bind('<Control-n>',New)
root.bind('<Control-o>',openfile)
root.bind('<Control-s>',Save)
root.bind('<Control-g>',SaveAs)
root.bind('<Control-q>',ProgExit)
root.bind('<Control-r>',run_code)
root.bind('<Control-p>',font_up)
root.bind('<Control-m>',font_down)

root.mainloop()