from collections import deque

# Define the starting state
start = (3, 3, 1) # (missionaries on the left bank, cannibals on the left bank, boat on left (1) or right (0))

# Define the goal state
goal = (0, 0, 0)

# Define the actions (move two missionaries, move two cannibals, move one cannibal and one missionary, move one missionary and one cannibal)
actions = [
    (2, 0, 1),
    (0, 2, 1),
    (1, 1, 1),
    (1, 0, 1),
    (0, 1, 1)
]

# Define a function to check if a state is valid
def is_valid(state):
    m, c, b = state
    if m < c and m > 0:
        return False
    if m > 3 or m < 0:
        return False
    if c > 3 or c < 0:
        return False
    if b != 1 and b != 0:
        return False
    return True

# Define a function to generate all possible next states from a given state
def next_states(state):
    m, c, b = state
    next_states = []
    for action in actions:
        m2, c2, b2 = action
        if b == 1:
            m2 *= -1
            c2 *= -1
            b2 = 0
        m3, c3 = m + m2, c + c2
        if is_valid((m3, c3, b2)):
            next_states.append((m3, c3, b2))
    return next_states

# Define a function to solve the problem using BFS
def bfs_solve():
    queue = deque([(start, [start])])
    while queue:
        (state, path) = queue.popleft()
        if state == goal:
            return path
        for next_state in next_states(state):
            if next_state not in path:
                queue.append((next_state, path + [next_state]))
    return None

# Call the bfs_solve function to get the solution
solution = bfs_solve()

# Print the solution, if one was found
if solution is not None:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found.")