class PathFinder:
	def __init__(self, graph, point_count):
		self.graph = graph
		self.max_path = []
		self.max_length = 0
		self.point_status = [0 for i in range(point_count)]
		self.N = len(self.point_status)
		self.max_distance = 10 ** 10


	def path(self, node, distance=0, used_nodes=[]):
		if len(used_nodes) + 1 > self.max_length or (len(used_nodes) + 1 == self.max_length and distance < self.max_distance):
			self.max_length = len(used_nodes) + 1
			self.max_path = used_nodes[::] + [node,]
			self.max_distance = distance
		for i in range(len(self.graph[node])):
			if self.point_status[node] == 0:
				self.path(self.graph[node][i][0], distance + self.graph[node][i][1], used_nodes + [node,])
			else:
				self.path(self.graph[node][i][0], distance + self.graph[node][i][1], used_nodes)


	def delete_nodes(self, nodes):
		for i in nodes:
			self.point_status[i] = 1
			self.graph[i] = []

		for i in self.graph:
			for j in nodes:
				for k in self.graph[i]:
					if k[0] == j:
						del self.graph[i][self.graph[i].index(k)]
						break


	def find_all_paths(self):
		PATHS = []
		graph_size = len(self.graph)
		while graph_size > 0:
			self.max_length = 0
			self.max_path = []
			self.max_distance = 10 ** 10

			roots = []

			for i in range(self.N):
				t = 1
				for j in range(self.N):
					t *= i not in list(map(lambda x:x[0], self.graph[j]))
				if t:
					roots.append(i)

			for i in roots:
				self.path(i)

			PATHS.append(self.max_path)
			self.delete_nodes(self.max_path)
			graph_size -= len(self.max_path)
		return PATHS