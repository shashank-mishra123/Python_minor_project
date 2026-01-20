# create the calculator with history saver 

# create the txt file
HISTORY_FILE ="history.txt"

# to show history
def show_history():
    file =open(HISTORY_FILE,'r')
    lines = file.readlines()
    if len(lines)==0:
        print("----- No history found ---")

    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file=open(HISTORY_FILE,'w')
    file.close()
    print("--- history cleared----")

def save_history(equation,result):
    file = open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()


def calculator(user_input):
    parts = user_input.split()
    if len(parts)!=3:
        print(" invalid input")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == '+':
        result= num1+num2
    elif op =='-':
         result= num1-num2
    elif op =='*':
         result= num1*num2
    elif op =='/':
        if num2==0:
            print("-- dont input zero ---")
            return
        else:
             result=num1/num2
    else:
        print("-- dont be using another operands")

    if  int(result)==result:
        result=int(result)
    print("Result :",result)

    save_history(user_input,result)


def main():
    print("---Hello this is a calculator----")
    while True:
        user_input = input("Enter the condition like calculation ,save_ history ,clear_history , exit\n (+,-,*,/)")
        if user_input=='exit':
            print("--bye---")
            break
        elif user_input=='show_history':
            save_history()
        elif user_input=='clear_history':
            clear_history()
        else:
            calculator(user_input)

main()
