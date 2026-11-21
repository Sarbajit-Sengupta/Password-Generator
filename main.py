import secrets

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!@$%&*"


def positive_integer(prompt, minimum=1):
    value = int(input(prompt))
    if value < minimum:
        raise ValueError("Enter a positive whole number.")
    return value


def main():
    while True:
        try:
            length = positive_integer("What length would you like your password to be: ")
            count = positive_integer("How many passwords would you like: ", minimum=0)
        except (EOFError, KeyboardInterrupt):
            return
        except ValueError:
            print("Enter positive whole numbers for length; count must be nonnegative.")
            continue
        for _ in range(count):
            password = ''.join(secrets.choice(chars) for _ in range(length))
            print("Here is your password :", password)


if __name__ == '__main__':
    main()
