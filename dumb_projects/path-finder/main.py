import curses 
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if (y, x) in path:
                stdscr.addstr(y * 2, x * 4, 'P', RED)
            else:
                stdscr.addstr(y * 2, x * 4, char, BLUE)

def find_start(maze, start):
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == start:
                return y, x

    return None 

def find_path(maze, stdscr):
    start= "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        print_queue(q, stdscr)  # print the queue
        stdscr.refresh()

        if maze[row][col] == end:
            return path
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)        


def print_queue(q, stdscr):
    queue_content = list(q.queue)  # get queue content
    height, width = stdscr.getmaxyx()  # get the height and width of the window
    start_row = height - len(queue_content) - 1  # calculate the row to start printing from

    if start_row < 0:  # if there are more items in the queue than rows available
        queue_content = queue_content[-height+1:]  # only take the last height-1 elements
        start_row = 1  # start from the second row (first row will be the "Queue:" string)

    stdscr.addstr(start_row - 1, 0, "Queue:")
    for i, item in enumerate(queue_content):
        stdscr.addstr(start_row + i, 0, str(item))  # print each item


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0: # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): # DOWN
        neighbors.append((row + 1, col))
    if col > 0: # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): # RIGHT
        neighbors.append((row, col + 1))

    return neighbors

    # breath first search algorithm


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()



wrapper(main)