
def queensproblem(rows, columns):
    solutions = [[]]
    for row in range(rows):
        solutions = add_one_queen(row, columns, solutions)
    return solutions

def add_one_queen(new_row, columns, prev_solutions):
    return [solution + [new_column]
            for solution in prev_solutions
            for new_column in range(columns)
            if no_conflict(new_row, new_column, solution)]

def no_conflict(new_row, new_column, solution):
    return all(solution[row]       != new_column           and
               solution[row] + row != new_column + new_row and
               solution[row] - row != new_column - new_row
               for row in range(new_row))

count = 0
r = input("Enter number of ROWS for Chess/Matrix: ")
c = input("Enter number of COLUMNS for Chess/Matrix: ")

for solution in queensproblem(int(r), int(c)):
    count += 1
    print(solution)

print("\n Total number of solution is: ", count)