import unittest

from src.binary_maze import bfs, Point, QueueVertex


class MyTestCase(unittest.TestCase):
    def test_find_shortest_path(self):
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

        start = Point(0, 0)
        final = Point(7, 5)



        result = bfs(adjMat, start, final)

        self.assertEqual(12, result)
