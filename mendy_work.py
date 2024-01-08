import math

def main():
    """
    this is a function sin, cos and tan. It is make the value of sin cos and type with the degree that you input
    :return:
    """
    global result
    text = e.get()
    operation = text[0:3]
    angle = int(text[3: -1])
    if operation == "sin":
        result = math.sin(angle)
    elif operation == "cos":
        result = math.cos(angle)
    elif operation == "tan":
        result = math.tan(angle)
    e.delete(0, END)
    e.insert(0, str(result))

if __name__ == "__main__":
    main()