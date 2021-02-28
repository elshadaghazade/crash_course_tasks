import string

symbols = list(string.ascii_letters + string.digits + string.punctuation + "əƏşŞüÜğĞçÇıIйЙцЦуУкКеЕнНгГшШщЩзЗхХъЪфФыЫвВаАпПрРоОлЛдДжЖэЭяЯчЧсСмМиИтТьЬбБюЮ№")

while True:
    while True:
        action = input("Choose one of the following actions: e (encode), d (decode), q (quit) ")

        if not action in "edq":
            print("Choose correct action")
            continue
        else:
            break

    if action == "q":
        print("Bye!")
        break
    elif action == "e":
        
        while True:
            mystr = input("Type your text to encode: ")
            if not mystr.strip():
                print("Text is empty. Try again!")
                continue
            else:
                break

        while True:
            shift = input("Type a shift number. It should be positive or negative integer: ")
            try:
                shift = int(shift) % len(symbols)
                break
            except:
                print("Shift number should be negative or positive integer. Try again!")
                continue
        splitted = mystr.split()
        
        part_one = symbols[:-shift]
        part_two = symbols[-shift:]
        new_symbols = part_two + part_one

        encoded = []
        for word in splitted:
            new_word = []
            for letter in word:
                index = symbols.index(letter)
                new_word.append(new_symbols[index])
            encoded.append("".join(new_word))

        encoded = " ".join(encoded)
        with open("cypher.txt", "w") as f:
            f.write(encoded)
    elif action == "d":
        
        while True:
            shift = input("Type a shift number. It should bepositive or negative integer: ")
            try:
                shift = int(shift) % len(symbols)
                break
            except:
                print("Shift number should be negative or positive integer. Try again!")
                continue
                
        with open("cypher.txt", "r") as f:
            mystr = f.read()
        splitted = mystr.split()
        
        part_one = symbols[:-shift]
        part_two = symbols[-shift:]
        new_symbols = part_two + part_one

        decoded = []
        for word in splitted:
            new_word = []
            for letter in word:
                index = new_symbols.index(letter)
                new_word.append(symbols[index])
            decoded.append("".join(new_word))

        decoded = " ".join(decoded)
        print(decoded)