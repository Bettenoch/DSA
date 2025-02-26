import heapq
from typing import List, Tuple


class AStarPathFinder:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0]) if grid else 0

    def heuristic(self, a: Tuple[int, int], b: Tuple[int, int]):
        return abs(a[0] - b[0]) + abs( a[1] - b[1])

    def get_neighbours(self, node: Tuple[int, int])-> List[Tuple[int, int]]:
        x,y = node
        neighbours = []

        directions = [(-1, 0), (1, 0), (-1, 0), (1, 0)]

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if self.rows > nx >= 0 == self.grid[ny][nx] and 0 <= ny < self.columns:
                neighbours.append((nx, ny))
            return neighbours
