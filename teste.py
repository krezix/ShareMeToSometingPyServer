from tkinter import *

root = Tk()

#text1 = Text(root, height=20, width=30)
##photo=PhotoImage(file='./William_Shakespeare.gif')
#text1.insert(END,'\n')
#text1.image_create(END, image=photo)

#ext1.pack(side=LEFT)

#text2 = Text(root, height=20, width=50)
#scroll = Scrollbar(root, command=text2.yview)
#text2.configure(yscrollcommand=scroll.set)
#text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
#text2.tag_configure('big', font=('Verdana', 20, 'bold'))
#text2.tag_configure('color', foreground='#476042', 
#						font=('Tempus Sans ITC', 12, 'bold'))
#text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
#text2.insert(END,'\nWilliam Shakespeare\n', 'big')

#quote = """
#To be, or not to be that is the question:
#Whether 'tis Nobler in the mind to suffer
#The Slings and Arrows of outrageous Fortune,
#Or to take Arms against a Sea of troubles,
#"""
#text2.insert(END, quote, 'color')
#text2.insert(END, 'follow-up\n', 'follow')
#text2.pack(side=LEFT)
#scroll.pack(side=RIGHT, fill=Y)

#def addNormalText(ctrl , txt):
#	ctrl.insert(END,txt+'\n')

# def addBoldText(ctrl , txt):
# 	ctrl.insert(END,txt+'\n','bold_italics')

# addNormalText(text2,"teste")
# addNormalText(text2,"teste23")

# addBoldText(text2,"teste233")

class myText():
	def __init__(self, root):
		self.root = root
		self.myTxt = Text(self.root)
		self.scroll = Scrollbar(self.root, command=self.myTxt.yview)
		self.myTxt.configure(yscrollcommand=self.scroll.set)
		self.configure_tags()
		self.myTxt.pack(side=LEFT)
		self.scroll.pack(side=RIGHT, fill=Y)

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

txt = myText(root)
txt.add('este e um texto em normal\n')
txt.add_text('este estará deprecado')
txt.add_bolded('texto em negrito')
txt.add('texto com cor\n','color')
txt.add_follow('wtf is this?')

root.mainloop()