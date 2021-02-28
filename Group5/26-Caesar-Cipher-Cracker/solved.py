def get_symbol_list():
    import string
    return list(string.ascii_letters + string.digits + string.punctuation)

def shift_list(shift, symbol_list):
    length = len(symbol_list)
    shift = shift % length
    
    return symbol_list[-shift:] + symbol_list[:-shift]

def crypt(text, shift, encrypt=True):
    symbol_list = get_symbol_list()
    shifted_symbol_list = shift_list(shift, symbol_list)
    
    text = text.split()
    new_text = []
    for word in text:
        new_word = []
        for letter in word:
            if encrypt:
                index = symbol_list.index(letter)
                letter = shifted_symbol_list[index]
            else:
                index = shifted_symbol_list.index(letter)
                letter = symbol_list[index]
                
            new_word.append(letter)
        new_text.append("".join(new_word))
    return " ".join(new_text)

def analyse_text(text_list):
    length = len(text_list)
    correct_cnt = 0
    saitler = "aeiou"
    
    sait_cnt = 0
    samit_cnt = 0
    for word in text_list:
        for letter in word:
            if sait_cnt > 2 or samit_cnt > 2:
                break
                
            if letter.lower() in saitler.lower():
                sait_cnt += 1
                samit_cnt = 0
            else:
                sait_cnt = 0
                samit_cnt += 1
        else:
            correct_cnt += 1
            sait_cnt = samit_cnt = 0
            
    return correct_cnt * 100 / length >= 50

def crach(text):
    length = len(get_symbol_list())
    
    for i in range(length):
        new_text = crypt(text, i, False)
        
        if analyse_text(new_text.split()):
            print(new_text)
            ask = input("Do you want to continue? [y or n]: ")
            if ask.lower() != 'y':
                return i