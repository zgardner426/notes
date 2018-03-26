import csv
import matplotlib.pyplot as plt


with open('data/library_info.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)

names = [x[0].strip() for x in data ][1:] # all chi library names (alphabetical)
# print(names)
name_index = [x for x in range(len(names))]
# print(name_index)

ytd = [x[-1] for x in data][1:]
# print(ytd)
ytd = [int(x) for x in ytd] # year to date computer sessions as libraries


# plot ytd vs library as a bar graph
plt.figure(1, figsize=(12, 5), tight_layout = True, facecolor="lightblue")
plt.bar(name_index, ytd, color="red")
plt.xticks(name_index, names, rotation=(90), fontsize=8)  # index list, starings list
plt.title("Chicago Library Computer Sessions- 2017", fontsize=20)
plt.ylabel("Computer Use")
plt.show()


# plot three libraries

headers = data.pop(0)
print(headers)
print(names)

print(names.index("Lincoln Park")) # index of lincoln park
print(names.index("Lincoln Belmont"))
print(names.index("Sulzer Regional"))

month_names = headers[1: -1]
print(month_names)

month_num = [x for x in range(12)]

sulzer_y = data[names.index("Sulzer Regional")][1:-1]
sulzer_y = [int(x) for x in sulzer_y]
lb_y = data[names.index("Lincoln Belmont")][1:-1]
lb_y = [int(x) for x in lb_y]
lp_y = data[names.index("Lincoln Park")][1:-1]
lp_y = [int(x) for x in lp_y]

plt.figure(2, tight_layout=True)
plt.plot(month_num, sulzer_y, label="Sulzer")
plt.plot(month_num, lb_y, label="Lincoln Belmont")
plt.plot(month_num, lp_y, label="Lincoln Park")
plt.title("computure use per month (2017")
plt.ylabel("usage")
plt.xlabel("month")
plt.xticks(month_num, month_names, rotation=90)
plt.legend(bbox_to_anchor=(.75, .40), loc="center")
plt.show()