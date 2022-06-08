class inject:

    def __init__(value, name, sugar, fat, salt):
        value.name = input('Name: ')
        value.sugar = float(input('Sugar Intake (ONLY IN G): '))
        value.fat = float(input('Fat Intake (ONLY IN G):'))
        value.salt = float(input('Salt Intake (ONLY IN MG): '))
        print()
        value.max_sugar = 38
        value.max_fat = 80
        value.max_salt = 2000

    def inject_is_healthy(value):
        print(f"{value.name} Diagnotic Screen: ")
        if value.sugar <= value.max_sugar:
            print(f'Sugar Intake {value.sugar} is under limit of 38g. YOU ARE OK. Congratulations!')
        else:
            print(f'Sugar Intake {value.sugar} is over limit of 38g. NOT HEALTHY!')
        
        if value.fat <= value.max_fat:
            print(f'Fat Intake {value.fat} under limit of 80g. YOU ARE OK. Congratulations!')
        else:
            print(f'Fat Intake {value.fat} over limit of 80g. NOT HEALTHY!')

        if value.salt <= value.max_salt:
            print(f'Salt Intake {value.salt} under limit of 2000mg. YOU ARE OK. Congratulations!')
        else:
            print(f'Salt Intake {value.salt} over limit of 2000mg. NOT HEALTHY!')


# value name sugar fat for 3 users with testing health check up...
inject1 = inject("user1", 38, 80, 2000)
inject2 = inject("user2", 38, 80, 2000)
inject3 = inject("user3", 38, 80, 2000)

print()
inject1.inject_is_healthy()
print()
inject2.inject_is_healthy()
print()
inject3.inject_is_healthy()
