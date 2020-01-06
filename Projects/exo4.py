import matplotlib.pyplot as plt

quantity= []
y_utility= []
print('Please enter a product')
product = input()
print('Please enter the maximum quantity')
max = int(input())
i = 0
while (i < max):
    print('For',max - i,product,' what added level hapiness do you ?')
    quantity.append(max - i)
    y_utility.append(int(input()))
    i = i + 1
y_utility.reverse()
print (y_utility)
print(quantity)

plt.plot(y_utility,quantity, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.axis([y_utility[0] - 2 ,y_utility[i - 1] + 2, 0, max + 2 ])
plt.ylim(0, max + 2, y_utility[0] , y_utility[i - 1] + 2)
plt.ylabel('utility')
plt.show()

