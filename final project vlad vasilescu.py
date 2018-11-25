#   15-112: Principles of Programming and Computer Science
#   Final Project: OS simulator
#   Name      : Vlad-Radu Vasilescu
#   AndrewID  : vvasiles

#   File Created: November 21, 2018


from Tkinter import *
from datetime import datetime
import threading
from tkFont import *
import os
from tkMessageBox import *
from tkFileDialog import *

# class for the main user interface
class mainWnd:

    def __init__(self):
        self.wnd = Tk()
        self.wnd.title ('Welcome to Blinds!')
        self.wnd.geometry ('1023x768')

        #sets background image
        self.backgroundFrame = Frame (self.wnd, height = 737, width = 1024, bg = '#3CB6AC', cursor = "target") 
        self.backgroundFrame.place (x = 0, y = 0)
        self.backgroundImage = PhotoImage (file = './background.gif')
        self.backgroundLabel = Label(self.wnd, image = self.backgroundImage, cursor = "target")
        self.backgroundLabel.image = self.backgroundImage
        self.backgroundLabel.place(x=0, y=0)

        self.bar = Frame (self.wnd, height = 31, width = 1024, bg = '#3C59ED', cursor = "heart", bd = 1 )
        self.bar.place (x = 0, y = 737)

        #clock building
        self.timeString = datetime.now().strftime('%H:%M:%S')
        self.timeLabel = Label(self.wnd, text = self.timeString, width = 14, height = 1, bg = '#3EC0DF', cursor = "watch", font = 'times 7 bold')
        self.timeLabel.place (x = 1023, y = 737, anchor = NE)
        self.dateString = datetime.now().strftime('%d/%m/%Y')
        self.dateBox = Label (self.wnd, text = self.dateString, height = 1, width = 14, bg = '#3EC0DF', cursor = "watch", font = 'times 7 bold')
        self.dateBox.place (x = 1023, y = 753, anchor = NE)
        self.thread = threading.Timer(1.0, self.updateClock)
        self.thread.start()

        #construction of start button that opens start window
        self.start = startWindow(self.wnd)
        self.startButton = Button (self.wnd, cursor = 'heart')
        self.startImage = PhotoImage (file = 'button.gif')
        self.startButton.image = self.startImage
        self.startButton.config (image = self.startImage, width = '41', height = '30', bd = 0, command = self.start.openStartWindow)
        self.startButton.place (x = 0, y= 737)

        #self.wnd.overrideredirect(1)

    #function that updates the clock every second
    def updateClock(self):
        self.timeLabel.config(text = datetime.now().strftime('%H:%M:%S'))
        self.thread = threading.Timer(1.0, self.updateClock)
        self.thread.start()

 # start window class
