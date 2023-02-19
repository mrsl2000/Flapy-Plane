import math
import numpy as np
import matplotlib.pyplot as plt

record_file = open("record.txt","r")
lines = record_file.readlines()

min_record = []
avg = []
max_record = []
number = list(range(1,int(len(lines)/2)+1))

for i in range(int(len(lines)/2)):
    
    tmp1 = lines[2*i].split()
    tmp2 = lines[2*i+1].split()

    min_record.append(int(tmp1[0]))
    avg.append((float(tmp1[1]) + float(tmp2[1])) / 2)
    max_record.append(int(tmp1[2]))

plt.plot(number, min_record, color='r', label='min')
plt.plot(number, avg, color='g', label='avg')
plt.plot(number, max_record, color='b', label='max')

plt.xlabel("Generations")
plt.ylabel("Score")
plt.title("Learning_Curve")

plt.legend()
plt.show()