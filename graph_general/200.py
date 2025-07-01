"""Leetcode 200 Iland""" 

[
	[1, 1, 1, 0, 0],
	[0, 0, 1, 1, 1],
	[0, 0, 0, 0, 0],
	[1, 0, 0, 0, 1],
	[1, 0, 1, 1, 1],
]


def number_of_land(land):
	visited = [[0] * len(land[0]) for _ in range(len(land))]
	land_counter = 0
	def dfs(x, y):
		if not (0 < x < len(land)) and not (0 < y < len(land[0])):
			return  
		if land[x][y] == 0 or visited[x][y] ==1:
			return 

		visited[x][y] = 1
		dfs(x - 1, y )
		dfs(x + 1, y)
		dfs(x, y - 1)
		dfs(x, y + 1)


	for i in range(len(land)):
		for j in range (len(land[0])):
			if land[i][j] == 1 and visited[i][j] == 0:
				land_count += 1 			
				dfs(i, j)
	return land_counter