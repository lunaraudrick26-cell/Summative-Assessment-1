# Exercise 7: Some Counting - OPTIMIZED

counts = [
    ("0 to 50", range(0, 51)),
    ("50 to 0", range(50, -1, -1)),
    ("30 to 50", range(30, 51)),
    ("50 to 10 (by 2s)", range(50, 9, -2)),
    ("100 to 200 (by 5s)", range(100, 201, 5))
]

for label, nums in counts:
    print(f"{label}: {' '.join(map(str, nums))}\n")