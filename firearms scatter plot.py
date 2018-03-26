import matplotlib.pyplot as plt
import csv
import numpy as np

with open("data/World firearms murders and ownership - Sheet 1 (1).tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

headers = data.pop(0)
print(headers)


# Homicide by firearm rate per 100k vs Average firearms per 100


homicide_per_100k = []
average_firearms_per_100 = []
country_names =[]
# no wars, no political unrest, established democracies or similar
countries_to_plot = ["United States", "France", "England and Wales", "Netherlands", "Sweden", "Norway", "Canada", "Japan", "South Korea", "Poland", "Australia"]

for i in range(len(data)):
    if data[i][0] in countries_to_plot:
        try:
            homicide = float(data[i][5])
            firearm = float(data[i][7])
            homicide_per_100k.append(homicide)
            average_firearms_per_100.append(firearm)
            names = data[i][0]
            country_names.append(names)
        except:
            print("failed", data[i][0])


plt.figure(1, figsize=(12, 7))
plt.scatter(average_firearms_per_100, homicide_per_100k)
for i in range(len(country_names)):
    plt.annotate(country_names[i], xy=(average_firearms_per_100[i], homicide_per_100k[i]), xytext=(20, 20))
m, b = np.polyfit(homicide_per_100k, average_firearms_per_100, 1)  # 1 for linear (returns m and b)
x = [0, 100]
y = [point * m + b for point in x]
plt.plot(x, y)
plt.title("World Firearm Death")
plt.ylabel("Homicides per 100k population")
plt.xlabel("Firearms per 100")

plt.show()
