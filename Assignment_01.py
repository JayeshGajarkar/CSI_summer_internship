# Lower triangle pattern
def print_lower_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
        

# Upper triangle pattern
def print_upper_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()

# Pyramid
def print_pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("*", end=" ")
        print()

n = 5
print("Lower Triangle Pattern:")
print_lower_triangle(n)

print("Upper Triangle Pattern:")
print_upper_triangle(n)

print("Pyramid")
print_pyramid(n)
