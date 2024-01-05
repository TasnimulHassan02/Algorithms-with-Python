# -*- coding: utf-8 -*-
"""Task6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XU5xMvu7O71JVDp0k4mX57EvOoMHOru8
"""

from google.colab import drive
drive.mount('/content/drive')

task6_input = open(file='/content/drive/MyDrive/CSE221/Lab 04/input6.txt', mode='r')

task6_output = open(file='/content/drive/MyDrive/CSE221/Lab 04/output6.txt', mode='w')

def max_diamonds_jumanji(grid):
    def dfs(r, c):
        if r < 0 or r >= R or c < 0 or c >= H or grid[r][c] == '#':
            return 0
        diamonds = 0
        if grid[r][c] == 'D':
            diamonds += 1
        grid[r][c] = '#'
        diamonds += max(dfs(r + 1, c),dfs(r - 1, c),dfs(r, c + 1),dfs(r, c - 1))
        return diamonds
    R, H = len(grid), len(grid[0])
    max_diamonds = 0
    for row in range(R):
        for col in range(H):
            if grid[row][col] == '.':
                max_diamonds = max(max_diamonds, dfs(row, col))
    return max_diamonds

R, H = map(int, task6_input.readline().strip().split())
grid = [list(task6_input.readline().strip()) for _ in range(R)]
task6_output.write(str(max_diamonds_jumanji(grid)))

task6_input.close()
task6_output.close()