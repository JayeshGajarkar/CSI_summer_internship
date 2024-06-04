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

n = 5
print("Lower Triangle Pattern:")
print_lower_triangle(n)

print("Upper Triangle Pattern:")
print_upper_triangle(n)
