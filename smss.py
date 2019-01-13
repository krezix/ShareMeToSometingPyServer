from bottle import route, run, get, post
import tkinter as tk
import threading

class Gui: 
    def __init__(self, parent):        
        self.parent = parent     
        parent.title ( "Share Me To Something Server"   )
        self.label = tk.Label(parent, text="Main window label")
        self.label.grid(row=0, column=0)
        #self.window = Frame1(self)
        #self.window.grid(row=0, column=10, rowspan=2)
        self.label.pack()

if __name__=="__main__":
    root = tk.Tk()
    my_gui = Gui(root)
    root.mainloop()
'''
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent        
        self.title('Share Me To Something Server')
        self.lbl = tk.Label(win, text = 'IP : ')
        self.pack()
        self.win.mainloop()

@route('/')
def index():
    return 'No Commands sent ...'

@get('/openurl')
def get_openurl():
    return 'get open url'

@post('/openurl')
def post_openurl():
    return '200'

run(host='localhost',port=8080,debug=True)

'''
