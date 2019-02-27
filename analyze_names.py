import pickle

with open("names.dat", "rb") as f:
    names = pickle.load(f)

name_counts = {}
for name in names:
    if not name.name in name_counts:
        name_counts[name.name] = 0
    name_counts[name.name] += 1

sort_list = sorted(name_counts, key=name_counts.get, reverse=True)

for key in sort_list:
    print("{} mentioned {} times".format(key, name_counts[key]))
