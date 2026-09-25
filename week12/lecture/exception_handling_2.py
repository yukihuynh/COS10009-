from quadratic import solve

# try catch with customised error message
try:
    x1, x2 = solve(1, 0, 1)
except ValueError as e:
    print("Error:", e)
