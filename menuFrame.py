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

		global canvas
		canvas = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		canvas.pack()

		self.paint()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def getController(self):
		return self.controller

	def setController(self, con):
		self.controller = con

	def paint(self):
		canvas.create_text(320, 50, fill = 'white', text = 'Menu', font = ('Times New Roman', 36, 'italic'))