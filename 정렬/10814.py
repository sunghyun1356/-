# Read an integer input
n = int(input())

# Initialize an empty list to store values
values = []

# Read 'n' lines of input
for i in range(n):
    values.append(input().split())

# Sort the list based on the first element of each sublist
values = sorted(values, key=lambda x: x[0])

# Print the sorted values
for value in values:
    print(" ".join(value))
