import tkinter as tk
import main

class MenuFrame(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 360
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)
		self.setController(controller)

		tk.Label(self, text = 'メニューフレーム').pack()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def getController(self):
		return self.controller

	def setController(self, con):
		self.controller = con