file = open("input.txt")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class queueNode:
    def __init__(self, point: Point, dist: int):
        self.point = point
        self.dist = dist


row_direction = [-1, 0, 0, 1]
col_direction = [0, -1, 1, 0]


def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


def bfs(graph, start: Point, final: Point):
    s = queueNode(start, 0)
    queue = [s]
    visited = [[False for i in range(COL)]
               for j in range(ROW)]
    visited[start.x][start.y] = True
    if graph[start.x][start.y] != 1 or graph[final.x][final.y] != 1:
        return -1
    while queue:
        current_node = queue.pop(0)
        point = current_node.point

        if point.x == final.x and point.y == final.y:
            with open('result.txt', 'w') as file:
                file.write(str(current_node.dist))
            return current_node.dist

        for i in range(4):
            row = point.x + row_direction[i]
            column = point.y + col_direction[i]

            if is_valid(row, column) and graph[row][column] == 1 and not visited[row][column]:
                visited[row][column] = True
                adj_cell = queueNode(Point(row, column), current_node.dist + 1)
                queue.append(adj_cell)
    return -1


lines = file.readline()
parts = lines.split(",")
x = int(parts[0])
y = int(parts[1])

lines = file.readline()
parts = lines.split(",")
x_dest = int(parts[0])
y_dest = int(parts[1])

lines = file.readline()
parts = lines.split(",")
row = int(parts[0])
column = int(parts[1])

adjMat = [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
          [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
          [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
          [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
          [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]


ROW = row
COL = column
start = Point(x, y)
dest = Point(x_dest, y_dest)
print(bfs(adjMat, start, dest))
