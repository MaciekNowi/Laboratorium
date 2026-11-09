x=input("Podaj 1 liczbe: ")
operator=input("Podaj opeartor(+ - * /) ")
y=input("Podaj 2 liczbe: ")
x_float=float(x)
y_float= float(y)

if operator=="+":
     print(x_float+y_float)
if operator== "-":
    print(x_float-y_float)
if operator == "*":
     print(x_float*y_float)
if operator == "/":
    if y_float== 0:
        print("Nie mozna dzielic przez 0")
    else:
        print(x_float/y_float)
