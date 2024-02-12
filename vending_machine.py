from tkinter import Tk, Button, Label, Frame, END
from twilio.rest import Client
from tkinter.messagebox import showinfo

class VendingMachine(Frame):
    def __init__(self,root):
        Frame.__init__(self, root)
        self.label = Label(text= "Please enter the product code!", fg = "black", bg = "white", font=('Helvetica', 35), anchor="e", padx=50)
        self.label.grid(column=0, row=0, columnspan=3, sticky='nsew')

        Button1 = Button(text= "1", command=self.oneClicked)
        Button1.grid(column=0, row=1, sticky='nsew')
        Button2 = Button(text= "2", command=self.twoClicked)
        Button2.grid(column=1, row=1, sticky='nsew')
        Button3 = Button(text= "3", command=self.threeClicked)
        Button3.grid(column=2, row=1, sticky='nsew')

        Button4 = Button(text= "4", command=self.fourClicked)
        Button4.grid(column=0, row=2, sticky='nsew')
        Button5 = Button(text= "5", command=self.fiveClicked)
        Button5.grid(column=1, row=2, sticky='nsew')
        Button6 = Button(text= "6", command=self.sixClicked)
        Button6.grid(column=2, row=2, sticky='nsew')

        Button7 = Button(text= "7", command=self.sevenClicked)
        Button7.grid(column=0, row=3, sticky='nsew')
        Button8 = Button(text= "8", command=self.eightClicked)
        Button8.grid(column=1, row=3, sticky='nsew')
        Button9 = Button(text= "9", command=self.nineClicked)
        Button9.grid(column=2, row=3, sticky='nsew')

        Button0 = Button(text= "0", command=self.zeroClicked)
        Button0.grid(column=1, row=4, sticky='nsew')

        Button_clear = Button(text= "Clear!", command=self.clearClicked)
        Button_clear.grid(column=2, row=4, sticky='nsew')

        Button_buy = Button(text= "Buy!", command=self.buyClicked)
        Button_buy.grid(column=0, row=4, sticky='nsew')
        

    def oneClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="1")
        else:
            self.label.config(text=current_text + "1")

    def twoClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="2")
        else:
            self.label.config(text=current_text + "2")

    def threeClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="3")
        else:
            self.label.config(text=current_text + "3")

    def fourClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="4")
        else:
            self.label.config(text=current_text + "4")
    
    def fiveClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="5")
        else:
            self.label.config(text=current_text + "5")

    def sixClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="6")
        else:
            self.label.config(text=current_text + "6")

    def sevenClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="7")
        else:
            self.label.config(text=current_text + "7")

    def eightClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="8")
        else:
            self.label.config(text=current_text + "8")

    def nineClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="9")
        else:
            self.label.config(text=current_text + "9")

    def zeroClicked(self):
        current_text = self.label.cget("text")
        if current_text == "Please enter the product code!":
            self.label.config(text="0")
        else:
            self.label.config(text=current_text + "0")

    def buyClicked(self):
            products = {111: "lays chips", 112: "hersheys", 113: "coca cola", 114: "healthy yoghurt"}
            prices = {111: '$3.25', 112: "$1.75", 113: "$1.00", 114: "$3.25"}
            current_text = self.label.cget("text")
            try:
                account_sid = '##'
                auth_token = '##'
                client = Client(account_sid, auth_token)
                message = client.messages.create(from_ = '+####', body=f'{products[int(current_text)]} has been bought. Price = {prices[int(current_text)]}', to='+####')
            except KeyError:
                showinfo(message= "This item is not on the vending machine!!")
                self.label.config(text = "Please enter the product code!")
    def clearClicked(self):
        self.label.config(text = "Please enter the product code!")




root = Tk()
root.title("Vending Machine")
root.attributes("-fullscreen", True)
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
starter = VendingMachine(root)
starter.grid()
root.mainloop()