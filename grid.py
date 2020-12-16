
def get_location(n, m): 
  
    if (n > m): 
        if (m % 2 == 0): 
            print("U"); 
        else: 
            print("D"); 
    else: 
        if (n % 2 == 0): 
            print("L"); 
        else: 
            print("R"); 


option_repeat = True
while(option_repeat):
    test_cases = input("Please, input total test cases: ")
    try:
        test_cases = int(test_cases)
        option_repeat = False
    except Exception as e:
        print("-----> Please only numbers <-----")
        print("\n")
     

for test in range(test_cases):
    rows = input("Please enter the number of rows (N): ")
    rows = int(rows)
    columns = input("Please enter the number of columns (M): ")
    columns = int(columns)
    get_location(rows, columns)