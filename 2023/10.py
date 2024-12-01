from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

# replacing data with test data
adata = """\
.....
.S-7.
.|.|.
.L-J.
....."""

LUT = {
        "|": ((-1, 0), (1, 0)),
        "-": ((0, 1), (0, -1)),
        "L": ((-1, 0), (0, 1)),
        "J": ((-1, 0), (0, -1)),
        "7": ((0, -1), (1, 0)),
        "F": ((0, 1), (1, 0)),
}

def returnPoints(matrix, pipesDict, neighborsPoints):
  import re

  startingPosition = next(((i, match.start()) for i, row in enumerate(matrix) if (match := re.search(r"S", row))), (0, 0))

  points = []
  sY = startingPosition[0]
  sX = startingPosition[1]

  for point in neighborsPoints:
    i, j = point

    if(0 <= sY+i < len(matrix) and 0 <= sX+j < len(matrix[0]) and matrix[sY+i][sX+j] != '.'):
      currentSymbol = matrix[sY+i][sX+j]
      pipesNextY, pipesNextX = [pipesDict[currentSymbol][i][iterat+1] for i, iterat in enumerate(point)]

      if(pipesNextY != '' and pipesNextX != ''): points.append((sY+i,sX+j))
  
  return points, sY, sX

def get_valid_neighbors(matrix: tuple[tuple[str]], x: int, y: int):
    for i, j in LUT[matrix[x][y]]:
        yield (x+i, y+j)

lines = data.splitlines()

matrix2 = [entry.strip() for entry in lines]
pipesDict = {
  '-': [['',0,''],[2,'',-2]],
  '|': [[2,'',-2],['',0,'']],
  '7': [['',1,-1],[1,-1,'']],
  'J': [[1,-1,''],[1,-1,'']],
  'L': [[1,-1,''],['',1,-1]],
  'F': [['',1,-1],['',1,-1]]
}

#Get all pipes connected to starting point
neighborsPoints = [[-1,0],[0,-1],[0,1],[1,0]]

def part1() -> int:
    matrix = tuple(tuple(line) for line in lines)
    for i, a in enumerate(matrix):
        for j, b in enumerate(a):
            if b == "S":
                start_pos = (i, j)
    print(f"Initial position: {start_pos}")

    valid_path = [start_pos]

    for n1, n2 in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x, y = start_pos[0] + n1, start_pos[1] + n2
        item = matrix[x][y]
        if item not in LUT: 
            continue
        for i, j in LUT[item]:
            if x + i == start_pos[0] and y + j == start_pos[1]:
                valid = (x, y)
    valid_path.append(valid)
    print(valid_path)

    while True:
        has_valid = False
        for coords in get_valid_neighbors(matrix, *valid_path[-1]):
            if coords not in valid_path:
                has_valid = True
                valid_path.append(coords)
                break
        if not has_valid:
            break

    return len(valid_path)//2

def part2() -> int:
    points, sY, sX = returnPoints(matrix2, pipesDict, neighborsPoints)
    
    points = [(sY, sX), points[0]]

    while True:
        pointsDifference = (points[-2][0] - points[-1][0], points[-2][1] - points[-1][1])
        
        currentSymbol = matrix2[points[-1][0]][points[-1][1]]
        pipeCalc = pipesDict[currentSymbol]

        pipesNextY, pipesNextX = [pipeCalc[i][diff+1] for i, diff in enumerate(pointsDifference)]
        
        nextCoordY, nextCoordX = (points[-2][0] + pipesNextY, points[-2][1] + pipesNextX)
        newPoint = (nextCoordY, nextCoordX)

        if(newPoint == (sY,sX)): break
        points.append(newPoint)
    
    # Shoelace formula
    # A = 1/2 * sum(xi * yi+1 - yi * xi+1)

    # Pick's theorem
    # A = i + points/2 - 1    i - interior points
    # i = A - points/2 + 1

    sumOfPoints = 0
    howManyPoints = len(points)

    for i in range(howManyPoints):
        nextIndex = (i+1) % howManyPoints
        sumOfPoints += points[i][1] * points[nextIndex][0] - points[i][0] * points[nextIndex][1]

    result = round((sumOfPoints/2) - howManyPoints/2 + 1)

    return result


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    #submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    #submit(p2, part="b")