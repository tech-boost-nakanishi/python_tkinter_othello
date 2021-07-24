import tkinter as tk
import main

class SettingFrame(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 360
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)

		tk.Label(self, text = '設定フレーム').pack()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT