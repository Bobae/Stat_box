# Permutations and Combination calculator 



# The following function is determine how many number are between a range
# of 1 to 100 (inclusive) that are dividible by x or y.
def div_counts(x,y):
    count = 0
    duplicate = 0
    for i in range(1, 101):
        if i%x == 0:
            print("Good for", x,";", i)
            count = count + 1
            print("count is:",count)
        if i%y == 0:
            print("Good for 5: ", i)
            count = count + 1
            print("count is:",count)
        if i%(x*y) ==0:
            duplicate = duplicate + 1
    print count - duplicate
        
