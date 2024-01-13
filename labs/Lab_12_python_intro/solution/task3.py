text = input("Input text: ")
histo_dict = {}
for i in text:
    if i != " ":
        if i in histo_dict:
            histo_dict[i] = histo_dict[i] + 1
        else:
            histo_dict[i] = 1
sorted_dict = dict(sorted(histo_dict.items()))
for i in range(0, max(sorted_dict.values())):
    for j in sorted_dict:
        if sorted_dict[j] >= (max(sorted_dict.values()) - i):
            print("#", end="")
        else:
            print(" ", end="")
    print("\n", end="")
print("".join(list(sorted_dict.keys())))