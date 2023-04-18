def newtonSqrt(n): 
    approx = 0.5 * n
    better = 0.5 * (approx + n/approx) 
    while better != approx:
        approx = better
        better = 0.5 * (approx + n/approx) 
    return approx
print('The square root is' ,newtonSqrt(int(input("Enter the number: "))))
