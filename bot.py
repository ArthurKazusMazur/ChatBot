import time


def chprint(string):
    for char in string:
        print(char, end="")
        time.sleep(0.25)
    print("\r")


def greet(bot_name, birth_year):
    chprint('Hello! My name is ' + bot_name + '.')
    chprint('I was created in ' + birth_year + '.')


def remind_name():
    chprint('Please, remind me your name.')
    name = input("< ")
    chprint('What a great name you have, ' + name + '!')


def guess_age():
    chprint('Let me guess your age.')
    chprint('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input("< "))
    rem5 = int(input("< "))
    rem7 = int(input("< "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    chprint("Your age is " + str(age) + ": that's a good time to start programming!")


def count():
    chprint('Now I will prove to you that I can count to any number you want.')

    num = int(input("< "))
    curr = 1
    while curr <= num:
        print(curr, '!')
        time.sleep(0.25)
        curr += 1


def test():
    chprint("Let's test your programming knowledge.")
    chprint("Why do we use methods?")
    chprint("1. To repeat a statement multiple times.")
    chprint("2. To decompose a program into several small subroutines.")
    chprint("3. To determine the execution time of a program.")
    chprint("4. To interrupt the execution of a program.")

    variants = [1, 2, 3, 4]

    user_ans = int(input("< "))

    while user_ans != variants[3]:
        chprint('Please, try again.')
        user_ans = int(input("< "))
    else:
        if user_ans == variants[3]:
            return chprint('Completed, have a nice day!')


def end():
    chprint('Congratulations, have a nice day!')


greet('Aidra', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
