def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("ゼロ除算!")
    else:
        print("答えは ", result)
    finally:
        print("finally 節実行中")


if __name__ == "__main__":
    divide(2, 0)
