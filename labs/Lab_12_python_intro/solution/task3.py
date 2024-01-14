<<<<<<< HEAD
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
=======
def to_characters_histogram(text: str):
    chars = {}
    for char in filter(lambda char: not char.isspace(), text):
        chars.update({char : chars.get(char, 0) + 1})
    sorted_columns = sorted(chars.items())
    max_height = max(chars.values())
    sorted_text_columsn = "\n".join("".join(["#" if height <= column[1] else " " for column in sorted_columns]) for height in range(max_height, 0, -1))
    return sorted_text_columsn + "\n" + "".join([column[0] for column in sorted_columns])

if __name__ == '__main__':
    text = input()
    print(to_characters_histogram(text))
>>>>>>> 8ca2eeef386c20360bbb5f6b8ed0abfe4c98dbf7
