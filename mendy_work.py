import math

def main():
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