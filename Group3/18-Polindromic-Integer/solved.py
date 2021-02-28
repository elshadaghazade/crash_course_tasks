def ask_numbers():
    """
    Asks from user two different numbers. But second number should be greater that first number
    """
    while True:
        try:
            number1 = int(input("Type a number: "))
        except:
            print("Number is wrong. Try again!")
            continue

        break

    while True:
        try:
            number2 = int(input("Type a second number: "))
        except:
            print("Number is wrong. Try again!")
            continue

        break
        
    if number2 <= number1:
        print(f"{number2} is less than {number1}. Try again!")
        number1, number2 = ask_numbers()
        
    return number1, number2


def find_natural_polindroms(number1, number2):
    """Finds count of natural polindroms between number1 and number2 (inclusive). Natural polindroms are: 11, 22, 121, 2332 and etc."""
    cnt = 0
    for number in range(number1, number2 + 1):
        number = str(number)
        
        if number == number[::-1]:
            cnt += 1
            
    return cnt


def find_nonlitcher_numbers(number1, number2):
    """Finds count of nonlitcher numbers between number1 and number2 (inclusive)"""
    def is_non_litcher(number, step=1):
        number = str(number)
        
        if step >= 60:
            return False
        elif number != number[::-1]:
            return is_non_litcher(int(number) + int(number[::-1]), step + 1)
        else:
            return True
        
    cnt = 0
    
    for number in range(number1, number2+1):
        if is_non_litcher(number):
            cnt += 1
            
    return cnt


def find_litcher_numbers(number1, number2):
    """Finds count of litcher number and list of them between number1 and number2 (inclusive)"""
    def is_litcher(number, step=1):
        number = str(number)
        
        if step >= 60:
            return True
        elif number != number[::-1]:
            return is_litcher(int(number) + int(number[::-1]), step + 1)
        else:
            return False
        
    cnt = 0
    numbers = []
    
    for number in range(number1, number2+1):
        if is_litcher(number):
            cnt += 1
            numbers.append(number)
            
    return cnt, numbers


number1, number2 = ask_numbers()

natural_polindroms = find_natural_polindroms(number1, number2)
nonlitchers = find_nonlitcher_numbers(number1, number2)
count, litchers = find_litcher_numbers(number1, number2)

print("natural numbers:", natural_polindroms)
print("nonlitcher numbers:", nonlitchers)
print("count of litchers:", count)
print("litcher numbers:", litchers)

