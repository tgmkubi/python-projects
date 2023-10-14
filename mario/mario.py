def pyramid():
    height = int(input("Height: "))
    while height > 0:
        for brick in range(1,height + 1):
            print(f"{' ' * (height - 1)}{'#' * brick}  {'#' * brick}")
            height = height - 1

pyramid()