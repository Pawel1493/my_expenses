import sys

EXPENSES = []

MONTHS = {1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec',
          7: 'Lipiec', 8: 'Sierpień', 9: 'Wrzesień', 10: 'Październik', 11: 'Listopad', 12: 'Grudzień'}

def add_expense(month):
    amount_expense = int(input("Kwota wydatku [zł]: "))
    category = input("Podaj kategorię wydatku: ")
    expense = (amount_expense, category, month)
    EXPENSES.append(expense)


def show_expenses(month):
    print("\nWszystkie wydatki miesiąca: ")
    for expense_amount, category, expense_month in EXPENSES:
        if month == expense_month:
            print(f" {expense_amount} - {category}")


def show_stats(month):
    all_month_expenses = sum(expense_amount for expense_amount, _, expense_month in EXPENSES if expense_month == month)
    year_total_amount = sum(expense_amount for expense_amount, _, _ in EXPENSES)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in EXPENSES if expense_month == month)
    number_of_expenses_year = len(EXPENSES)
    average_of_month = 0
    average_of_year = 0

    if number_of_expenses_this_month > 0:
        average_of_month = round(all_month_expenses / number_of_expenses_this_month, 2)
    if number_of_expenses_year > 0:
        average_of_year = round(year_total_amount / number_of_expenses_year, 2)

    print("\nStatystyki")
    print("Suma miesięcznych wydatków [zł]: ", all_month_expenses)
    print("Suma wszystkich wydatków [zł]: ", year_total_amount)
    print("Średnia wydatków danego miesiąca [zł]: ", average_of_month)
    print("Średnia wydatków wszystkich miesięcy [zł]: ", average_of_year)


def categories():
    file = 'category.txt'

    while True:
        print()
        print("0. Powrót do poprzedniego menu")
        print("1. Wyświetl kategorie")
        print("2. Dodaj kategorię")
        print("3. Usuń kategorię")

        try:
            choice = int(input("Wybierz opcję: "))
        except ValueError:
            print("Prawdopodobnie wprowadziłeś złe dane. Spróbuj jeszcze raz.")
            continue
        if choice < 0 or choice > 3:
            print("Podaj liczbę z przedziału [0-3] odpowiadającą odpowiedniemu miesiącu.")

        if choice == 0:
            break
        if choice == 1:
            with open(file) as category:
                content = category.readlines()
            print("\nZapisane kategorie: ")
            for cat in content:
                print(cat.strip())

        elif choice == 2:
            insert_category_name = input("Podaj nazwę kategorii: ")
            with open(file, 'a') as write_category:
                write_category.write(str(insert_category_name.title()) + "\n")

        elif choice == 3:
            remove_category_name = input("Podaj nazwę kategorii którą chcesz usunąć: ")
            with open(file) as category:
                content = category.readlines()
            for cat in content:
                if cat.strip() == remove_category_name:
                    content.remove(cat)
            with open(file, 'w') as category:
                for cat in content:
                    category.write(str(cat.title()))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        print()
        while True:
            try:
                month = int(input("Podaj miesiąc [1-12]: "))
            except ValueError:
                print("Prawdopodobnie wprowadziłeś złe dane. Spróbuj jeszcze raz.")
                continue
            if month < 1 or month > 12:
                print("Podaj liczbę z przedziału [1-12] odpowiadającą odpowiedniemu miesiącu.")
            else:
                break

        while True:
            print()

            for key, value in MONTHS.items():  # Wyświetlanie wybranego miesiąca
                if month == key:
                    print("Miesiąc ", value)

            print("0. Powrót do wyboru miesiąca")
            print("1. Wyświetl wszystkie wydatki")
            print("2. Dodaj wydatek")
            print("3. Kategorie")
            print("4. Statystyki")
            print("5. Zakończenie programu")
            print()

            try:
                 choice = int(input("Wybierz opcję: "))
            except ValueError:
                print("Prawdopodobnie wprowadziłeś złe dane. Spróbuj jeszcze raz.")
                continue
            if choice < 0 or choice > 5:
                print("Podaj liczbę z przedziału [0-5] odpowiadającej opcji menu.")

            if choice == 0:
                break
            elif choice == 1:
                show_expenses(month)
            elif choice == 2:
                add_expense(month)
            elif choice == 3:
                categories()
            elif choice == 4:
                show_stats(month)
            elif choice == 5:
                sys.exit()




