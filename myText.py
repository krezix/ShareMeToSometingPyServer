from tkinter import *
class myText():
	def __init__(self, root):
		self.root = root
		self.myTxt = Text(self.root)
		self.scroll = Scrollbar(self.root, command=self.myTxt.yview)
		self.myTxt.configure(yscrollcommand=self.scroll.set)
		self.configure_tags()
		
		self.scroll.pack(side=RIGHT, fill=Y)
		self.myTxt.pack(fill=BOTH, expand=1)	
	def add_text(self,txt):		
		self.myTxt.insert(END,txt+'\n')
	def add_bolded(self,txt):
		self.myTxt.insert(END,txt+'\n', 'bold')
	def add_follow(self, txt):
		self.myTxt.insert(END,txt+'\n', 'follow')
	
	def add(self,txt,tag='normal'):
		self.myTxt.insert(END,txt, tag)

	def configure_tags(self):
		self.myTxt.tag_configure('normal', font=('Courier New', 10))
		self.myTxt.tag_configure('bold', font=('Courier New', 12, 'bold'))
		self.myTxt.tag_configure('big', font=('Courier New', 20, 'bold'))
		self.myTxt.tag_configure('color', foreground='#280482',	font=('Tempus Sans ITC', 12, 'bold'))
		self.myTxt.tag_bind('follow', '<1>', lambda e, t=self.myTxt: t.insert(END, "Not now, maybe later!"))