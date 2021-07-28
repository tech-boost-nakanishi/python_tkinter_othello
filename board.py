from decimal import Decimal, ROUND_HALF_UP

class Board():
	def __init__(self, blength, gfwidth):
		self.blength = blength
		self.gfwidth = gfwidth
		self.masuwidth = self.masuheight = int(Decimal(str(self.gfwidth / self.blength)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

	def getX(self, mx):
		for i in range(self.blength):
			if mx >= i * self.masuwidth and mx <= i * self.masuwidth + self.masuwidth:
				return i

	def getY(self, my):
		for i in range(self.blength):
			if my >= i * self.masuheight and my <= i * self.masuheight + self.masuheight:
				return i

	def drawBoard(self, canvas):
		# ボード背景
		canvas.create_rectangle(0, 0, self.gfwidth, self.gfwidth, fill = 'darkgreen')

		## 境界線
		linecolor = 'black'
		# 横線
		for i in range(self.blength):
			canvas.create_line(0, (i + 1) * self.masuheight, self.gfwidth, (i + 1) * self.masuheight, fill = linecolor, width = 2)

		# 縦線
		for i in range(self.blength):
			canvas.create_line((i + 1) * self.masuwidth, 0, (i + 1) * self.masuwidth, self.gfwidth, fill = linecolor, width = 2)