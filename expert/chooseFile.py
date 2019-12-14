import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()

print(tkFileDialog.askopenfilename())
