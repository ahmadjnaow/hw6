import sqlite3

def create_table():
    connect = sqlite3.connect('cars.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
                id INTEGER PRIMARY KEY,
                nomer TEXT,
                brand TEXT,
                model TEXT,
                year INTEGER,
                opisrabot TEXT,
                status TEXT
                )""")
    connect.commit()
    connect.close()


def add_car():
    connect = sqlite3.connect('cars.db')
    cursor = connect.cursor()

    nomer = input("Введите номер машины: ")
    brand = input("Введите марку машины: ")
    model = input("Введите модель машины: ")
    year = int(input("Введите год выпуска машины: "))
    opisrabot = input("Описание работ: ")
    status = "В обслуживании"

    cursor.execute("INSERT INTO cars (nomer, brand, model, year, opisrabot, status) VALUES (?, ?, ?, ?, ?, ?)",
                   (nomer, brand, model, year, opisrabot, status))

    connect.commit()
    print("Машина успешно добавлена в базу данных.")
    connect.close()


def update_car():
    connect = sqlite3.connect('cars.db')
    cursor = connect.cursor()

    car_id = int(input("Введите id машины: "))
    nomer = input("Введите новый номер машины: ")
    brand = input("Введите новый бренд машины: ")
    model = input("Введите новую модель машины: ")
    year = int(input("Введите новый год выпуска машины: "))

    cursor.execute("UPDATE cars SET nomer = ?, brand = ?, model = ?, year = ? WHERE id = ?",
                   (nomer, brand, model, year, car_id))

    connect.commit()
    connect.close()


def view_all_cars():
    connect = sqlite3.connect('cars.db')
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM cars")
    cars = cursor.fetchall()

    print("Список всех автомобилей:")
    for car in cars:
        print(f"ID: {car[0]}, Номер: {car[1]}, Марка: {car[2]}, Модель: {car[3]}, Год выпуска: {car[4]}, Статус: {car[6]}")
        
    connect.close()


def view_cars_in_service():
    connect = sqlite3.connect('cars.db')
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM cars WHERE status = 'В обслуживании'")
    cars = cursor.fetchall()

    print("Список автомобилей в обслуживании:")
    for car in cars:
        print(f"ID: {car[0]}, Номер: {car[1]}, Марка: {car[2]}, Модель: {car[3]}, Год выпуска: {car[4]}, Описание работ: {car[5]}")
        
    connect.close()


def view_ready_cars():
    connect = sqlite3.connect('cars.db')
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM cars WHERE status = 'Готово к выдаче'")
    cars = cursor.fetchall()

    print("Список автомобилей, готовых к выдаче:")
    for car in cars:
        print(f"ID: {car[0]}, Номер: {car[1]}, Марка: {car[2]}, Модель: {car[3]}, Год выпуска: {car[4]}, Описание работ: {car[5]}")
        
    connect.close()

def main():
    create_table()

    while True:
        print("1. Добавить новый автомобиль")
        print("2. Обновить информацию о машине")
        print("3. Просмотреть список всех автомобилей")
        print("4. Просмотреть список автомобилей в обслуживании")
        print("5. Просмотреть список автомобилей, готовых к выдаче")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_car()
        elif choice == "2":
            update_car()
        elif choice == "3":
            view_all_cars()
        elif choice == "4":
            view_cars_in_service()
       







