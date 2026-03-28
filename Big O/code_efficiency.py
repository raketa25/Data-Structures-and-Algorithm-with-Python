# Complex output
print("Team\t\tWon\tLost\nLeafs\t\t1\t1\nSabres\t\t0\t2")
print('\n')

# String Formatting
print("{%d, %d, %d}" % (1, 2, 3))
print('\n')
print("%s scored %d and completed %f of the quest" % ('Sloan', 
15, 55))
print('\n')
# Let’s change the line to show only two decimal points
print("%s scored %d and completed %.2f of the quest" % ('Sloan', 
15, 55))
print('\n')

# We can also use the numbers after the ‘%’ symbol to space out the values.
print("%20s%20d" % ('Sloan', 15))
print('\n')

fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
fib(5)