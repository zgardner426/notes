import csv
import matplotlib.pyplot as plt


with open('data/library_info.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)

names = [x[0] for x in data ][1:] # all chi library names (alphabetical)
# print(names)
name_index = [x for x in range(len(names))]
# print(name_index)

ytd = [x[-1] for x in data][1:]
# print(ytd)
ytd = [int(x) for x in ytd] # year to date computer sessions as libraries


# plot ytd vs library as a bar graph
plt.figure(1, figsize=(12, 5), tight_layout = True, facecolor="lightblue")
plt.bar(name_index, ytd, color="red")
plt.xticks(name_index, names, rotation=(90), fontsize=8)  # index list, strings list
plt.title("Chicago Library Computer Sessions- 2017", fontsize=20)
plt.ylabel("Computer Use")
plt.show()