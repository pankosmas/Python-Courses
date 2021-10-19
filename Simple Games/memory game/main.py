
active_game = True
found = 0
hidden = [1, 4, 3, 2, 3, 2, 4, 1]

N = 8

# other states open and temp_open
state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]

while active_game:
    # read first position
    first_pos = int(input("Give 1st position (must be closed and 1-" + str(N) + "): ")) - 1
    while first_pos < 0 or first_pos >= N or state[first_pos] == "open":
        if first_pos < 0:
            print("You entered position below 1.")
        elif first_pos >= N:
            print("You entered position greater than " + str(N) + ".")
        else:
            print("You tried to open an already opened card.")
        first_pos = int(input("Give 1st position (must be closed and 1-" + str(N) + "): ")) - 1

    # read second position
    second_pos = int(input("Give 2nd position (must be closed and 1-" + str(N) + "): ")) - 1
    while (second_pos < 0 or second_pos >= N) or state[second_pos] == "open" or second_pos == first_pos:
        if second_pos < 0:
            print("You entered position below 1.")
        elif second_pos >= N:
            print("You entered position greater than " + str(N) + ".")
        elif second_pos == first_pos:
            print("You entered the same position.")
        else:
            print("You tried to open an already opened card.")
        second_pos = int(input("Give 2nd position (must be closed and 1-" + str(N) + "): ")) - 1

    # change state: both temp open
    state[first_pos] = "temp_open"
    state[second_pos] = "temp_open"

    # print 2 cards current state
    for position in range(N):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(hidden[position], end="")
        else:
            print(hidden[position], end="")
    print("")

    # if same stay open else close again
    if hidden[first_pos] == hidden[second_pos]:
        state[first_pos] = "open"
        state[second_pos] = "open"
        print("Success!")
        found += 2
        if found == N:
            print("Congratulations! Game Finished!")
            active_game = False
    else:
        state[first_pos] = "closed"
        state[second_pos] = "closed"
        print("Failure!")

# print 2 cards current state
    for position in range(N):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(hidden[position], end="")
        else:
            print(hidden[position], end="")
    print("")
