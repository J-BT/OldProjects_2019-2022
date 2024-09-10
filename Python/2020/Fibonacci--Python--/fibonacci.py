#!/usr/bin/env python

# Fibonacci sequence

def main():
    print("#################################################################")
    print("######*****************************************************######")
    print("###  This programm computes the first-nth fubonacci numbers!! ###")
    print("######*****************************************************######")
    print("#################################################################")

    n_th = int(input("Enter the n-th number : "))

    #--------------------------------------------------------------------------#
    # We initialize the variable which enable us to compute a fibonacci number #
    #--------------------------------------------------------------------------#
    f, prev2 = 0, 0     # where f = fibonacci number
    prev1 = 1


    for i in range(1, n_th + 1):
        if i%2 != 0:
            f += prev1
            prev1 = f
        elif i%2 == 0:
            f+= prev2
            prev2 = f
        print(f)
    print("\n\nEt voilà ^^")

main()
input("Press <Enter> to quit")
