import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sip
import textwrap

class Gui(QMainWindow):
	def __init__(self):
		super(Gui,self).__init__()
		self.global_attributes()
#Settings for the main window(QWidget) widget
		self.setWindowTitle("GUI #2")
		self.setGeometry(250,250,1900,700)
		self.setCentralWidget(self.frame)
#-----------------------------------------------------
#Function calls to layout definitions
		self.h_layout_top()
		self.h_layout_bottom()
		self.v_layout()
#-----------------------------------------------------
#Initialization of widgets ti be used by class object
	def global_attributes(self):
		self.exit_btn = QPushButton()
		self.exit_btn.setText("EXIT")
		self.exit_btn.setStyleSheet("color:teal;background:red")
		self.exit_btn.clicked.connect(sys.exit)

		self.animal_file_seeker = 0
		self.yo_mamma_file_seeker = 0
		self.blonde_file_seeker = 0
		self.dirty_file_seeker = 0
		self.bluecollar_file_seeker = 0

		self.t_pixmap = QPixmap("t-brain.jpg")
		self.t_brain_pic = QLabel()
		self.t_brain_pic.setPixmap(self.t_pixmap)

		self.h_t_brain = QHBoxLayout()
		

		self.greeting = QLabel()
		self.greeting_hLayout = QHBoxLayout()
		self.greeting.setStyleSheet('''
					color:white;
					font-family:proggy;
					font-size:50px;
					font-weight:50
					''')
		self.h_t_brain.insertWidget(1,self.greeting)

		self.frame = QFrame(self)
		self.frame.setObjectName("mainframe")
		self.frame.setStyleSheet("QWidget#mainframe {border-image:url(t-brain.jpg)}")
		self.count = 0;
#----------------------------------------------------
#Defines the top layer of main gui widget
	def h_layout_top(self):
		self.h_box_top = QHBoxLayout()
		self.main_label = QLabel()
		self.main_label.setText("T-Brain")
		self.main_label.setStyleSheet('''
			font-family: monospace;
			font-weight:bold;
			font-size:100px;
			color:red
			''')
		self.h_box_top.addStretch()
		self.h_box_top.addWidget(self.main_label)
		self.h_box_top.addStretch()
#------------------------------------------------------
#Defines the bottom layer for main gui widget
	def h_layout_bottom(self):
		self.h_box_bottom = QHBoxLayout()
		self.btn = QPushButton()
		self.btn.setText("LET'S TALK")
		self.btn.setStyleSheet("background:red")
		self.btn.clicked.connect(self.generate_window)
		self.h_box_bottom.addWidget(self.btn)
#------------------------------------------------------
#Defines the vertical layer in which all horizontal layers are added to
	def v_layout(self):
		self.v_box = QVBoxLayout()
		self.v_box.addLayout(self.h_box_top)
		self.v_box.addStretch()
		self.v_box.addLayout(self.h_box_bottom)
		self.frame.setLayout(self.v_box)
#-------------------------------------------------------
#Function to generate new app window(Activated by sender button from h_layout_top def )
	def generate_window(self):
#Settings for new window
		self.new_window = QWidget()
		self.new_window.setGeometry(500,250,500,500)
		self.new_window.setStyleSheet("background:teal")
		self.setCentralWidget(self.new_window)
#--------------------------------------------------------------
#Creation of new window layer objects
		self.nw_vLayout = QVBoxLayout()
		self.nw_hLayout = QHBoxLayout()
#--------------------------------------------------------------
#Creation and settings for line Edit objext (Allows user to type)
		self.le = QLineEdit(self.new_window)
		self.le.setStyleSheet("background:skyblue;color:blue")
		self.le.resize(200,25)
		self.le.setPlaceholderText("Enter your name here")
#---------------------------------------------------------------
#Creation of widget buttons to be added to layouts
		#Clear button signals the clear window function
		self.clr_btn = QPushButton(self.new_window)
		self.clr_btn.setText("clear")
		self.clr_btn.setStyleSheet("background:silver")
		self.clr_btn.clicked.connect(self.le.clear)
		#Print button signals the Activate function
		self.prnt_btn = QPushButton()
		self.prnt_btn.setText("Start")
		self.prnt_btn.setStyleSheet("background:silver")
		self.prnt_btn.clicked.connect(self.activate_convo)
#----------------------------------------------------------------
#Definition of new window layout and positioning of widgets
		self.greeting_hLayout.addStretch()
		self.greeting_hLayout.addWidget(self.greeting)
		self.greeting_hLayout.addStretch()

		self.nw_vLayout.insertLayout(0,self.h_t_brain)
		self.nw_vLayout.addStretch()
		self.nw_vLayout.addWidget(self.le)
		self.nw_hLayout.addStretch()
		self.nw_hLayout.addWidget(self.clr_btn)
		self.nw_hLayout.addWidget(self.prnt_btn)
		self.nw_hLayout.addStretch()
		self.nw_vLayout.addLayout(self.nw_hLayout)
		self.nw_vLayout.addStretch()

		self.new_window.setLayout(self.nw_vLayout)
		self.new_window.show()