class startWindow:

    #the widgets from the start window
    def __init__(self, wnd):
        self.wnd = wnd
        self.startWnd = Frame(wnd, height = 281, width = 250)
        
        self.backgroundStart = Frame (self.startWnd, height = 281, width = 250 , bg = '#3EC0DF', cursor = "target")

        self.canvasButton = Button (self.startWnd, cursor = 'spraycan')
        self.canvasImage = PhotoImage (file = 'canvas.gif')
        self.canvasButton.image = self.canvasImage
        self.canvasButton.config (image = self.canvasImage, width = 95, height = 95)

        self.wordButton = Button (self.startWnd, cursor = 'pencil')
        self.wordImage = PhotoImage (file = 'word.gif')
        self.wordButton.image = self.wordImage
        self.wordButton.config (image = self.wordImage, width = 95, height = 95, command = self.openNotepad)


        self.calcButton = Button (self.startWnd, cursor = 'pirate')
        self.calcImage = PhotoImage (file = 'calculator.gif')
        self.calcButton.image = self.calcImage
        self.calcButton.config (image = self.calcImage, width = 95, height = 95, command = self.openCalculator)


        self.pongButton = Button (self.startWnd, cursor = 'mouse')
        self.pongImage = PhotoImage (file = 'pong.gif')
        self.pongButton.image = self.pongImage
        self.pongButton.config (image = self.pongImage, width = 95, height = 95)

        self.shutButton = Button (self.startWnd, cursor = 'pirate')
        self.shutButton.config (width = 15, height = 2, text = 'Shut Down', font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'red', command = self.wnd.destroy)     
        
        self.logButton = Button (self.startWnd, cursor = 'question_arrow')
        self.logButton.config (width = 15, height = 2, text = 'Log Off', font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
        self.switch = True
        
    #constructs the start window on call
    def openStartWindow(self):
       
        if self.switch:
            self.switch = False
            self.startWnd.place (x = 0, y = 456)
            self.backgroundStart.place (x = 0, y = 0)
            self.canvasButton.place (x = 20, y = 20)
            self.wordButton.place (x = 125, y = 20)
            self.calcButton.place (x = 20, y = 125)
            self.pongButton.place (x = 125, y = 125)
            self.shutButton.place (x = 10, y = 230)
            self.logButton.place (x = 125, y = 230)
        else:
            self.switch = True
            self.startWnd.place_forget()

    #opens calculator app
    def openCalculator(self):
        self.calc = calculator (self.wnd)
        self.calc.openCalculator()

    #calls notepad app
    def openNotepad(self):
        self.notepad = Notepad()
    



class calculator:

    def __init__(self, wnd):
        self.wnd = wnd

    
        # self.calcWnd.title ('Very Scientific Calculator')
        
        #custom frtame implemented for calculator  
        self.border = app(292, 320, self.wnd, 'Very Scientific Calculator')
        self.calcWnd = Frame (self.border.mainFrame, width = 292, height = 290, bg = "light salmon")
        self.calcWnd.place (y = 38)
        self.input = StringVar()
        self.buttons()

    #buttons texture and functionality    
    def buttons(self):

        self.calcEntry = Entry (self.calcWnd, width = 18, textvariable = self.input, fg = "blue", font = "system 22 bold", bg = '#3EC0DF')

        self.butt1 = Button (self.calcWnd, text = '7', command = lambda:self.setEntry('7'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
        
        self.butt2 = Button (self.calcWnd, text = '4', command = lambda:self.setEntry('4'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')

        self.butt3 = Button (self.calcWnd, text = '1', command = lambda:self.setEntry('1'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
     
        self.butt4 = Button (self.calcWnd, text = '.', command = lambda:self.setEntry('.'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = '#3EC0DF')
     
        self.butt5 = Button (self.calcWnd, text = '8', command = lambda:self.setEntry('8'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
   
        self.butt6 = Button (self.calcWnd, text = '5', command = lambda:self.setEntry('5'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
     
        self.butt7 = Button (self.calcWnd, text = '2', command = lambda:self.setEntry('2'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
   
        self.butt8 = Button (self.calcWnd, text = '0', command = lambda:self.setEntry('0'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
     
        self.butt9 = Button (self.calcWnd, text = '9', command = lambda:self.setEntry('9'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
   
        self.butt10 = Button (self.calcWnd, text = '6', command = lambda:self.setEntry('6'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
     
        self.butt11 = Button (self.calcWnd, text = '3', command = lambda:self.setEntry('3'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange')
  
        self.butt12 = Button (self.calcWnd, text = '=', command = self.operation, height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = '#3EC0DF')

        self.butt13 = Button (self.calcWnd, text = '+', command = lambda:self.setEntry('+'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = '#3EC0DF')

        self.butt14 = Button (self.calcWnd, text = '-', command = lambda:self.setEntry('-'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = '#3EC0DF')

        self.butt15 = Button (self.calcWnd, text = '*', command = lambda:self.setEntry('*'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = '#3EC0DF')

        self.butt16 = Button (self.calcWnd, text = '/', command = lambda:self.setEntry('/'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = '#3EC0DF')

        self.butt17 = Button (self.calcWnd, text = 'AC', command = self.clear, height = 3, width = 18, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange red')

        self.butt18 = Button (self.calcWnd, text = 'DEL', command = self.delete, height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = 'orange red')

        self.butt19 = Button (self.calcWnd, text = 'mod', command = lambda:self.setEntry('%'), height = 3, width = 7, font = 'times 8 bold', activebackground = '#3EC0DF', bg = '#3EC0DF')
        

    def setEntry(self,text):
        self.rawEntry = self.input.get()
        if self.rawEntry == 'Error!Check input,Boss':
            self.input.set(text)
        else:
            self.input.set(self.rawEntry + text)

    #verifies syntax errors   
    def operation(self):
        try:
            self.input.set(eval(self.input.get()))
        except:
            self.input.set("Error!Check input,Boss")
    
    def clear(self):    
        self.input.set('')
    
    def delete(self):      
        self.input.set(self.input.get()[:-1])

    #constructs the calculator when called
    def openCalculator(self):
        self.calcEntry.grid (row = 0, columnspan = 4)
        self.butt1.grid (row = 1, column = 0)
        self.butt2.grid (row = 2, column = 0)        
        self.butt3.grid (row = 3, column = 0)        
        self.butt4.grid (row = 4, column = 0)        
        self.butt5.grid (row = 1, column = 1)        
        self.butt6.grid (row = 2, column = 1)        
        self.butt7.grid (row = 3, column = 1)        
        self.butt8.grid (row = 4, column = 1)        
        self.butt9.grid (row = 1, column = 2)        
        self.butt10.grid (row = 2, column = 2)        
        self.butt11.grid (row = 3, column = 2)        
        self.butt12.grid (row = 4, column = 2)        
        self.butt13.grid (row = 1, column = 3)        
        self.butt14.grid (row = 2, column = 3)
        self.butt15.grid (row = 3, column = 3)        
        self.butt16.grid (row = 4, column = 3) 
        self.butt17.grid (row = 5, columnspan = 2)
        self.butt18.grid (row = 5, column = 2)
        self.butt19.grid (row = 5, column = 3)

#class for a custom frame for each application with drag&drop
class app:

    def __init__(self, width, height, wnd, title):


        self.wnd = wnd
        self.mainFrame = Frame (self.wnd, height = height, width = width)
        self.mainFrame.place(x = 100, y = 100)
        self.topBar = Frame (self.mainFrame, height = 31, width = width, bg = '#3EC0DF')
        self.topBar.place (x = 0, y = 0)
        self.topBarTitle = Label (self.topBar, text = title, font = "system 18 bold", bg = 'light salmon')
        self.topBarTitle.pack()

        #exit and minimize buttons; minimize to be implemented in the second checkpoint 
        self.exitB = Button (self.mainFrame, height = 1, width = 1, text = "X", font = "system 8 bold", bg = "red", activebackground = "red", command = self.mainFrame.destroy)
        self.exitB.place(x = 290, y = 2, anchor = 'ne')
        self.minimizeB = Button (self.mainFrame, height = 1, width = 1, text = "_", font = "system 8 bold", bg = "orange", activebackground = 'orange')
        self.minimizeB.place(x = 272, y = 2, anchor = 'ne')

        #active drag and drop 
        self.topBarTitle.bind("<ButtonPress-1>", self.press)
        self.topBarTitle.bind("<ButtonRelease-1>", self.release)
        self.topBarTitle.bind("<B1-Motion>", self.move)
        
    
    def press (self,event):
        self.x = event.x
        self.y = event.y

    def release (self, event):
        self.x = None
        self.y = None

    def move (self, event):
        self.dx = event.x_root - self.x
        self.dy = event.y_root - self.y
        self.mainFrame.place(x = self.dx - self.wnd.winfo_x()-8, y = self.dy - self.wnd.winfo_y() - 30)  



class Notepad:


    def __init__(self):
       
        
        #the window is still a Tk, not a frame in the main window
        #but will be  implemented in checkpoint 2
        self.notepadWnd = Tk()
        self.notepadWnd.geometry('800x600')
        self.notepadWnd.title ("Text Editor 9000")
        self.notepadWnd.configure (background = "salmon")

        #sets the text entry box and initializes menus
        self.inputText = Text(self.notepadWnd, width = 99 , height = 37)
        self.menu = Menu(self.notepadWnd)
        self.fileMenu = Menu(self.menu, tearoff = 0)
        self.editMenu = Menu(self.menu, tearoff = 0)
        self.scrollbar = Scrollbar(self.inputText)
        self.file = None

        self.inputText.pack()
        # file menu and edit menu
        self.fileMenu.add_command(label = "New", command = self.newFile)
        self.fileMenu.add_command(label = "Open", command = self.openFile)
        self.fileMenu.add_command(label = "Save", command = self.saveFile)
        self.fileMenu.add_separator()

        self.fileMenu.add_command(label = "Exit", command = self.notepadWnd.destroy)
        self.menu.add_cascade(label = "File", menu = self.fileMenu)

        self.editMenu.add_command(label = "Cut", command = self.cut)
        self.editMenu.add_command(label = "Copy", command = self.copy)
        self.editMenu.add_command(label = "Paste", command = self.paste)
        self.menu.add_cascade(label = "Edit", menu = self.editMenu)



        self.notepadWnd.config(menu = self.menu)

        # self.scrollbar.place (x = 794, y = 0, anchor = 'ne')
    
        self.scrollbar.config(command = self.inputText.yview)
        self.inputText.config(yscrollcommand = self.scrollbar.set)
        #self.scrollbar.pack ( side = RIGHT, fill = Y )

    #copy, cut, paste functions
    def cut(self):
        self.inputText.event_generate ("<<Cut>>")

    def copy(self):
        self.inputText.event_generate ("<<Copy>>")

    def paste(self):
        self.inputText.event_generate ("<<Paste>>")

    #save file in any format 
    def saveFile(self):

        if self.file == None:
            #save as new file
            self.file = asksaveasfilename(initialfile = 'Meow.txt', defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None
            else:
                #write an empty file with the content of the text box
                file = open (self.file, "w")
                file.write (self.inputText.get(1.0, END))
                file.close()
                #change the window title
                self.notepadWnd.title(os.path.basename (self.file))
                
            
        else:
            file = open (self.file, "w")
            file.write (self.inputText.get(1.0, END))
            file.close()

    def openFile(self):
        
        self.file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.file == "":
            #no file to open
            self.file = None
        else:
            #open the file
            self.notepadWnd.title (os.path.basename (self.file))
            self.inputText.delete (1.0, END)

            #imports file by reading it and inserting it in the text box
            file = open (self.file, "r")

            self.inputText.insert (1.0, file.read())

            file.close()

    #creates new file
    def newFile(self):
        self.notepadWnd.title ("Meow")
        self.file = None
        self.inputText.delete (1.0, END)


    









mainWnd()   
mainloop()