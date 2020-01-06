import matplotlib.pyplot as plt

i = 0
while (i < 3):
    if (i == 0):
        print('>> enter the present value')
        value = float(input())
    if (i == 1):
        print('>> enter the interest rate')
        interest = float(input())
    if (i == 2):
        print('>> enter the number of year')
        years = float(input())
    i = i + 1

FV = value * (1 + interest) ** years

print("%.2f" % FV)