#------------------------------------------------------------
#Activate function definition
#Uses the number of clicks made on a single button to switch the various slots all connected by one signal(conservative)
#Promotes the recycling of objects.
	def activate_convo(self,new_window):
		self.count += 1
		if self.count == 1:
			self.greeting.setText(("Hello there "+self.le.text()))
			sip.delete(self.le)
			sip.delete(self.clr_btn) 
			self.prnt_btn.setText("Continue")
			self.h_t_brain.insertWidget(0,self.t_brain_pic)
		if self.count == 2:
			self.prnt_btn.setText("Continue")
			string = "I am T-Brain, pleased to meet you"
			format_str = textwrap.fill(string,20)
			self.greeting.setText((format_str))
		if self.count == 3:
			self.greeting.setText("Wanna hear some jokes?")
			sip.delete(self.prnt_btn)
			self.add_yes_no()
		if self.count == 4:
			self.sender = self.sender()
			if self.sender.text() == "YES":
				sip.delete(self.h_yes_no)
				sip.delete(self.yes_btn)
				sip.delete(self.no_btn)
				sip.delete(self.or_label)
				string="Awesome, I just happen to have tons in my arsenal.\nWhat kind of jokes do you like?"
				format_str = textwrap.fill(string,15)
				self.greeting.setText(format_str)
				self.jokes_menu()
			elif self.sender.text() == "NO":
				sip.delete(self.h_yes_no)
				sip.delete(self.yes_btn)
				sip.delete(self.no_btn)
				sip.delete(self.or_label)
				self.h_exit = QHBoxLayout()
				self.h_exit.insertStretch(0)
				self.h_exit.insertWidget(1,self.exit_btn)
				self.h_exit.insertStretch(2)
				self.nw_vLayout.addLayout(self.h_exit)
				self.nw_vLayout.addStretch()
				string="OK no problem, come back anytime :D"
				format_str = textwrap.fill(string,15)
				self.greeting.setText(format_str)
#Function that adds two buttons and albel to the current window.
#Purpose: capable of changing up the widget layout of the current window instead of creating a whole new window.
	def add_yes_no(self):

		self.yes_btn = QPushButton()
		self.yes_btn.setStyleSheet("background:teal;color:red")
		self.yes_btn.setText("YES")
		self.yes_btn.clicked.connect(self.activate_convo)

		self.no_btn = QPushButton()
		self.no_btn.setStyleSheet("background:teal;color:red")
		self.no_btn.setText("NO")
		self.no_btn.clicked.connect(self.activate_convo)

		self.or_label = QLabel()
		self.or_label.setText("OR")
		self.or_label.setStyleSheet("color:red")
		
		self.h_yes_no = QHBoxLayout()
		self.h_yes_no.addStretch()
		self.h_yes_no.addWidget(self.yes_btn)
		self.h_yes_no.addStretch()
		self.h_yes_no.addWidget(self.or_label)
		self.h_yes_no.addStretch()
		self.h_yes_no.addWidget(self.no_btn)
		self.h_yes_no.addStretch()

		self.nw_vLayout.insertStretch(2)
		self.nw_vLayout.insertLayout(3,self.h_yes_no)
#This function creates a list of buttons that allows the user to choose a joke category
	def jokes_menu(self):
		self.animal_btn = QPushButton()
		self.animal_btn.setText("ANIMAL")
		self.animal_btn.setStyleSheet("background:teal;color:red")
		self.animal_btn.clicked.connect(lambda:self.scan_files(self.animal_btn))

		self.yo_mamma_btn = QPushButton()
		self.yo_mamma_btn.setText("YO MAMMA")
		self.yo_mamma_btn.setStyleSheet("background:teal;color:red")
		self.yo_mamma_btn.clicked.connect(lambda:self.scan_files(self.yo_mamma_btn))

		self.blonde_btn = QPushButton()
		self.blonde_btn.setText("BLONDE")
		self.blonde_btn.setStyleSheet("background:teal;color:red")
		self.blonde_btn.clicked.connect(lambda:self.scan_files(self.blonde_btn))

		self.dirty_btn = QPushButton()
		self.dirty_btn.setText("DIRTY")
		self.dirty_btn.setStyleSheet("background:teal;color:red")
		self.dirty_btn.clicked.connect(lambda:self.scan_files(self.dirty_btn))				

		self.bluecollar_btn = QPushButton()
		self.bluecollar_btn.setText("BLUE COLLAR")
		self.bluecollar_btn.setStyleSheet("background:teal;color:red")
		self.bluecollar_btn.clicked.connect(lambda:self.scan_files(self.bluecollar_btn))

		self.h_exit = QHBoxLayout()
		self.h_exit.insertStretch(0)
		self.h_exit.insertWidget(1,self.exit_btn)
		self.h_exit.insertStretch(2)

		self.h_animal = QHBoxLayout()
		self.h_animal.addStretch()
		self.h_animal.addWidget(self.animal_btn)
		self.h_animal.addStretch()

		self.h_yo_mamma = QHBoxLayout()
		self.h_yo_mamma.addStretch()
		self.h_yo_mamma.addWidget(self.yo_mamma_btn)
		self.h_yo_mamma.addStretch()

		self.h_blonde = QHBoxLayout()
		self.h_blonde.addStretch()
		self.h_blonde.addWidget(self.blonde_btn)
		self.h_blonde.addStretch()

		self.h_dirty = QHBoxLayout()
		self.h_dirty.addStretch()
		self.h_dirty.addWidget(self.dirty_btn)
		self.h_dirty.addStretch()

		self.h_blue_collar = QHBoxLayout()
		self.h_blue_collar.addStretch()
		self.h_blue_collar.addWidget(self.bluecollar_btn)
		self.h_blue_collar.addStretch()

		self.nw_vLayout.insertStretch(2)
		self.nw_vLayout.insertLayout(3,self.h_animal)
		self.nw_vLayout.insertLayout(4,self.h_yo_mamma)
		self.nw_vLayout.insertLayout(5,self.h_blonde)
		self.nw_vLayout.insertLayout(6,self.h_dirty)
		self.nw_vLayout.insertLayout(7,self.h_blue_collar)
		self.nw_vLayout.insertLayout(8,self.h_exit)

