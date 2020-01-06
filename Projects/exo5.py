
import numpy as np
import matplotlib.pyplot as plt

print("USD base")
new = []
new.append(1)
GBP = float(input())
new.append(GBP)
CAD = float(input())
new.append(CAD)
EUR = float(input())
new.append(EUR)
AUD = float(input())
new.append(AUD)
print (new)

gbp = []
cad = []
eur = []
aud = []

x = 0
i = 0
while (x < 5):
    tmp = x
    i = 0
    while(i < 5):

            tmp2 = new[x]
            value=  new[i]/tmp2
            final = "%.5f" % round(value, 5)
            if (final == '1.00000'):
                final = 1

            if (x == 1):
                gbp.append(final)
            if (x == 2):
                cad.append(final)
            if (x == 3):
                eur.append(final)
            if (x == 4):
                aud.append(final)
            if (i == tmp & x == tmp ):
                i = i + 1
            else:
                 i = i + 1
          
    x = x + 1

fig = plt.figure()
ax = fig.add_subplot(111)
y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]    
col_labels = ['USD', 'GBP','CAD','EUR', 'AUD']
row_labels = ['USD', 'GBP','CAD','EUR', 'AUD']
table_vals = [[new[0],gbp[0],cad[0],eur[0],aud[0]],
[new[1],gbp[1],cad[1], eur[1], aud[1]],
[new[2],gbp[2],cad[2], eur[2], aud[2]],
[new[3],gbp[3],cad[3], eur[3], aud[3]],
[new[4],gbp[4],cad[4], eur[4], aud[4]]]


the_table = plt.table(cellText=table_vals,
                      colWidths=[0.1] * 5,
                      rowLabels=row_labels,
                      colLabels=col_labels,
                      loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.scale(2.5, 2.5)

plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
for pos in ['right','top','bottom','left']:
    plt.gca().spines[pos].set_visible(False)
plt.savefig('matplotlib-table.png', bbox_inches='tight', pad_inches=0.05)


plt.show()

