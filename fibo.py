def main():
    a, b = 0, 1
    while b < 30:
        print(b)
        # a, b = b, a + b
        a_old = a
        a = b
        b = a_old + b


if __name__ == "__main__":
    main()
