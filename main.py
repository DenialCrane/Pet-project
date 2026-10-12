from scooter import scooter

my_scooter = scooter(20, 0 , True)

print("=== СИСТЕМА УПРАВЛЕНИЯ ЭКО-САМОКАТОМ ECO-RIDE ===")

while True:
    print("1 - Начать поездку")
    print("2 - Поставить на зарядку(100%)")
    print("3 - Выйти из симулятора")
    
    choice = input("Выбери действие: ")
    if choice == "1":
        result = my_scooter.start_ride()
        print(result)
    elif choice == "2":
        my_scooter.charge()
        print("Самокат полностью заряжен! Батарея:", my_scooter.battery)
    elif choice == "3":
        print("Завершение работы системы...")
        break
    else:
        print("Не верная команда, попробуйте ещё раз")