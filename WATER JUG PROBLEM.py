from collections import deque

def solve_water_jug():

    # Initial state: (4L jug, 3L jug)
    start = (0, 0)

    # Goal: Get exactly 2 litres
    goal = 2

    queue = deque()
    queue.append((start, []))

    visited = {start}

    while queue:

        state, path = queue.popleft()
        a, b = state

        # Goal reached
        if a == goal or b == goal:
            return path + [(state, "Goal Reached")]

        moves = []

        # Fill 4L jug
        moves.append(((4, b), "Fill 4L jug"))

        # Fill 3L jug
        moves.append(((a, 3), "Fill 3L jug"))

        # Empty 4L jug
        moves.append(((0, b), "Empty 4L jug"))

        # Empty 3L jug
        moves.append(((a, 0), "Empty 3L jug"))

        # Pour 4L jug -> 3L jug
        amount = min(a, 3 - b)
        moves.append((
            (a - amount, b + amount),
            "Pour 4L -> 3L"
        ))

        # Pour 3L jug -> 4L jug
        amount = min(b, 4 - a)
        moves.append((
            (a + amount, b - amount),
            "Pour 3L -> 4L"
        ))

        for new_state, action in moves:

            if new_state not in visited:

                visited.add(new_state)

                queue.append((
                    new_state,
                    path + [(new_state, action)]
                ))

    return None


# Solve
solution = solve_water_jug()

print("========== WATER JUG PROBLEM ==========\n")

if solution:

    # Initial state
    print("Step 0")
    print("4L Jug = 0 L")
    print("3L Jug = 0 L")
    print()

    # Display all steps
    for step in range(len(solution)):

        state, action = solution[step]

        print("Step", step + 1)
        print("Action :", action)
        print("4L Jug =", state[0], "L")
        print("3L Jug =", state[1], "L")
        print()

    # Final result
    final_state, final_action = solution[-1]

    print("========== FINAL ==========")
    print("4L Jug =", final_state[0], "L")
    print("3L Jug =", final_state[1], "L")

    print("\nPath Cost =", len(solution))
    print("Total Steps =", len(solution))

else:
    print("No solution found.")
