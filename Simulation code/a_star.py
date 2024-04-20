from __future__ import print_function
import matplotlib.pyplot as plt
from matplotlib import ticker
from operator import itemgetter
import random
import math


class AStarGraph(object):

	def __init__(self):
		self.barriers = []
		self.grid = [(0, 30), (0, 30)]
		self.goals = [(27, 14, 0, 0), (18, 4, 0, 0), (7, 9, 2, 0)]
		x = []
		for i in range(0, 100):
			a = random.randint(self.grid[0][0], self.grid[0][1])
			b = random.randint(self.grid[1][0], self.grid[1][1])
			x.append((a, b))

		self.barriers.append(x)

	def setGoals(self, goal):
		self.goals = goal

	def findOptimalPath(self, s, g):
		vals = [graph.heuristic(s, x) for x in g]
		for i in range(len(g)):
			lst = list(g[i])
			lst[3] = vals[i]
			g[i] = tuple(lst)
		g.sort(key=itemgetter(2, 3))
		return g

	def heuristic(self, start, goal):
		dx = (start[0] - goal[0]) ** 2
		dy = (start[1] - goal[1]) ** 2
		return math.sqrt((dx + dy))

	def get_vertex_neighbours(self, pos):
		n = []
		# Moves allow link a chess king
		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
			x2 = pos[0] + dx
			y2 = pos[1] + dy
			if x2 < self.grid[0][0] or x2 > self.grid[0][1] or y2 < self.grid[1][0] or y2 > self.grid[1][1]:
				continue
			n.append((x2, y2))
		return n

	def move_cost(self, a, b):
		for barrier in self.barriers:
			if b in barrier:
				return 10000  # Extremely high cost to enter barrier squares
		return 1  # Normal movement cost


def Scheduler(start, goals, graph):
	g = goals
	g = graph.findOptimalPath(start, g)
	bucket = []

	overallCost = 0
	overallPath = []
	goalPath = []
	S = start
	while len(g) > 0:
		goalPath, c = AStarSearch(S, (g[0][0], g[0][1]), graph)
		S = goalPath.pop()
		overallPath.extend(goalPath)
		overallCost += c
		bucket.append(g.pop(0))  # goal has been achieved
		graph.findOptimalPath(S, g)  # Find the next optimal path
	graph.goals = bucket
	overallPath.append(tuple((S)))
	return overallPath, overallCost


def AStarSearch(start, end, graph):
	G = {}  # Actual movement cost to each position from the start position
	F = {}  # Estimated movement cost of start to end going via this position

	# Initialize starting values
	G[start] = 0
	F[start] = graph.heuristic(start, end)

	closedVertices = set()
	openVertices = set([start])
	cameFrom = {}
	p = []
	current = None
	while len(openVertices) > 0:
		# Get the vertex in the open list with the lowest F score
		current = None
		check = current
		currentFscore = None
		for pos in openVertices:
			if current is None or F[pos] < currentFscore:
				if F[pos] is not 10000:  # Obstacles cannot be traversed
					currentFscore = F[pos]
					current = pos

		# Check if we have reached the goal
		if current == end:
			# Retrace our route backward
			path = [current]
			while current in cameFrom:
				current = cameFrom[current]
				path.append(current)
			path.reverse()

			return path, F[end]  # Done!

		# Mark the current vertex as closed
		openVertices.remove(current)
		closedVertices.add(current)

		# Update scores for vertices near the current position
		for neighbour in graph.get_vertex_neighbours(current):
			if graph.move_cost(current, neighbour) == 10000:
				continue
			if neighbour in closedVertices:
				continue  # We have already processed this node exhaustively
			candidateG = G[current] + graph.move_cost(current, neighbour)

			if neighbour not in openVertices:
				openVertices.add(neighbour)  # Discovered a new vertex
			elif candidateG >= G[neighbour]:
				continue  # This G score is worse than previously found

			# Adopt this G score
			cameFrom[neighbour] = current
			G[neighbour] = candidateG
			H = graph.heuristic(neighbour, end)
			F[neighbour] = G[neighbour] + H

	print("A* failed to find a solution")
	p = [current]
	while current in cameFrom:
		current = cameFrom[current]
		p.append(current)
	return p, 0


if __name__ == "__main__":
	Patients = []
	num = input("AMBULANCE NEARBY:")
	for i in range(int(num)):
		print("Location (x,y) of ambulance " + str(i) + " : ")
		a = input("x: ")
		b = input("y: ")
		c = input("Priority (1-10) of ambulance " + str(i) + " : ")
		Patients.append((int(a), int(b), int(c), 0))

	Patients = [(27, 14, 0, 0), (18, 4, 0, 0), (7, 9, 0, 0)]

	graph = AStarGraph()
	graph.setGoals(Patients)

	result, cost = Scheduler((0, 0), Patients, graph)
	print("route", result)
	print("cost", cost)

	fig, ax = plt.subplots(1, 1)
	ax.plot([v[0] for v in result], [v[1] for v in result])
	for barrier in graph.barriers:
		ax.plot([v[0] for v in barrier], [v[1] for v in barrier], 'ro')

	xgoal = []
	ygoal = []

	for i in range(len(result)):
		for j in range(len(graph.goals)):
			if result[i][0] == graph.goals[j][0] and result[i][1] == graph.goals[j][1]:
				xgoal.append(graph.goals[j][0])
				ygoal.append(graph.goals[j][1])

	plt.scatter(xgoal, ygoal, s=90, color="green")
	txt = range(0 + 1, len(xgoal) + 1)
	for i, j in enumerate(txt):
		ax.annotate(j, (xgoal[i], ygoal[i]))

	ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

	plt.xlim(graph.grid[0][0], graph.grid[0][1])
	plt.ylim(graph.grid[1][0], graph.grid[1][1])

	plt.grid(True, which="both")
	plt.show()
