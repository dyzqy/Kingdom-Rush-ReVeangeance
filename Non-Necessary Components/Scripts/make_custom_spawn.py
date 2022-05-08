# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:37:08 2021

@author: mmlho
"""

import pickle
import random
import itertools as it

DIRECTORY = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Kingdom Rush Vengeance\\'
LEVEL = 26
PATHS = pickle.load(open(DIRECTORY + f'Revengeance\\Nodes\\level{LEVEL}_nodes', 'rb'))
MAXPATH = len(PATHS)
MINNODE = 20
MAXNODE = [110, 140, 160, 140]

random.seed(0)
with open(f'temp_level{LEVEL}.txt', 'w') as file:
    file.write('')

def make_single_spawn(paths, level, enemy, path, subpath, node, delay):
    x, y = paths[path][subpath][node]
    
    with open('spawn_template.txt', 'r') as file:
        template = ''.join([line for line in file])
        template = template.format(enemy=enemy, subpath=subpath, x=x, y=y, node=node, path=path, delay=delay)
    
    with open(f'temp_level{level}.txt', 'a') as file:
        file.write(template)
        file.write('\n')

def make_formation(paths, level, enemy, path, formation, start_node, delay):
    for subpath, node in formation:
        make_single_spawn(paths, level, enemy, path, subpath, start_node + node, delay)

WEDGE = [(1, 0), (2, 0), (0, 3)]
DIAMOND = [(0, 0), (1, 3), (2, 3), (0, 6)]
SQUARE = list(it.product([0, 1, 2], [0, 3, 6]))
SQUAD = SQUARE + [(0, 9)]
FISH = DIAMOND + [(1, 9), (2, 9)]

time = 0
for _ in range(10):
    path = random.randrange(0, MAXPATH)
    subpath = random.randint(0, 2)
    node = random.randint(MINNODE, MAXNODE[path])
    while path == 2 and 88 <= node <= 119:
        node = random.randint(MINNODE, MAXNODE[path])
    make_single_spawn(PATHS, 26, 'skeleton', path, subpath, node, time)
    
for _ in range(10):
    path = random.randrange(0, MAXPATH)
    subpath = random.randint(0, 2)
    node = random.randint(MINNODE, MAXNODE[path])
    while path == 2 and 88 <= node <= 119:
        node = random.randint(MINNODE, MAXNODE[path])
    make_single_spawn(PATHS, 26, 'skeleton', path, subpath, node, time + 1)

time = 10
for _ in range(15):
    path = random.randrange(0, MAXPATH)
    subpath = random.randint(0, 2)
    node = random.randint(MINNODE, MAXNODE[path])
    while path == 2 and 88 <= node <= 119:
        node = random.randint(MINNODE, MAXNODE[path])
    make_single_spawn(PATHS, 26, 'skeleton', path, subpath, node, time)

for _ in range(15):
    path = random.randrange(0, MAXPATH)
    subpath = random.randint(0, 2)
    node = random.randint(MINNODE, MAXNODE[path])
    while path == 2 and 88 <= node <= 119:
        node = random.randint(MINNODE, MAXNODE[path])
    make_single_spawn(PATHS, 26, 'skeleton', path, subpath, node, time + 1)
    
time = 20
for _ in range(10):
    path = random.randrange(0, MAXPATH)
    start_node = random.randint(MINNODE, MAXNODE[path])
    while path == 2 and 82 <= start_node <= 119:
        start_node = random.randint(MINNODE, MAXNODE[path])
    make_formation(PATHS, 26, 'skeleton', path, DIAMOND, start_node, time)

time = 35
make_formation(PATHS, 26, 'skeleton', 1, SQUAD, 60, time)
make_formation(PATHS, 26, 'skeleton', 3, SQUAD, 60, time)
make_single_spawn(PATHS, 26, 'skeleton_golem', 0, 0, 12, time)
make_single_spawn(PATHS, 26, 'skeleton_golem', 2, 0, 75, time)

time = 45
make_formation(PATHS, 26, 'skeleton', 1, SQUARE, 80, time)
make_formation(PATHS, 26, 'skeleton', 3, SQUARE, 80, time)
make_single_spawn(PATHS, 26, 'skeleton_golem', 1, 0, 77, time)
make_single_spawn(PATHS, 26, 'skeleton_golem', 3, 0, 77, time)
make_single_spawn(PATHS, 26, 'skeleton_knight', 1, 0, 89, time)
make_single_spawn(PATHS, 26, 'skeleton_knight', 3, 0, 89, time)

time = 60
for _ in range(5):
    path = random.randrange(0, MAXPATH)
    subpath = random.randint(0, 2)
    node = random.randint(MINNODE, MAXNODE[path])
    while path == 2 and 88 <= node <= 119:
        node = random.randint(MINNODE, MAXNODE[path])
    make_single_spawn(PATHS, 26, 'haunted_skeleton', path, subpath, node, time)

for _ in range(5):
    path = random.randrange(0, MAXPATH)
    subpath = random.randint(0, 2)
    node = random.randint(MINNODE, MAXNODE[path])
    while path == 2 and 88 <= node <= 119:
        node = random.randint(MINNODE, MAXNODE[path])
    make_single_spawn(PATHS, 26, 'haunted_skeleton', path, subpath, node, time + 1)

time = 70
make_formation(PATHS, 26, 'haunted_skeleton', 0, WEDGE, 40, time)
make_formation(PATHS, 26, 'haunted_skeleton', 2, WEDGE, 80, time)

time = 80
make_formation(PATHS, 26, 'haunted_skeleton', 1, WEDGE, 60, time)
make_formation(PATHS, 26, 'haunted_skeleton', 3, WEDGE, 60, time)

time = 90
make_formation(PATHS, 26, 'skeleton', 0, FISH, 60, time)
make_formation(PATHS, 26, 'skeleton', 2, FISH, 120, time)
make_single_spawn(PATHS, 26, 'skeleton_knight', 0, 0, 72, time)
make_single_spawn(PATHS, 26, 'skeleton_knight', 2, 0, 132, time)

time = 95
make_formation(PATHS, 26, 'skeleton_knight', 1, DIAMOND, 75, time)
make_formation(PATHS, 26, 'skeleton_knight', 3, DIAMOND, 75, time)
make_single_spawn(PATHS, 26, 'skeleton_golem', 1, 0, 72, time)
make_single_spawn(PATHS, 26, 'skeleton_golem', 3, 0, 72, time)

time = 100
make_formation(PATHS, 26, 'skeleton_knight', 1, SQUAD, 70, time)
make_formation(PATHS, 26, 'skeleton_knight', 3, SQUAD, 70, time)

time = 110
make_formation(PATHS, 26, 'skeleton_golem', 1, WEDGE, 70, time)
make_formation(PATHS, 26, 'skeleton_golem', 3, WEDGE, 70, time)

time = 130
for _ in range(3):
    path = random.randrange(0, MAXPATH)
    subpath = random.randint(0, 2)
    node = random.randint(MINNODE, MAXNODE[path])
    while path == 2 and 88 <= node <= 119:
        node = random.randint(MINNODE, MAXNODE[path])
    make_single_spawn(PATHS, 26, 'tainted_treant', path, subpath, node, time)

for _ in range(3):
    path = random.randrange(0, MAXPATH)
    subpath = random.randint(0, 2)
    node = random.randint(MINNODE, MAXNODE[path])
    while path == 2 and 88 <= node <= 119:
        node = random.randint(MINNODE, MAXNODE[path])
    make_single_spawn(PATHS, 26, 'tainted_treant', path, subpath, node, time + 1)

time = 145
make_formation(PATHS, 26, 'skeleton', 1, SQUARE, 80, time)
make_formation(PATHS, 26, 'skeleton', 3, SQUARE, 80, time)
make_single_spawn(PATHS, 26, 'tainted_treant', 1, 0, 89, time)
make_single_spawn(PATHS, 26, 'tainted_treant', 3, 0, 89, time)
make_single_spawn(PATHS, 26, 'haunted_skeleton', 1, 0, 77, time)
make_single_spawn(PATHS, 26, 'haunted_skeleton', 3, 0, 77, time)

time = 165
make_formation(PATHS, 26, 'skeleton', 1, SQUARE, 80, time)
make_formation(PATHS, 26, 'skeleton', 3, SQUARE, 80, time)
make_single_spawn(PATHS, 26, 'skeleton_golem', 1, 0, 77, time)
make_single_spawn(PATHS, 26, 'skeleton_golem', 3, 0, 77, time)
make_single_spawn(PATHS, 26, 'tainted_treant', 1, 0, 89, time)
make_single_spawn(PATHS, 26, 'tainted_treant', 3, 0, 89, time)
make_single_spawn(PATHS, 26, 'skeleton_knight', 1, 1, 89, time)
make_single_spawn(PATHS, 26, 'skeleton_knight', 3, 1, 89, time)
make_single_spawn(PATHS, 26, 'skeleton_knight', 1, 2, 89, time)
make_single_spawn(PATHS, 26, 'skeleton_knight', 3, 2, 89, time)

time = 185
make_formation(PATHS, 26, 'tainted_treant', 0, WEDGE, 30, time)
make_formation(PATHS, 26, 'tainted_treant', 3, WEDGE, 70, time)
make_formation(PATHS, 26, 'haunted_skeleton', 1, DIAMOND, 60, time + 1)
make_formation(PATHS, 26, 'haunted_skeleton', 2, DIAMOND, 63, time + 1)

time = 200
make_single_spawn(PATHS, 26, 'tainted_treant', 1, 0, 67, time)
make_single_spawn(PATHS, 26, 'tainted_treant', 2, 0, 70, time)
make_formation(PATHS, 26, 'haunted_skeleton', 1, FISH, 55, time + 1)
make_formation(PATHS, 26, 'haunted_skeleton', 2, FISH, 58, time + 1)

del PATHS
