def greeting():
    answer = input("Greeting: ").lower().strip()

    if "hello" in answer and answer.startswith("hello"):
        print("$0")
    elif answer.startswith("h"):
        print("$20")
    else:
        print("$100")

greeting()