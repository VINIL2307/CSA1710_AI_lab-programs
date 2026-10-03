from collections import deque

# Initial state
# (Vacuum Position, Room A, Room B)
initial_state = ("A", "Dirty", "Dirty")


# Check whether both rooms are clean
def is_goal(state):
    position, A, B = state
    return A == "Clean" and B == "Clean"


# Generate available actions
def get_actions(state):
    position, A, B = state
    actions = []

    # SUCK
    if position == "A" and A == "Dirty":
        actions.append(("SUCK", ("A", "Clean", B)))

    elif position == "B" and B == "Dirty":
        actions.append(("SUCK", ("B", A, "Clean")))

    # RIGHT
    if position == "A":
        actions.append(("RIGHT", ("B", A, B)))

    # LEFT
    if position == "B":
        actions.append(("LEFT", ("A", A, B)))

    return actions


# Breadth First Search
def find_optimal_path(initial_state):

    queue = deque()
    queue.append((initial_state, []))

    visited = set()
    visited.add(initial_state)

    while queue:

        state, path = queue.popleft()

        # Goal check
        if is_goal(state):
            return state, path

        # Generate next states
        for action, next_state in get_actions(state):

            if next_state not in visited:
                visited.add(next_state)

                queue.append(
                    (next_state, path + [(action, next_state)])
                )

    return None, []


# Display all 8 states
print("===== 8 STATES OF VACUUM WORLD =====")

states = [
    ("A", "Clean", "Clean"),
    ("A", "Clean", "Dirty"),
    ("A", "Dirty", "Clean"),
    ("A", "Dirty", "Dirty"),
    ("B", "Clean", "Clean"),
    ("B", "Clean", "Dirty"),
    ("B", "Dirty", "Clean"),
    ("B", "Dirty", "Dirty")
]

for i, state in enumerate(states, 1):
    print("S" + str(i), "=", state)


# Find optimal path
goal_state, path = find_optimal_path(initial_state)


# Display initial state
print("\n===== INITIAL STATE =====")
print("Initial State:", initial_state)


# Display steps
print("\n===== STEP-BY-STEP PATH =====")

print("Initial:", initial_state)

for i, (action, next_state) in enumerate(path, 1):

    print("\nStep", i)
    print("Action:", action)
    print("State:", next_state)


# Calculate final path cost
total_cost = len(path)


# Display final result
print("\n===== FINAL RESULT =====")
print("Goal State:", goal_state)
print("Optimal Path:", end=" ")

for i, (action, state) in enumerate(path):

    print(action, end="")

    if i < len(path) - 1:
        print(" -> ", end="")

print()
print("Total Optimal Path Cost:", total_cost)
