class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class QueueVertex:
    def __init__(self, point: Point, dist: int):
        self.point = point
        self.dist = dist


ROW_DIRECTION = [-1, 0, 0, 1]
COL_DIRECTION = [0, -1, 1, 0]
TOTAL_DIRECTIONS = 4


def is_valid(row, col):
    return (row >= 0) and (row < TOTAL_ROW_COUNT) and (col >= 0) and (col < TOTAL_COLUMN_COUNT)


def bfs(matrix, start: Point, final: Point):
    source = QueueVertex(start, 0)
    queue = [source]
    visited = [[False for i in range(TOTAL_COLUMN_COUNT)]
               for j in range(TOTAL_ROW_COUNT)]
    visited[start.x][start.y] = True
    if matrix[start.x][start.y] != 1 or matrix[final.x][final.y] != 1:
        return -1
    while queue:
        current_point = queue.pop(0)
        point = current_point.point

        if point.x == final.x and point.y == final.y:
            write_result_to_file(current_point.dist)
            return current_point.dist

        for i in range(TOTAL_DIRECTIONS):
            row = point.x + ROW_DIRECTION[i]
            column = point.y + COL_DIRECTION[i]

            if is_valid(row, column) and matrix[row][column] == 1 and not visited[row][column]:
                visited[row][column] = True
                processed_point = QueueVertex(Point(row, column), current_point.dist + 1)
                queue.append(processed_point)
    return -1


def read_data_from_file():
    with open("input.txt", 'r') as file:
        lines = file.readlines()

    x_start, y_start = map(int, lines[0].strip().split(','))
    x_dest, y_dest = map(int, lines[1].strip().split(','))
    row, column = map(int, lines[2].strip().split(','))

    matrix = []

    for line in lines[3:]:
        numbers = [int(num) for num in line if num.isdigit()]
        matrix.append(numbers)

    return x_start, y_start, x_dest, y_dest, row, column, matrix

def write_result_to_file(result):
    with open('result.txt', 'w') as file:
        file.write(str(result))
x_start, y_start, x_dest, y_dest, row, column, matrix = read_data_from_file()
TOTAL_ROW_COUNT = row
TOTAL_COLUMN_COUNT = column
start = Point(x_start, y_start)
destination = Point(x_dest, y_dest)

bfs(matrix, start, destination)
