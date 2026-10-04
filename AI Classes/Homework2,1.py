labels = [    " Cat ",    "DOG",    "cat",    " bird ",        "Dog ",    "UNKNOWN",    "BIRD",    "  cat  "]

a = list(filter(lambda x: x.strip().lower() , labels))
for x in a:
    if x.strip().lower() != "unknown":
        a.append(x)

b = list(map(lambda x: x.strip().lower(), a))
print(b)
