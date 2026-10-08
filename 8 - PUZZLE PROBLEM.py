from heapq import heappush, heappop

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(state):
    cost = 0
    for i in range(9):
        if state[i] != 0:
            j = GOAL.index(state[i])
            cost += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return cost

def moves(state):
    result = []
    z = state.index(0)
    r, c = divmod(z, 3)

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr * 3 + nc
            new = list(state)
            new[z], new[nz] = new[nz], new[z]
            result.append(tuple(new))

    return result

def solve(start):
    pq = []
    heappush(pq, (h(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == GOAL:
            return path, g

        for next_state in moves(state):
            if next_state not in visited:
                heappush(
                    pq,
                    (g + 1 + h(next_state),
                     g + 1,
                     next_state,
                     path)
                )

    return None, 0

def display(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else "_" 
                       for x in state[i:i+3]))

# Input
start = tuple(map(int, input(
    "Enter 9 numbers (0 for blank): "
).split()))

path, cost = solve(start)

if path:
    print("\n========== SOLUTION ==========")

    for i, state in enumerate(path):
        print("\nStep", i)
        display(state)

    print("\n==============================")
    print("Final Path Cost =", cost)
    print("Total Steps     =", len(path) - 1)
    print("==============================")
else:
    print("No solution exists.")
