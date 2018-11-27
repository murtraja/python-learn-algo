graph = [
	{1:4, 7:8}, # 0th vertex
	{2:8, 7:11, 0:4}, # 1st vertex
	{1:8, 5:4, 8:2}, # 2nd vertex
	{2:7, 4:9, 5:14}, # 3rd vertex
	{3:9, 5:10}, # 4th vertex
	{2:4, 3:14, 4:10, 6:2}, # 5th vertex
	{5:2, 7:1, 8:6}, # 6th vertex
	{0:8, 6:1, 8:7}, # 7th vertex
	{2:2, 6:6, 7:7}, # 8th vertex
]
SOURCE_VERTEX = 0
INF = 1000
shortest = [INF for _ in graph]
shortest[SOURCE_VERTEX] = 0
visited = set()

def pick_minimum():
	minimum = INF + 1;
	minimum_vertex = -1;
	for i in range(0, len(shortest)):
		if i in visited:
			continue;
		if shortest[i] < minimum:
			minimum = shortest[i];
			minimum_vertex = i;
	if minimum_vertex == -1:
		print("No minimum vertext found")
	else:
		print("Minimum vertex {} found with distance {}"
			.format(minimum_vertex, minimum))
		return minimum_vertex


def shortest_path():
	parent = [-1 for _ in range(0, len(graph))]
	while len(visited) != len(graph):
		min_vertex = pick_minimum();
		visited.add(min_vertex);
		for (adjacent_vertex, weight) in graph[min_vertex].iteritems():
			current_value = shortest[adjacent_vertex];
			updated_value = shortest[min_vertex] + weight
			if updated_value < current_value:
				print("vertex {}. shortest {} -> {}"
					.format(adjacent_vertex, shortest[adjacent_vertex], updated_value))
				shortest[adjacent_vertex] = updated_value;
				parent[adjacent_vertex] = min_vertex;
	print("shortest")
	print(shortest)
	print("parents")
	print(parent);
	for vertex in range(0, len(shortest)):
		if vertex == SOURCE_VERTEX:
			continue;
		next_parent = vertex;
		parents = [vertex]
		while next_parent!=SOURCE_VERTEX:
			next_parent = parent[next_parent]
			parents.append(next_parent)
		path_info = " -> ".join(map(str,parents[::-1]))
		print("vertex {}. {} ({})".format(vertex, path_info, shortest[vertex]))

if __name__ == '__main__':
	shortest_path();