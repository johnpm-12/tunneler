# John Moffitt 2018

import threading
import heapq

import wx
import wx.lib.pubsub


# thread class that solves the shortest path and sends solution back to main thread through wx pub/sub message system
class SolverThread(threading.Thread):
    def __init__(self, grid):
        super(SolverThread, self).__init__()
        # grid is a list of lists of True and False, True is a wall, False is an empty path
        self.grid = grid
        # stop_flag is used by main thread to tell this thread to stop early if user closes application
        self.stop_flag = False

    # runs in a separate thread when start is called on the thread object, without blocking the main thread
    def run(self):
        # initialize the solution to 0 steps and no locations
        solution_path = set()
        solution_steps = 0
        # initialize a heap to use as a simple priority queue
        min_steps_heap = []
        # initialize the actual item that will be on the heap
        # tuple with (# of steps taken so far, tuple of current location, and a set of all visited locations)
        initial_heap_item = (0, (4, 0), set())
        # heapq.heappush adds the item and maintains heap sorting based on the first element of the item (steps)
        # this means that a heap pop will return the item with the least number of steps
        # so the first one to get to the end is the fastest and we don't have to solve all possible paths to find the fastest
        heapq.heappush(min_steps_heap, initial_heap_item)
        # loop until the heap is empty, or reaching the end will break the loop
        while min_steps_heap:
            # check if this thread has been told to stop by main thread and break early if so
            # this allows the gui to be responsive if closed while solving and not have any background zombie threads running
            if self.stop_flag:
                break
            # pop the item from the heap with the lowest number of steps taken so far
            steps, location, visited = heapq.heappop(min_steps_heap)
            # check if we've reached the end
            if location[0] == 0 and location[1] == 4:
                # set the solution variables to the current set of visited locations and number of steps
                solution_path = visited
                solution_steps = steps
                break
            # add current location to the set of visited locations
            visited.add(location)
            # create a list of adjacent coordinates
            adjacent_locations = [
                (location[0] + 1, location[1]),
                (location[0] - 1, location[1]),
                (location[0], location[1] + 1),
                (location[0], location[1] - 1)
            ]
            # loop over the 4 adjacent locations
            for next_location in adjacent_locations:
                # make sure it's actually inside the grid
                if (0 <= next_location[0] < 5) and (0 <= next_location[1] < 5):
                    # make sure it hasn't already been visited
                    if next_location not in visited:
                        # check if there is a wall there
                        if self.grid[next_location[0]][next_location[1]]:
                            # add the next location to the heap with steps incremented by 8 (7 to destroy wall and 1 to move to it) and a copy of the visited set
                            # a copy is done on the visited set because otherwise, there would only be one visited set and many pointers to it, which breaks it
                            heapq.heappush(min_steps_heap, (steps + 8, next_location, visited.copy()))
                        else:
                            # or add the next location with steps + 1
                            heapq.heappush(min_steps_heap, (steps + 1, next_location, visited.copy()))
        # use pub/sub message system to send the solution to main thread
        wx.CallAfter(wx.lib.pubsub.pub.sendMessage, 'solved', path=solution_path, steps=solution_steps)

    # function that main thread can call if it wants this thread to stop early
    def cancel(self):
        self.stop_flag = True