#This function deals with the file processing which is signaled by each button that was created in the previous section
	def scan_files(self,btn):
		if btn.text() == "ANIMAL":
			self.greeting.setStyleSheet("border:5px solid pink;background:pink;color:teal;font-size:30px")
			with open("animal.txt","r") as rf:
				self.joke = ""
				rf.seek(self.animal_file_seeker)
				for x in  range(2):
					self.joke += rf.readline()
					if self.joke == "":
						self.end_text = "Whoops thats it for animal jokes hope you laughed alot."
						self.format_end_text = textwrap.fill(self.end_text,25)
						self.greeting.setText(self.format_end_text)
						return
			self.format_jk = textwrap.fill(self.joke,25)
			self.greeting.setText(self.format_jk)
			self.animal_file_seeker += len(self.joke)

		if btn.text() == "YO MAMMA":
			self.greeting.setStyleSheet("border:5px solid pink;background:pink;color:teal;font-size:30px")
			with open("yo_mamma.txt","r") as rf:
				self.joke = ""
				rf.seek(self.yo_mamma_file_seeker)
				for x in range(2):
					self.joke += rf.readline()
					if self.joke == "":
						self.end_text = "Whoops thats it for Yo Mamma jokes hope you laughed alot."
						self.format_end_text = textwrap.fill(self.end_text.center(30,'-'),25)
						self.greeting.setText(self.format_end_text)
						return
			self.format_jk = textwrap.fill(self.joke,25)
			self.greeting.setText(self.format_jk)
			self.yo_mamma_file_seeker += len(self.joke)

		if btn.text() == "DIRTY":
			self.greeting.setStyleSheet("border:5px solid pink;background:pink;color:teal;font-size:30px")
			with open("dirty.txt","r") as rf:
				self.joke = ""
				rf.seek(self.dirty_file_seeker)
				for x in range(2):
					self.joke += rf.readline()
					if self.joke == "":
						self.end_text = "Whoops thats it for DIRTY jokes hope you laughed alot."
						self.format_end_text = textwrap.fill(self.end_text,25)
						self.greeting.setText(self.format_end_text)
						return
			self.format_jk = textwrap.fill(self.joke,25)
			self.greeting.setText(self.format_jk)
			self.dirty_file_seeker += len(self.joke)

		if btn.text() == "BLONDE":
			self.greeting.setStyleSheet("border:5px solid pink;background:pink;color:teal;font-size:30px")
			with open("blonde.txt","r") as rf:
				self.joke = ""
				rf.seek(self.blonde_file_seeker)
				for x in range(2):
					self.joke += rf.readline()
					if self.joke == "":
						self.end_text = "Whoops thats it for BLONDE jokes hope you laughed alot."
						self.format_end_text = textwrap.fill(self.end_text,30)
						self.greeting.setText(self.format_end_text)
						return
			self.format_jk = textwrap.fill(self.joke,20)
			self.greeting.setText(self.format_jk)
			self.blonde_file_seeker += len(self.joke)

		if btn.text() == "BLUE COLLAR":
			self.greeting.setStyleSheet("border:5px solid pink;background:pink;color:teal;font-size:30px")
			with open("bluecollar.txt","r") as rf:
				self.joke = ""
				rf.seek(self.bluecollar_file_seeker)
				for x in range(2):
					self.joke += rf.readline()
					if self.joke == "":
						self.end_text = "Whoops thats it for BLUE COLLAR jokes hope you laughed alot."
						self.format_end_text = textwrap.fill(self.end_text,30)
						self.greeting.setText(self.format_end_text)
						return
			self.format_jk = textwrap.fill(self.joke,20)
			self.greeting.setText(self.format_jk.center(22))
			self.bluecollar_file_seeker += len(self.joke)
#End of GUI class-------------------------------------------------
#Initialization of overall app and gui class creates above
app = QApplication(sys.argv)
myapp = Gui()
myapp.showMaximized()
sys.exit(app.exec_())	
