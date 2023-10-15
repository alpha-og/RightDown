import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(1,1)
parentMenu = tk.Menu(root)
root.config(menu=parentMenu)

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

root.mainloop()
