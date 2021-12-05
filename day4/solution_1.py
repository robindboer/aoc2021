import os

input_file = open("./input.txt", "r")

draw_order = [int(num) for num in input_file.readline().split(",")]
boards = []

for line in input_file.readlines():
    if line.startswith("\n"):
        continue
    row = [int(num) for num in line.replace("\n", "").split()]
    boards.append(row)

for current_draw in draw_order:
    for row in boards:
        for i, num in enumerate(row):
            if num == current_draw:
                row[i] = -1
    
    winning_board_no = None

    # Check for horizontal bingo
    for i, row in enumerate(boards):
        if sum(row) == -5:
            winning_board_no = divmod(i, 5)[0]
    
    # Check for vertical bingo
    columns = list(zip(*boards))
    for column in columns:
        board_columns = [column[i:i + 5] for i in range(0, len(column), 5)]
        for i, col in enumerate(board_columns):
            if sum(col) == -5:
                winning_board_no = i
    
    if winning_board_no:
        start = winning_board_no * 5
        winning_board = boards[start:start + 5]
        remaining_numbers = []
        for row in winning_board:
            for num in row:
                if num >0:
                    remaining_numbers.append(num)

        print(f"remaining: {sum(remaining_numbers)}")
        print(f"current draw: {current_draw}")
        print(f"solution: {sum(remaining_numbers) * current_draw}")
        break

