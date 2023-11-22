import matplotlib.pyplot as plt
data = []

with open("./DATOS/2023-11-22T11:42:12.125703.csv", "r") as f:
    for i in f:
        data.append(i[:-2])

timestamps = []
values1 = []
values2 = []
for i in range(len(data)):    
    timestamps.append(data[i].split(",")[1])
    values1.append(data[i].split(",")[2])
    values2.append(data[i].split(",")[3])
    
plt.figure()
plt.plot(timestamps, values1, label='Ambiente')
plt.plot(timestamps, values2, label='Amplificador')

plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.show()
