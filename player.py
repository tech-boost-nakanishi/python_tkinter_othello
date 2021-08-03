import main

class Player():
	def __init__(self):
		# 8方向用リスト
		self.direction = [
			[0, -1],
			[0, 1],
			[1, 0],
			[-1, 0],
			[1, -1],
			[1, 1],
			[-1, -1],
			[-1, 1],
		]

	def PutStone(self, stonesList, x, y, blank, myself, opponent, mode):
		count = dx = dy = 0

		for i in range(len(self.direction)):
			dx, dy = x, y
			flipstones = []

			while True:
				dx += self.direction[i][0]
				dy += self.direction[i][1]

				if dx < 0 or dy < 0 or dx >= len(stonesList) or dy >= len(stonesList):
					break

				if stonesList[dx][dy] == blank:
					break

				if stonesList[dx][dy] == myself:
					count += len(flipstones)
					if mode == 'change':
						stonesList[x][y] = myself
						if len(flipstones) > 0:
							# ストーンをひっくり返す
							for i in range(len(flipstones)):
								stonesList[flipstones[i][0]][flipstones[i][1]] = myself
					break

				if stonesList[dx][dy] == opponent:
					flipstones.append([dx, dy])

		return count, stonesList

	def CanPutStone(self, stonesList, blank, myself, opponent):
		count = 0

		for y in range(len(stonesList)):
			for x in range(len(stonesList[y])):
				if stonesList[x][y] == blank:
					if self.PutStone(stonesList, x, y, blank, myself, opponent, 'check')[0] > 0:
						count += 1

		if count > 0:
			return True, stonesList

		return False, stonesList