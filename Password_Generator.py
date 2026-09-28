import random
import string
onLoop = True
passwordsGenerated = 1
punctuation = "!@#$%^&*()-_=+[]{};:,.<>?"

print('=======================================================')
while onLoop:
    isInvalid = True
    character_pool = ''
    while True:
        size = int(input('\tEnter password length (8 - 16): '))
        if 8 <= size <= 16:
            break
        print('Invalid length. Please enter a value between 8 and 16.')
        

    print('=======================================================')

    passChar = []


    while isInvalid:
        includeLetter = input('\tInclude letters? (Y|N): ')
        while True:
            match includeLetter:
                case 'Y' | 'y':
                    includeLetter = True
                    break
                case 'N' | 'n':
                    includeLetter = False
                    break
                case _:
                    includeLetter = input('Invalid input. Please choose between between (Y|N): ')

        print('=======================================================')

        includeDigit = input('\tInclude Digits? (Y|N): ')
        while True:
            match includeDigit:
                case 'Y' | 'y':
                    includeDigit = True
                    break
                case 'N' | 'n':
                    includeDigit = False
                    break
                case _:
                    includeDigit = input('Invalid input. Please choose between between (Y|N): ')

        print('=======================================================')

        includePunctuation = input('\tInclude Special Characters? (Y|N): ')
        while True:
            match includePunctuation:
                case 'Y' | 'y':
                    includePunctuation = True
                    break
                case 'N' | 'n':
                    includePunctuation = False
                    break
                case _:
                    includePunctuation = input('Invalid input. Please choose between between (Y|N): ')

        print('=======================================================')

        if(includeDigit or includeLetter or includePunctuation):
            if (includeDigit):
                character_pool += string.digits
                isInvalid = False 
            if (includeLetter):
                character_pool += string.ascii_letters
                isInvalid = False 
            if (includePunctuation):
                character_pool += punctuation
                isInvalid = False 
        else:
            print('\tInvalid inputs. Put at least one "Y"')
            print('=======================================================')

    for i in range(size):
        random_char = random.choice(character_pool)
        passChar.append(random_char)
    print('Your randomly generated password is: ', end = '')

    for i in passChar:
        print(i, end ='')

    print('\n=======================================================')
    print('\tPasswords Generated: ', passwordsGenerated)
    print('=======================================================')
    
    onLoop = input('Would you care to generate another password? (Y|N): ')
    while True:
        match onLoop:
            case 'Y' | 'y':
                passwordsGenerated += 1
                break
            case 'N' | 'n':
                onLoop = False
                print('=======================================================')
                print('\tThank you for using this program!')
                print('=======================================================')
                break
            case _:
                onLoop = input('Invalid input. Please choose between between (Y|N): ')
