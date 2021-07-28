class Player():
	def __init__(self, blength, gfwidth):
		self.blength = blength
		self.gfwidth = gfwidth

		# ストーンクラスのインスタンス生成
		import stone
		self.stoneobj = stone.Stone(self.blength, self.gfwidth)
		