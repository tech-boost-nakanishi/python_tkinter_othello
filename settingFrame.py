import tkinter as tk
import main
import sqlite3
from tkinter import messagebox

class SettingFrame(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 360
		self.bgcolor = 'forestgreen'
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		self.pack_propagate(0)

		tk.Label(self, text = 'Settings', fg = 'white', bg = self.bgcolor, font = ('Times New Roman', 36, 'italic')).place(x = 50, y = 25)

		# 色選択ラベルフレーム
		self.bw_frame = tk.LabelFrame(self, width=self.WIDTH - 90, height=80, text='色', font=('Arial', 20, 'bold'), bg = self.bgcolor, bd = 3, fg = 'white')
		self.bw_frame.place(x = 45, y = 90)
		self.bw_frame.pack_propagate(0)
		self.colorvalue = tk.StringVar()
		self.colorvalue.set(self.getBORWVALUE())
		self.wradio = tk.Radiobutton(self.bw_frame, value="w", variable=self.colorvalue, text='白', font=('Arial', 28, 'bold'), bg = self.bgcolor, fg = 'white')
		self.wradio.place(x = 110, y = 5)
		self.bradio = tk.Radiobutton(self.bw_frame, value="b", variable=self.colorvalue, text='黒', font=('Arial', 28, 'bold'), bg = self.bgcolor)
		self.bradio.place(x = 260, y = 5)

		# 先攻後攻選択ラベルフレーム
		self.attack_frame = tk.LabelFrame(self, width=self.WIDTH - 90, height=80, text='順番', font=('Arial', 20, 'bold'), bg = self.bgcolor, bd = 3, fg = 'white')
		self.attack_frame.place(x = 45, y = 190)
		self.attack_frame.pack_propagate(0)
		self.attackvalue = tk.IntVar()
		self.attackvalue.set(self.getATTACKVALUE())
		self.fradio = tk.Radiobutton(self.attack_frame, value=0, variable=self.attackvalue, text='先攻', font=('Arial', 28, 'bold'), bg = self.bgcolor)
		self.fradio.place(x = 110, y = 5)
		self.sradio = tk.Radiobutton(self.attack_frame, value=1, variable=self.attackvalue, text='後攻', font=('Arial', 28, 'bold'), bg = self.bgcolor)
		self.sradio.place(x = 260, y = 5)

		# 変更ボタン
		tk.Button(self, text = '変　更', bg = self.bgcolor, highlightbackground = self.bgcolor, command = self.changeSettings).place(x = 290, y = 300)

		# メニュー画面遷移ボタン
		tk.Button(self, text = 'メニュー画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, command = lambda: main.show_frame('メニューフレーム')).place(x = 300, y = 40)

		# ゲーム画面遷移ボタン
		tk.Button(self, text = 'ゲーム開始', bg = self.bgcolor, highlightbackground = self.bgcolor, command = lambda: main.show_frame('ゲームフレーム')).place(x = 425, y = 40)

		# 終了ボタン
		tk.Button(self, text = '閉じる', bg = self.bgcolor, highlightbackground = self.bgcolor, command = controller.destroy).place(x = 525, y = 40)

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def getBORWVALUE(self):
		conn = sqlite3.connect('setting.db')
		cur = conn.cursor()
		result = cur.execute('SELECT color FROM settings WHERE id = 1').fetchone()
		cur.close()
		conn.close()
		return result[0]

	def getATTACKVALUE(self):
		conn = sqlite3.connect('setting.db')
		cur = conn.cursor()
		result = cur.execute('SELECT attack FROM settings WHERE id = 1').fetchone()
		cur.close()
		conn.close()
		return result[0]

	def changeSettings(self):
		conn = sqlite3.connect('setting.db')
		cur = conn.cursor()
		cur.execute('UPDATE settings SET color = "{}", attack = {} WHERE id = 1'.format(self.colorvalue.get(), self.attackvalue.get()))
		conn.commit()
		cur.close()
		conn.close()

		if messagebox.showinfo('メッセージ', '設定を変更しました。') == 'ok':
			self.colorvalue.set(self.getBORWVALUE())
			self.attackvalue.set(self.getATTACKVALUE())