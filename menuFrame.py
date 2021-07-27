import tkinter as tk
import main

class MenuFrame(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 360
		self.bgcolor = 'darkgreen'
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)
		self.setController(controller)
		self.menuindex = tk.IntVar()
		self.menuindex.set(1)
		self.menulength = 3

		self.canvas = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		self.canvas.pack()

		self.paint()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def getController(self):
		return self.controller

	def setController(self, con):
		self.controller = con

	def repaint(self, event = None):
		self.canvas.delete('all')
		self.paint()

	def keyPressed(self, event):
		key = event.keysym
		
		if key == 'Return':
			if self.menuindex.get() == 1:
				main.show_frame('ゲームフレーム')
			elif self.menuindex.get() == 2:
				main.show_frame('設定フレーム')
			elif self.menuindex.get() == 3:
				self.getController().quit()
		elif key == 'Up':
			self.menuindex.set(self.menuindex.get() - 1)
		elif key == 'Down':
			self.menuindex.set(self.menuindex.get() + 1)

		if self.menuindex.get() == 0:
			self.menuindex.set(self.menulength)
		if self.menuindex.get() > self.menulength:
			self.menuindex.set(1)

	def mouseEnter(self, event):
		tag = event.widget.gettags('current')[0]

		if tag in ['start', 'startrect', 'setting', 'settingrect', 'quit', 'quitrect']:

			for wid in ['startselected', 'settingselected', 'quitselected']:
				event.widget.itemconfig(wid, fill = self.bgcolor)

			if tag in ['start', 'startrect']:
				self.menuindex.set(1)
				event.widget.itemconfig('startselected', fill = 'red')
			elif tag in ['setting', 'settingrect']:
				self.menuindex.set(2)
				event.widget.itemconfig('settingselected', fill = 'red')
			elif tag in ['quit', 'quitrect']:
				self.menuindex.set(3)
				event.widget.itemconfig('quitselected', fill = 'red')

	def mousePressed(self, event):
		tag = event.widget.gettags('current')[0]

		if tag == 'start':
			main.show_frame('ゲームフレーム')
		elif tag == 'setting':
			main.show_frame('設定フレーム')
		elif tag == 'quit':
			self.getController().quit()

	def paint(self):
		self.canvas.create_text(320, 50, fill = 'white', text = 'Menu', font = ('Times New Roman', 36, 'italic'))

		self.canvas.create_rectangle(220, 115, 415, 155, fill = self.bgcolor, width = 0, tags = 'startrect')
		self.canvas.create_text(320, 130, fill = 'white', text = 'game start', font = ('Times New Roman', 40, 'italic'), tags = 'start')

		self.canvas.create_rectangle(250, 185, 385, 225, fill = self.bgcolor, width = 0, tags = 'settingrect')
		self.canvas.create_text(320, 200, fill = 'white', text = 'settings', font = ('Times New Roman', 40, 'italic'), tags = 'setting')

		self.canvas.create_rectangle(270, 255, 365, 295, fill = self.bgcolor, width = 0, tags = 'quitrect')
		self.canvas.create_text(320, 270, fill = 'white', text = 'quit', font = ('Times New Roman', 40, 'italic'), tags = 'quit')

		# スタートメニュー選択時
		self.canvas.create_text(210, 135, fill = 'red' if self.menuindex.get() == 1 else self.bgcolor, text = '>', font = ('arial', 40, 'bold'), tags = 'startselected')
		self.canvas.create_text(425, 135, fill = 'red' if self.menuindex.get() == 1 else self.bgcolor, text = '<', font = ('arial', 40, 'bold'), tags = 'startselected')

		# 設定メニュー選択時
		self.canvas.create_text(240, 205, fill = 'red' if self.menuindex.get() == 2 else self.bgcolor, text = '>', font = ('arial', 40, 'bold'), tags = 'settingselected')
		self.canvas.create_text(395, 205, fill = 'red' if self.menuindex.get() == 2 else self.bgcolor, text = '<', font = ('arial', 40, 'bold'), tags = 'settingselected')

		# 終了メニュー選択時
		self.canvas.create_text(260, 275, fill = 'red' if self.menuindex.get() == 3 else self.bgcolor, text = '>', font = ('arial', 40, 'bold'), tags = 'quitselected')
		self.canvas.create_text(375, 275, fill = 'red' if self.menuindex.get() == 3 else self.bgcolor, text = '<', font = ('arial', 40, 'bold'), tags = 'quitselected')

		# マウスイベントを設定
		self.canvas.tag_bind('current', '<Enter>', self.mouseEnter)
		self.canvas.tag_bind('current', '<ButtonPress-1>', self.mousePressed)