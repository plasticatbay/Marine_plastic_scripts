import numpy as np
import matplotlib.pyplot as plt
Days = np.arange(1,7)
Growth =0.1
nyears=40
Weight= np.ones(nyears)
fig = plt.figure()
ax = fig.add_subplot(111)
fig.suptitle('{} years simulation of plastic accumulation at Canna Nam Buch\n Linear pollution growth {}%'.format(nyears,Growth*100))


for j in Days:
    Weight[0]= 365.25*j
    for i in range(1, len(Weight)):
        Weight[i] = Weight[i-1]*(1-Growth)


    ax.plot(Weight[::-1].cumsum(), label = str(j)+'kg/day')

ax.legend(loc=2)
ax.set_xlabel('years')
ax.set_ylabel('Weight (kg)')
ax.grid(axis='y', linestyle=':')
plt.show()
