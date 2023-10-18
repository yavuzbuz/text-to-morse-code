user_input = input("Write down your text:\n")

morse_code_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                   "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "/"]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " "]

empty_list = []

for n in user_input:
    lower_n = n.lower()
    translate = morse_code_list[alphabet.index(lower_n)]
    empty_list.append(translate)

result = " ".join(empty_list)
print(result)
