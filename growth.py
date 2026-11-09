# Bacterial growth table
# Synthetic, educational example only.

cells = 100
hours = 0
doubling_time = 3

# 1. Print a header line like: Hour | Cells
print("Hour|Cells")

while hours<=24:
    print(hours, cells)
    hours = doubling_time + hours
    cells = cells * 2
