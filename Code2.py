def print_grid(arr):
    for row in arr:
        print(" ".join(map(str, row)))

def find_empty_location(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return i, j
    return None

def used_in_row(arr, row, num):
    return num in arr[row]

def used_in_col(arr, col, num):
    return num in [arr[i][col] for i in range(9)]

def used_in_box(arr, start_row, start_col, num):
    return num in [arr[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]

def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)

def solve_sudoku(arr):
    empty_location = find_empty_location(arr)

    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 10):
        if check_location_is_safe(arr, row, col, num):
            arr[row][col] = num

            if solve_sudoku(arr):
                return True

            arr[row][col] = 0

    return False

if __name__ == "__main__":
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    if solve_sudoku(grid):
        print_grid(grid)
    else:
        print("No solution exists")
