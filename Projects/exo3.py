import csv
import random
import matplotlib.pyplot as plt
import matplotlib.pyplot
import pylab
import collections 

count = 1
save = []
save2 = []
save3 = []
save_ab = []

def check(str, List):
    i = 0
    while i < len(List):
        if str in List:
            return 0
        i += 1
    return 1    
with open('world_bank_tariff.csv','rt') as f, open('world_bank_gdp.csv', 'rt')as f2:
  data = csv.reader(f)
  data2 = csv.reader(f2)
  transposed_csv = list(zip(*data))
  transposed_csv2 = list(zip(*data2))
  result = zip()
  while count < 11 :
        rd = random.randrange(6, 269)
        if (transposed_csv[2][rd-1] == '' or transposed_csv[2][rd-1]  == '0'): 
            count += 0
        elif (transposed_csv2[2][rd-1] == '0' or transposed_csv2[2][rd-1]  == ''): 
            count += 0
        else:
            if (check(transposed_csv[0][rd-1],save3) == 0) :
               count += 0
            else:
                count +=1
                x = (float(transposed_csv2[2][rd-1])) / 1000
                save.append(float(transposed_csv[2][rd-1])/10)
                save2.append(x)
                save3.append(transposed_csv[0][rd-1])
                save_ab.append(transposed_csv[1][rd-1])

print (save, save2, save3)

plt.xlim(0.000, 6.00)
plt.ylim(0, 100)
matplotlib.pyplot.scatter(save, save2, color ='r')
for i, txt in enumerate(save_ab):
    plt.annotate(save_ab[i], (save[i], save2[i]))
matplotlib.pyplot.show()
