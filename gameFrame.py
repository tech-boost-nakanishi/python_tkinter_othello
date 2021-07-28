import tkinter as tk
import main

class GameFrame(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 720
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)
		self.bgcolor = 'lightgray'
		self.masucount = 8
		self.BLANK = 0
		self.USER = 1
		self.COMPUTER = 2

		self.canvas = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		self.canvas.pack()

		# ボタン群
		tk.Button(self, text = '最初から', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('ゲームフレーム')).place(x = 10, y = 650)
		tk.Button(self, text = '終了', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = controller.destroy).place(x = 10, y = 680)
		tk.Button(self, text = 'メニュー画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('メニューフレーム')).place(x = 120, y = 650)
		tk.Button(self, text = '設定画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('設定フレーム')).place(x = 120, y = 680)

		# ボードクラスのインスタンス生成
		import board
		self.boardobj = board.Board(self.masucount, self.WIDTH)

		# ストーンクラスのインスタンス生成
		import stone
		self.stoneobj = stone.Stone(self.masucount, self.WIDTH)

		# プレーヤークラスのインスタンス生成
		import player
		self.playerobj = player.Player(self.masucount, self.WIDTH)

		# 設定クラスのインスタンス生成
		import settingFrame
		settingframe = settingFrame.SettingFrame(main.container, main.root)
		self.attackvalue = settingframe.getATTACKVALUE()
		self.borwvalue = settingframe.getBORWVALUE()

		self.paint()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def paint(self):
		# ボードを描画
		self.boardobj.drawBoard(self.canvas)

		self.stoneobj.drawWhiteStone(self.canvas, self.boardobj.getX(100), self.boardobj.getY(100))