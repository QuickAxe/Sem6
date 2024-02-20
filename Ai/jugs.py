#   We have two jugs of 4L and 3L
#   We need to get 2L of liquid in the 4L one
#
#

parent = {}
visited = set()


def jugs_dfs(current):
    x, y, _ = current

    if current in visited:
        return
    if x == 2:
        return current
    cases = []

    if x > 0:
        cases.append((0, y, "Emptying X"))

    if y > 0:
        cases.append((x, 0, "Emptying Y"))

    if x < 4:
        cases.append((4, y, "Filling X"))

    if y < 3:
        cases.append((x, 3, "Filling Y"))

    if x > 0 and y < 3:
        # x+y <= 3
        #  new_x = 0
        #   new_y = x+y
        if x + y <= 3:
            cases.append((0, x + y, "Pouring from X to Y"))

        # x+y > 3
        #    x y
        #    new_x = x -(3-y)
        #   ne_y   = 3
        else:
            cases.append((x - (3 - y), 3, "Pouring from X to Y"))
    # print("case 6")
    if x < 4 and y > 0:
        if x + y <= 4:
            cases.append((x + y, 0, "Pouring from Y to X"))
        else:
            cases.append((4, y - (4 - x), "Pouring from Y to X"))

    visited.add(current)

    for case in cases:
        if case not in parent:
            parent[case] = current
        if x := jugs_dfs(case):
            return x


answer = jugs_dfs((0, 0, "Start"))

# print(answer)


def print_sol(current):
    if current == (0, 0):
        print(f"{current} ")
        return
    print_sol(parent[current])
    print(f"{current} ")
    return


print_sol(answer)
