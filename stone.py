from decimal import Decimal, ROUND_HALF_UP

class Stone():
	def __init__(self, canvas, blength, gfwidth, defaultvalue):
		self.canvas = canvas
		self.blength = blength
		self.gfwidth = gfwidth
		self.defaultvalue = defaultvalue
		self.masuwidth = self.masuheight = int(Decimal(str(self.gfwidth / self.blength)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

		# ストーンリストの初期化
		self.stones = [[self.defaultvalue]*self.blength for i in range(self.blength)]

	def getStone(self, x, y):
		return self.stones[x][y]

	def setStone(self, x, y, state):
		self.stones[x][y] = state

	def getCountStones(self, state):
		count = 0

		for cy in range(len(self.stones)):
			for cx in range(len(self.stones[cy])):
				if self.getStone(cx, cy) == state:
					count += 1

		return count

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
		