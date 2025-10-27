# Exercise 8: Simple Search - OPTIMIZED

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search = input("Enter a name to search for: ")

if search in names:
    print(f"{search} found at position {names.index(search)}!")
else:
    print(f"{search} not found.")

print(f"\nAll names: {', '.join(names)}")