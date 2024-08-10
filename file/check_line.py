def check_for_word():
    word = input("Enter the word you want to search: ")
    with open("practice2.txt", "r") as f:
        data = f.read()
        if data.find(word) != -1:
            print("Found", word)
        else:
            print("Doesn't exist in the file")

check_for_word()

def check_for_line():
    w = input("Enter the word you want to search: ")
    data = True
    line = 1
    with open("practice2.txt", "r") as f:
        while data:
            data = f.readline()
            if w in data:
                print(line)
                return
            line += 1
    return -1

print(check_for_line())  # Corrected to call the function with parentheses

    