'''Доробіть консольного бота помічника з попереднього домашнього завдання та
додайте обробку помилок за допомоги декораторів.'''
# З добавленням цього дерокатора наші функції трішки скоротились в коді, а саме
# з них зникли перевірки if/else, тепер ці перевірки не використовуються щоб уникнути помилок
# функції йдуть на помилки, а декоратор їх охоплює, у великому коді це було б дуже зручно
def input_error(func):
    '''Декоратор який обробляє помилки ValueError, KeyError, IndexError'''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
# Пробуємо викликати нашу фукнцію, якщо кидає помилку, перехоплюємо
        except (ValueError, IndexError):
            return "Give me phone and name pls."
        except KeyError:
            return "User don't exist"
    return inner

def parse_input(user_input):
    '''Ця функція обробляє введене користувачем значення'''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@ input_error # обгортаємо наші функції
def add_contact(args, contacts):
    '''Ця функція додає користувача в книгу'''
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@ input_error
def change_contact(args, contacts):
    '''Ця функція змінює користувача в книзі'''
    name, phone = args
    if name not in contacts: # тут потрібно явно перевірити, інакше не працюватиме
        raise KeyError
    contacts[name] = phone
    return "Contact changed."

@ input_error
def get_user_phone(args, contacts):
    '''Ця функція витягує номер користувача з книги'''
    if len(args) > 1:
        # підіймає IndexError якщо запит завеликий, тобто є щось окрім ім'я користувача
        raise IndexError
    return contacts[args[0]]

def main():
    '''Це головна функція програми і сам консольний бот, який запускається тільки
    з цього файлу і працює доки не отримає команди про вихід'''
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(get_user_phone(args, contacts))
        elif command == 'all':
            for i, v in contacts.items():
                print(i, v)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
