import numpy as np

def gauss_jordan_elimination(A, b):
    
    # Augmenting the matrix A with the column vector b
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))

    # Applying Gauss-Jordan elimination
    rows, cols = augmented_matrix.shape
    for i in range(rows):
        # Partial Pivoting
        pivot_row = max(range(i, rows), key=lambda k: abs(augmented_matrix[k, i]))
        augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]

        # Make the diagonal element 1
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]

        # Make other elements in the column zero
        for j in range(rows):
            if i != j:
                augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]

    # Extracting the solution vector
    x = augmented_matrix[:, -1]

    return x

# Get user input for the coefficient matrix A
rows = int(input("Enter the number of rows for the coefficient matrix A: "))
cols = int(input("Enter the number of columns for the coefficient matrix A: "))

A = np.zeros((rows, cols))
print("Enter the elements of the coefficient matrix A:")
for i in range(rows):
    A[i] = [float(input(f"A[{i}][{j}]: ")) for j in range(cols)]

# Get user input for the right-hand side vector b
b = np.array([float(input(f"Enter the element for b[{i}]: ")) for i in range(rows)])

# Solve the system of equations
solution = gauss_jordan_elimination(A, b)
print("Solution:", solution)
