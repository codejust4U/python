"""
def magic_square(matrix_val):
    isize = len(matrix_val[0])
    sum_val = []
    for col in range(isize):
        sum_val.append(sum(row[col] for row in matrix_val))
        sum_val.extend([sum(lines) for lines in matrix_val])
        dlresult = 0
        for i in range(0,isize):
            dlresult+=matrix_val[i][i]
        sum_val.append(dlresult)
        dlresult = 0
        for i in range(isize-1,-1,-1):
            dlresult+=matrix_val[i][i]
        sum_val.append(dlresult)
        if len(set(sum_val))>1:
            return False
        return True
        
print(magic_square([[1,2,3],[4,5,6],[7,8,9]]))
print(magic_square([[4,9,2],[3,5,7],[8,1,6]]))

print(magic_square([[13,8,15],[14,12,10],[9,16,11]]))
"""

"""def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]  # Initialize the square with zeros

    # Set the starting position for the first number
    i = 0
    j = n // 2

    # Fill the magic square with numbers
    for num in range(1, n**2 + 1):
        magic_square[i][j] = num

        # Calculate the next position
        next_i = (i - 1) % n
        next_j = (j + 1) % n

        # If the next position is already filled, move down one row
        if magic_square[next_i][next_j] != 0:
            i = (i + 1) % n
        else:
            i, j = next_i, next_j

    return magic_square

# Generate a magic square of size 4x4
square_size = 4
magic_square_4x4 = generate_magic_square(square_size)

# Print the magic square
for row in magic_square_4x4:
    print(row)
"""

"""def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]  # Initialize the square with zeros

    i = n // 2
    j = n - 1

    num = 1

    while num <= n**2:
        if i == -1 and j == n:  # Wrap around if we go out of bounds
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        if magic_square[i][j]:  # If the cell is already filled, move up one row and to the left
            j -= 2
            i += 1
            continue
        else:
            magic_square[i][j] = num
            num += 1

        i -= 1
        j += 1

    return magic_square

# Generate a magic square of size 4x4
square_size = 4
magic_square_4x4 = generate_magic_square(square_size)

# Print the magic square
for row in magic_square_4x4:
    print(row)"""

"""def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]  # Initialize the square with zeros

    i = 0
    j = n // 2
    num = 1

    while num <= n**2:
        magic_square[i][j] = num
        num += 1

        new_i = (i - 1) % n
        new_j = (j + 1) % n

        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i = new_i
            j = new_j

    return magic_square

# Generate a magic square of size 4x4
square_size = 4
magic_square_4x4 = generate_magic_square(square_size)

# Print the magic square
for row in magic_square_4x4:
    print(row)"""

def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]  # Initialize the square with zeros

    i = 0
    j = n // 2
    num = 1

    while num <= n**2:
        magic_square[i][j] = num
        num += 1

        new_i = (i - 1) % n
        new_j = (j + 1) % n

        if magic_square[new_i][new_j] != 0:
            j = (j - 1) % n  # Move one step to the left if the cell is already filled
        else:
            i = new_i
            j = new_j

    return magic_square

# Generate a magic square of size 4x4
square_size = 4
magic_square_4x4 = generate_magic_square(square_size)

# Print the magic square
for row in magic_square_4x4:
    print(row)
