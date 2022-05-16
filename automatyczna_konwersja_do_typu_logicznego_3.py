list = ['load data', 'export data', 'analyze & predict']
a = input("""Choise a number: 
1 - load data
2 - export data
3 - analyze & predict
Select option above or press enter to exit: """)
if a == True:
    if a == 1:
        print("loading data...")
    elif a == 2:
        print("exporting data...")
    elif a == 3:
        print("analyze & predict")
    else:
        print("Must be a number 1-3!")
else:
    print("END")
