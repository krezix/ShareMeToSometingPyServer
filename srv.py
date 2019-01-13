from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import tkinter as tk
from myText import myText

# https://github.com/eduvpn/python-eduvpn-client/blob/master/eduvpn/oauth2.py
class ServerThread (threading.Thread):
    class RequestHandler(BaseHTTPRequestHandler):
        def response(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

        routes = {
            '/openurl'
        }    
        def do_openurlfrm(self):
            frm ="""
<form method='POST' action='/openurl'>
URL TO Open : <input type='text' name='url'>
<input type='submit'>
</form>
            """
            return frm

        def do_GET(self):

            print ("PAth : ", str(self.path))
            print ("headers : ", str(self.headers))
            #print("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            self.wfile.write(self.do_openurlfrm().encode('utf-8'))

        def write(self,data):
            self.wfile.write(data.encode('utf-8'));
        def do_POST(self):
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself
            self.mylogger.add_text(post_data)
            '''logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
'''
            self.response()
            self.write(str(post_data))
        
    def __init__(self,port,mylogger):
      threading.Thread.__init__(self)
      self.mylogger = mylogger     
      self.stopServer = False
      self.exitApp = False
      self.port = port
      self.start_server()
    
    def close_server(self):
        self.mylogger.add_bolded ('Stopping Server..')
        self.stopServer = True
        self.httpd.server_close()
    
    def close_app(self):
        self.close_server()
        self.exitApp = True
    
    def start_server(self):
        self.mylogger.add_bolded('Starting Server...')
        self.httpd = HTTPServer(('', self.port), self.RequestHandler)
        self.stopServer = False

    def run(self):
        while not self.exitApp : 
            while not self.stopServer:
                self.httpd.handle_request() 

class Gui: 
    def __init__(self, parent,port):        
        self.parent = parent     
        parent.title ( "Share Me To Something Server"   )
        #self.label = tk.Label(parent, text="Main window label")
        #self.label.grid(row=0, column=0)
        self.frmToolbar = tk.Frame (parent)  
        self.btnStartStop = tk.Button(self.frmToolbar,text ='Stop Server', command = self.StartServer)
        
        self.frmContent = tk.Frame(parent)
        self.txtLogger =myText(self.frmContent)
        #self.scroll = tk.Scrollbar(parent, command=self.txtLogger.yview)
        #self.txtLogger.configure(yscrollcommand=self.scroll.set)
        #self.window = Frame1(self)
        #self.window.grid(row=0, column=10, rowspan=2)
        #self.label.pack()
        self.frmToolbar.pack(side=tk.TOP,fill=tk.X)
        self.btnStartStop.pack(side=tk.LEFT)

        #self.txtLogger.pack(fill=tk.BOTH, expand=1)
        self.frmContent.pack(fill=tk.BOTH, expand=1)

        self.serverThread = ServerThread(port, self.txtLogger)
        self.serverThread.start()

        parent.protocol("WM_DELETE_WINDOW", self.on_closing)
#TODO :
#criar funcao para adicionar texto formatado
    def on_closing(self):
        self.serverThread.close_app()
        self.parent.destroy()


    def StartServer(self):
        if (self.btnStartStop.cget('text') == 'Start Server'):
            self.serverThread.start_server()
            #self.serverThread.stopServer = False
            self.btnStartStop.config(text='Stop Server')
        else:
            self.serverThread.close_server()
            self.btnStartStop.config(text='Start Server')



if __name__ == '__main__':
    #t1 = ServerThread(2345)
    #t1.start()
    root = tk.Tk()
    my_gui = Gui(root,2345)
    root.mainloop()

#def print_time(threadName, delay, counter):
#   while counter:
#      time.sleep(delay)
#      print ("%s: %s" % (threadName, time.ctime(time.time())))
#      counter -= 1

#def one_request(port, lets_connect, timeout=None):
#    """
#    Listen for one http request on port, then close and return request query
#    args:
#        port (int): the port to listen for the request
#    returns:
#        str: the request
#    """
#    logger.info("listening for a request on port {}...".format(port))

#    class RequestHandler(BaseHTTPRequestHandler):
#        def do_GET(self):
#            self.send_response(200)
#            self.send_header("Content-type", "text/html")
#            self.end_headers()

#            logo, name = get_brand(lets_connect)
#            logo = stringify_image(logo)
#            content = landing_page.format(logo=logo, brand=name).encode('utf-8')
#            self.wfile.write(content)
#            self.server.path = self.path

#    httpd = HTTPServer(('', port), RequestHandler)
#    if timeout:
#        httpd.socket.settimeout(timeout)
#    httpd.handle_request()
#    httpd.server_close()

#    if not hasattr(httpd, "path"):
#        raise Exception("Invalid response received")

#    parsed = urlparse(httpd.path)
#    logger.info("received a request {}".format(httpd.path))
#    return parse_qs(parsed.query)