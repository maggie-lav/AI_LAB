print("Hello, I'll take you to the GOAL")
mapRooms = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['E']
}

startRoom = 'A'
goalRoom = 'F'

print("Starting Room:", startRoom)
print("Goal Room:", goalRoom)
print("Map of rooms:" ,mapRooms)
print(r"            A          ")
print(r"           / \         ")
print(r"          B   C        ")
print(r"         / \   \       ")
print(r"        D   E   F      ")


def bfs(start, goal):
  queue = [start]
  visited =[]
  order =[]
  while queue:
    current = queue.pop(0)
    if current in visited:
      continue
    visited.append(current)
    order.append(current)

    if current == goal:
      return order

    for neighbor in mapRooms[current]:
      queue.append(neighbor)

  return order

order = bfs("A","F")
print(order)
print(len(order))

def dfs(start, goal):
  stack = [start]
  visited =[]
  order =[]
  while stack:
    current = stack.pop()
    visited.append(current)
    order.append(current)
    if current == goal:
      return order

    for neighbor in mapRooms[current]:
      stack.append(neighbor)

  return order

order = dfs("A","F")
print(order)
print(len(order))
print(order)

def bfs_path(start, goal, graph):
    queue = [(start, [start])]  # Queue stores (current_node, current_path)
    visited = set()

    while queue:
        current_node, path = queue.pop(0)

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

    return None  # No path found

print("BFS Path from", startRoom, "to", goalRoom, ":")
b_path = bfs_path(startRoom, goalRoom, mapRooms)
if b_path:
    print(b_path)
    print("Path length (nodes):", len(b_path))
else:
    print("No path found.")

    def dfs_path(start, goal, graph):
    stack = [(start, [start])]  # Stack stores (current_node, current_path)
    visited = set()

    while stack:
        current_node, path = stack.pop()

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)
            # Iterate neighbors in reverse for standard DFS behavior (leftmost child first)
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))

    return None  # No path found

print("\nDFS Path from", startRoom, "to", goalRoom, ":")
d_path = dfs_path(startRoom, goalRoom, mapRooms)
if d_path:
    print(d_path)
    print("Path length (nodes):", len(d_path))
else:
    print("No path found.")

    def find_all_paths(start, goal, graph):
    all_paths = []

    def dfs_recursive(current_node, current_path):
        # Add current_node to the current path
        current_path = current_path + [current_node]

        # If the current_node is the goal, we found a path
        if current_node == goal:
            all_paths.append(current_path)
            return

        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            # Avoid cycles within the current path
            if neighbor not in current_path:
                dfs_recursive(neighbor, current_path)
