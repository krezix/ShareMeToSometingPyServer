import tkinter as tk

class frmOptions(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.lblDefaultBrowser = tk.Label(self.parent,text="Default Browser :")
        self.lblDefaultBrowser.pack(side="left")
        self.txtDefaultBrowser = tk.Entry(self.parent)
        self.txtDefaultBrowser.pack()
if __name__ == "__main__":
    root = tk.Tk()
    frmOptions(root).pack(side="top", fill="both", expand=True)
    root.mainloop()