import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

class frmOptions(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frmDefaultBrowser = tk.Frame(self)
        
        self.browsers = ["Mozilla Firefox", 
                         "Google Chrome",
                         "Internet Explorer",
                         "Safari",
                         "Opera"]
                                    
        self.lblDefaultBrowser = tk.Label(self.frmDefaultBrowser,text="Default Browser :")
        self.lblDefaultBrowser.pack(side="left")
        #self.txtDefaultBrowser = tk.Entry(self)
        #self.txtDefaultBrowser.pack(side="left", fill=tk.X,expand=True)
        self.cbDefaultBrowser = tk.ttk.Combobox(self.frmDefaultBrowser, state="readonly",
                                    values=self.browsers)
        self.cbDefaultBrowser.current(0)
        self.cbDefaultBrowser.bind("<<ComboboxSelected>>", self.OncbDefaulBrowserSelected) # for multiple combos use lambda event:self.OncbDefaulBrowserSelected(event, "Hello"))
        self.cbDefaultBrowser.pack(side="left", fill=tk.X, expand=True)
        self.frmDefaultBrowser.pack(fill=tk.X, ipadx=2, ipady=2)

        self.frmBrowserLocation = tk.Frame(self)
        self.lblBrowserLocation = tk.Label(self.frmBrowserLocation, text="Browser Location :")
        self.lblBrowserLocation.pack(side="left")
        self.txtBrowserLocation = tk.Entry(self.frmBrowserLocation)
        self.txtBrowserLocation.pack(side="left", fill=tk.X, expand=True)
        self.btnDefaultBrowser = tk.Button(self.frmBrowserLocation, text="...", command = self.onbtnDefaultBrowserClick)
        self.btnDefaultBrowser.pack(side="left")
        self.btnTryFind = tk.Button(self.frmBrowserLocation,text="Try to Find it...")
        self.btnTryFind.pack(side="left")
        self.frmBrowserLocation.pack(fill=tk.X, ipadx=2, ipady=2)

    def OncbDefaulBrowserSelected(self, event):
        print( event.widget.get())
    
    def onbtnDefaultBrowserClick(self):
        print(tk.filedialog.askopenfile(initialdir = "/",title = "Select file",filetypes = (("executable files","*.exe"),("all files","*.*"))))

if __name__ == "__main__":
    root = tk.Tk()
    frmOptions(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
