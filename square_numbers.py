squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# a more efficiently written version
revised_squares = []
for value in range(1, 13):
    revised_squares.append(value ** 2)

print(revised_squares)
