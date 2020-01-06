
import matplotlib.pyplot as plt



demand_y = [10.,14,18,22,28,35,45,57,73,100]
axi_x = list([50, 45,40,35,30,25,20,15,10,5])
supply_y = [100,97,94,89,84,77,68,57,40,0]

plt.ylim(10, 100)

plt.plot(axi_x, demand_y)
plt.plot(axi_x, supply_y)
plt.xlim(5, 50)

plt.show()