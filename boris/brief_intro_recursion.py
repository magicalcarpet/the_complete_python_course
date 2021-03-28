def countdown_from(number):
    if number <= 0:
        return

    print(number) # 5 ==> 4 ==> 3 ==> 2 ==> 1
    countdown_from(number - 1)

countdown_from(5)