# -*- coding: utf-8 -*-
"""Task1A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mEANwxt_pXinhSxXKA_rQBUX8Ey8vORJ
"""

from google.colab import drive
drive.mount('/content/drive')

task1a_input = open(file='/content/drive/MyDrive/CSE221/Lab 05/input1a.txt', mode='r')

task1a_output = open(file='/content/drive/MyDrive/CSE221/Lab 05/output1a.txt', mode='w')

def dfs_visit(graph, u, color, time, d, f, p):
    color[u] = 'gray'
    time[0] += 1
    d[u] = time[0]
    for v in graph[u]:
        if color[v] == 'white':
            p[v] = u
            dfs_visit(graph, v, color, time, d, f, p)
    color[u] = 'black'
    time[0] += 1
    f[u] = time[0]

def dfs(graph, V):
    color = {v: 'white' for v in range(1, V + 1)}
    d = {v: 0 for v in range(1, V + 1)}
    f = {v: 0 for v in range(1, V + 1)}
    p = {v: None for v in range(1, V + 1)}
    time = [0]
    for u in range(1, V + 1):
        if color[u] == 'white':
            dfs_visit(graph, u, color, time, d, f, p)
    return f

lst = task1a_input.readline().strip().split(" ")
v = int(lst[0])
e = int(lst[1])
adj_list = {}
for i in range(1, v+1):
    adj_list[i] = []
for i in range(e):
    lst2 = task1a_input.readline().strip().split()
    u = int(lst2[0])
    v = int(lst2[1])
    adj_list[u].append(v)

def find_order(V, graph):
    f_time = dfs(graph, V)
    sorted_vert = sorted(f_time, key=lambda v: f_time[v], reverse=True)
    return sorted_vert

order = find_order(v, adj_list)
if len(order) == v:
    task1a_output.write(str(order))
else:
    task1a_output.write('IMPOSSIBLE')

task1a_input.close()
task1a_output.close()