cells = 100
hours = 0
doubling_time = 3

print(f"{'Hour':>4} | {'Cells':>6}")

while hours <= 24:
    print(f"{hours:>4} | {cells:>6}")
    hours += doubling_time
    cells *= 2