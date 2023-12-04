from aocd import data, submit, lines
import numpy as np
from scipy.signal import convolve2d

def part1(d, steps=100):
    arr = np.array([[*line] for line in d.splitlines()], dtype=int)
    return sum(flash(arr).sum() for _ in range(steps))

def part2(d):
    arr = np.array([[*line] for line in d.splitlines()], dtype=int)
    step = 0
    while np.any(arr):
        flash(arr)
        step += 1
    return step

def flash(arr):
    arr += 1
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    flashed = np.zeros(arr.shape, dtype=bool)
    while np.any(flashing := arr > 9):
        flashed |= flashing
        arr += convolve2d(flashing, mask, mode='same')
        arr[flashed] = 0
    return flashed

if __name__ == '__main__':
    print(f"Part 1: {part1(data)}")
    #submit(part1(data))
    print(f"Part 2: {part2(data)}")
    submit(part2(data))