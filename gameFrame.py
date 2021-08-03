import tkinter as tk
import main
from decimal import Decimal, ROUND_HALF_UP
from tkinter import messagebox
import time
import random
import threading

class GameFrame(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 720
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)
		self.bgcolor = 'lightgray'
		self.masucount = 8
		self.masuwidth = self.masuheight = int(Decimal(str(self.WIDTH / self.masucount)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
		self.BLANK = 0
		self.USER = 1
		self.COMPUTER = 2
		self.turnnum = tk.IntVar()
		self.failedcount = tk.IntVar()
		self.failedcount.set(0)
		self.isPut = False
		self.playerCanPut = False
		self.playerstones = []
		self.playercount = 0
		global mx, my
		self.mx = self.my = -1

		self.canvas = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		self.canvas.pack()

		# ボタン群
		tk.Button(self, text = '最初から', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('ゲームフレーム')).place(x = 10, y = 650)
		tk.Button(self, text = '終了', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = controller.destroy).place(x = 10, y = 680)
		tk.Button(self, text = 'メニュー画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('メニューフレーム')).place(x = 120, y = 650)
		tk.Button(self, text = '設定画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('設定フレーム')).place(x = 120, y = 680)

		# ボードクラスのインスタンス生成
		import board
		self.boardobj = board.Board(self.masucount, self.WIDTH, self.masuwidth, self.masuheight)

		# ストーンリスト初期化
		self.stones = [[self.BLANK]*self.masucount for i in range(self.masucount)]

		# ランダムに最初の位置を設定
		startrand = random.randint(1, 2)
		if startrand == 1:
			self.stones[3][3] = self.USER
			self.stones[4][3] = self.COMPUTER
			self.stones[3][4] = self.COMPUTER
			self.stones[4][4] = self.USER
		else:
			self.stones[3][3] = self.COMPUTER
			self.stones[4][3] = self.USER
			self.stones[3][4] = self.USER
			self.stones[4][4] = self.COMPUTER

		# プレーヤークラスのインスタンス生成
		import player
		self.playerobj = player.Player()

		# 設定クラスのインスタンス生成
		import settingFrame
		settingframe = settingFrame.SettingFrame(main.container, main.root)
		self.attackvalue = settingframe.getATTACKVALUE()
		self.borwvalue = settingframe.getBORWVALUE()
		if self.attackvalue == 0:
			self.turnnum.set(self.USER)
		else:
			self.turnnum.set(self.COMPUTER)

		self.paint()

		self.thread1 = threading.Thread(target=self.start)
		self.thread1.setDaemon(True)
		self.thread1.start()

	def start(self):
		while True:
			# ユーザーのターン
			if self.turnnum.get() == self.USER:
				self.playerCanPut, self.playerstones = self.playerobj.CanPutStone(self.stones, self.BLANK, self.USER, self.COMPUTER)
				if self.playerCanPut == True:
					self.failedcount.set(0)
					while True:
						if self.isPut == True:
							break
					self.isPut = False
				else:
					self.failedcount.set(self.failedcount.get() + 1)

				self.turnnum.set(self.COMPUTER)

			# コンピューターのターン
			elif self.turnnum.get() == self.COMPUTER:
				self.playerCanPut, self.playerstones = self.playerobj.CanPutStone(self.stones, self.BLANK, self.COMPUTER, self.USER)
				if self.playerCanPut == True:
					self.failedcount.set(0)
					self.computerRandom()
				else:
					self.failedcount.set(self.failedcount.get() + 1)

				self.turnnum.set(self.USER)

			# 再描画
			self.repaint()

			if self.failedcount.get() == 2:
				usercount = self.getStoneCount(self.USER)
				computercount = self.getStoneCount(self.COMPUTER)

				if usercount > computercount:
					messagebox.showinfo('メッセージ', 'あなたの勝ちです。')

				elif usercount < computercount:
					messagebox.showinfo('メッセージ', 'あなたの負けです。')

				elif usercount == computercount:
					messagebox.showinfo('メッセージ', '引き分けです。')

				break

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def drawBlackStone(self, x, y):
		diff = 6
		xPos = x * self.masuwidth
		yPos = y * self.masuheight

		self.canvas.create_oval(xPos + diff, yPos + diff, xPos + self.masuwidth - diff, yPos + self.masuheight - diff, fill = 'black', outline = 'black')

	def drawWhiteStone(self, x, y):
		diff = 6
		xPos = x * self.masuwidth
		yPos = y * self.masuheight

		self.canvas.create_oval(xPos + diff, yPos + diff, xPos + self.masuwidth - diff, yPos + self.masuheight - diff, fill = 'white', outline = 'white')

	def mousePressed(self, event):
		global mx, my, isPut
		self.mx = event.x
		self.my = event.y

		if self.turnnum.get() == self.USER:
			if self.stones[self.boardobj.getX(self.mx)][self.boardobj.getY(self.my)] == self.BLANK:
				self.playercount, self.playerstones = self.playerobj.PutStone(self.stones, self.boardobj.getX(self.mx), self.boardobj.getY(self.my), self.BLANK, self.USER, self.COMPUTER, 'check')
				if self.playercount > 0:
					self.playercount, self.playerstones = self.playerobj.PutStone(self.stones, self.boardobj.getX(self.mx), self.boardobj.getY(self.my), self.BLANK, self.USER, self.COMPUTER, 'change')
					self.stones = self.playerstones
					self.isPut = True

	def repaint(self, event = None):
		global mx, my
		self.mx = self.my = -1
		self.canvas.delete('turntext')
		self.canvas.delete('playercounttext')
		# どちらのターンか表示
		turnstr = ''
		if self.turnnum.get() == self.USER:
			turnstr = 'あなたの番です'
		else:
			turnstr = 'コンピューターの番です'
		self.canvas.create_text(400, 695, fill = 'black', text = turnstr, font = ('Arial', 20), tags = 'turntext')

		# それぞれのストーンの数を表示
		self.canvas.create_text(300, 665, fill = 'black', text = 'あなた:', font = ('Arial', 20), tags = 'playercounttext')
		self.canvas.create_text(350, 665, fill = 'black', text = self.getStoneCount(self.USER), font = ('Arial', 20), tags = 'playercounttext')

		self.canvas.create_text(480, 665, fill = 'black', text = 'コンピューター:', font = ('Arial', 20), tags = 'playercounttext')
		self.canvas.create_text(570, 665, fill = 'black', text = self.getStoneCount(self.COMPUTER), font = ('Arial', 20), tags = 'playercounttext')

		# マークの表示
		for cy in range(len(self.stones)):
			for cx in range(len(self.stones[cy])):
				if self.stones[cx][cy] == self.USER:
					if self.borwvalue == "b":
						self.drawBlackStone(cx, cy)
					else:
						self.drawWhiteStone(cx, cy)
				elif self.stones[cx][cy] == self.COMPUTER:
					if self.borwvalue == "b":
						self.drawWhiteStone(cx, cy)
					else:
						self.drawBlackStone(cx, cy)

	def paint(self):
		# ボードを描画
		self.boardobj.drawBoard(self.canvas)

		# マウスイベント
		self.canvas.bind('<Button-1>', self.mousePressed)

		self.repaint()

	def getStoneCount(self, state):
		newlist = []

		for y in self.stones:
			for x in y:
				newlist.append(x)

		return newlist.count(state)

	def computerRandom(self):
		time.sleep(0.5)

		blanklist = []

		for y in range(len(self.stones)):
			for x in range(len(self.stones[y])):
				if self.stones[x][y] == self.BLANK:
					self.playercount, self.playerstones = self.playerobj.PutStone(self.stones, x, y, self.BLANK, self.COMPUTER, self.USER, 'check')
					if self.playercount > 0:
						blanklist.append([x, y])

		self.failedcount.set(0)
		random.shuffle(blanklist)
		self.playercount, self.playerstones = self.playerobj.PutStone(self.stones, blanklist[0][0], blanklist[0][1], self.BLANK, self.COMPUTER, self.USER, 'change')
		self.stones = self.playerstones