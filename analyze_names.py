import pickle
from collections import defaultdict
from statistics import mean, pstdev

with open("names.dat", "rb") as f:
    items = pickle.load(f)

item_counts = defaultdict(list)
for item in items:
    item_counts[item.name].append(item.value)

sort_list = sorted(item_counts, key=lambda name: len(item_counts.get(name)), reverse=True)

output_string = "{:<20} {:<10} {:<10} {:<30}"
print(output_string.format("Item", "Occurences", "Average", "Standard deviation"))
for key in sort_list:
    count = len(item_counts[key])
    if count < 5:
        continue
    line_mean = mean(item_counts[key])
    line_variance = pstdev(item_counts[key], mu=line_mean)
    print(output_string.format(key, count, int(line_mean), int(line_variance)))
