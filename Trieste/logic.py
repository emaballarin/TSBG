# maximum number of turns to catch mr.X
maxTurns = 10
# list of the turns when mr.X location is revealed to everyone, possibly empty
reveals = []

# this, and the following files, must point to the new adjacency matrix, taxi, bus and ug arcs, correspondingly
f = open("data/matrix.txt", "r", encoding="utf8")
content = f.read()
f.close()
A = []
rows = content.split('\n')
size = len(rows)
for r in rows:
  A.append([int(c) for c in r if c != ' '])

taxi = {(i+1):set() for i in range(size)}
f = open("data/taxi.txt", "r", encoding="utf8")
content = f.read()
f.close()
for s in content.split('\n'):
  l = s.split(' ')
  taxi[int(l[0])] = {int(p) for p in l[1:]}

bus = {(i+1):set() for i in range(size)}
f = open("data/bus.txt", "r", encoding="utf8")
content = f.read()
f.close()
for s in content.split('\n'):
  l = s.split(' ')
  bus[int(l[0])] = {int(p) for p in l[1:]}

ug = {(i+1):set() for i in range(size)}
f = open("data/ug.txt", "r", encoding="utf8")
content = f.read()
f.close()
for s in content.split('\n'):
  l = s.split(' ')
  ug[int(l[0])] = {int(p) for p in l[1:]}

E = {(i+1):((taxi[i+1].union(bus[i+1])).union(ug[i+1])) for i in range(size)}

# the strings/moves in this function must be properly renamed
def moves(place):
  m = ['taxi']
  if bus[place]:
    m.append('bus')
  if ug[place]:
    m.append('ug')
  return m

# the strings/moves in this function must be properly renamed
def restrictedMoves(state):
  m = []
  if taxi[state[2]].difference(state[1]):
    m.append('taxi')
  if bus[state[2]].difference(state[1]):
    m.append('bus')
  if ug[state[2]].difference(state[1]):
    m.append('ug')
  return m

# the strings/moves in this function must be properly renamed
def dest(place, move):
  if move == 'taxi':
    return taxi[place]
  if move == 'bus':
    return bus[place]
  if move == 'ug':
    return ug[place]

def propagate(source, move):
  target = set()
  for p in source[0]:
    target = target.union(dest(p, move))
  return target.difference(source[1])

def found(state):
  return state[2] in state[1]
