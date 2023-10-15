import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from PIL import Image, ImageTk
root = tk.Tk()
root.resizable(1,1)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.title("RightDown")
parentMenu = tk.Menu(root)
root.config(menu=parentMenu)

style = ttk.Style()
# menus
subMenus = {
    "File":["New","Open...","Open Recent","hr","Close","Save...","Duplicate","Rename...","Move To...","Revert To","hr","Export as PDF…","Share","hr","Show Properties","hr","Page Setup...","Print..."],

    "Edit":["Undo", "Redo","hr", "Cut", "Copy", "Paste", "Paste and Match Style", "Delete", "Complete", "Select All","hr", "Insert", "Attach Files...", "Add Link...","hr", "Find", "Spelling and Grammar", "Substitutions", "Transformations", "Speech", "hr","AutoFill", "Start Dictation...", "Emoji & Symbols"],

    "Format":["Font", "Text","hr", "Make Plain Text", "Prevent Editing", "Wrap to Page", "Allow Hyphenation", "Make Layout Vertical","hr", "List...", "Table..."],

    "View":["Show Tab Bar", "Show All Tabs","hr", "Use Dark Background for Windows","hr", "Actual Size", "Zoom In", "Zoom Out","hr", "Enter Full Screen"],

    "Window":["Minimise", "Zoom", "Tile Window to Left of Screen", "Tile Window to Right of Screen", "Replace Tiled Window","hr", "Remove Window from Set","hr", "Show Previous Tab", "Show Next Tab", "Move Tab to New Window", "Merge All Windows","hr", "Bring All to Front","hr","Untitled 2"],

    "Help":["RightDown Help"]
}


def addMenu(parent: tk.Menu,menuName: str,menuItems: list):
    subMenu = tk.Menu(parent)
    for item in menuItems:
        if item == "hr":
            subMenu.add_separator()
        else:
            subMenu.add_cascade(label=item)
    parent.add_cascade(label=menuName,menu=subMenu, command=lambda:0)

for subMenu in subMenus:
    addMenu(parentMenu, subMenu, subMenus[subMenu])

# main frame
mainFrame = ttk.Frame(root)
mainFrame.rowconfigure(1,weight=1)
mainFrame.columnconfigure(0,weight=1)
mainFrame.grid(row=0,column=0, sticky="NEWS")

# toolbar
toolbarFrame = ttk.Frame(mainFrame)
# toolbarFrame.rowconfigure(0,weight=1)
# toolbarFrame.columnconfigure(0,weight=1)
toolbarFrame.grid(row=0, column=0, sticky="WE",padx=10)

# font picker
selectedFont = tk.StringVar()
fontOptions = ["Arial", "Times New Roman", "Calibri", "Helvetica", "Garamond", "Verdana", "Courier", "Comic Sans MS", "Georgia", "Palatino", "Tahoma", "Century Gothic", "Lucida Sans", "Trebuchet MS", "Franklin Gothic", "Baskerville", "Futura", "Rockwell", "Cambria", "Didot", "Bodoni", "Copperplate", "Book Antiqua", "Avant Garde", "Myriad", "Bell MT", "Corbel", "Optima", "Gill Sans", "Brush Script"]
fontOptionMenu = ttk.OptionMenu(toolbarFrame,selectedFont,*fontOptions)
fontOptionMenu.grid(row=0, column=0, sticky="W")

# font weight picker
selectedFontWeight = tk.StringVar()
fontWeightOptions = ["Thin", "Extra Light", "Light", "Regular", "Medium", "Semi-Bold", "Bold", "Extra Bold"]
fontWeightOptionMenu = ttk.OptionMenu(toolbarFrame,selectedFontWeight,*fontWeightOptions)
fontWeightOptionMenu.grid(row=0, column=1, sticky="W")

# font size picker
selectedFontSize = tk.IntVar()
fontSizeOptions = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
fontSizeOptionMenu = ttk.OptionMenu(toolbarFrame,selectedFontSize,*fontSizeOptions)
fontSizeOptionMenu.grid(row=0, column=2, sticky="W")

# colour picker
def pickColour(btn):
    colourCode = colorchooser.askcolor(title="Pick your desired colour")
    print(colourCode)

colourPickerBtn = ttk.Button(toolbarFrame, command=lambda:pickColour(colourPickerBtn))
colourPickerBtn.grid(row=0, column=3, sticky="W")

# bold, italics, underline
styleFrame = ttk.Frame(toolbarFrame)
styleFrame.grid(row=0,column=4, sticky="W")

boldImg = ImageTk.PhotoImage(Image.open("Assignment 2/RightDown/res/bold.png"))
italicsImg = ImageTk.PhotoImage(Image.open("Assignment 2/RightDown/res/italics.png"))
underlineImg = ImageTk.PhotoImage(Image.open("Assignment 2/RightDown/res/underline.png"))

ttk.Button(styleFrame,image=boldImg).grid(row=0,column=0,sticky="WE")
ttk.Button(styleFrame,image=italicsImg).grid(row=0,column=1,sticky="WE")
ttk.Button(styleFrame,image=underlineImg).grid(row=0,column=2,sticky="WE")

# alignment
alignFrame = ttk.Frame(toolbarFrame)
alignFrame.grid(row=0,column=5, sticky="W")

leftAlignImg = ImageTk.PhotoImage(Image.open("Assignment 2/RightDown/res/leftAlign.png"))
rightAlignImg = ImageTk.PhotoImage(Image.open("Assignment 2/RightDown/res/rightAlign.png"))
centerAlignImg = ImageTk.PhotoImage(Image.open("Assignment 2/RightDown/res/centerAlign.png"))
justifyAlignImg = ImageTk.PhotoImage(Image.open("Assignment 2/RightDown/res/justifyAlign.png"))
ttk.Button(alignFrame,image=leftAlignImg).grid(row=0,column=0,sticky="WE")
ttk.Button(alignFrame,image=rightAlignImg).grid(row=0,column=1,sticky="WE")
ttk.Button(alignFrame,image=centerAlignImg).grid(row=0,column=2,sticky="WE")
ttk.Button(alignFrame,image=justifyAlignImg).grid(row=0,column=3,sticky="WE")

# editor
editor = tk.Text(mainFrame)
editor.grid(row=1, column=0,sticky="NEWS")

# loop
root.mainloop()
