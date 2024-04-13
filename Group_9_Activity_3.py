import csv
def loading_data(path):
        with open(path, "r") as file:
            print("File exists.")
            print("Loading file…")
            print("File successfully loaded!\n")
            loaded_file = csv.reader(file)
            for data in loaded_file:
                for index in range(len(data)):
                    print('|'+data[index] + " "* (len("Sequence Boardgame ") - len(data[index]))+"|", end="")
                print()
            file.seek(0)
            names =[]
            for data in loaded_file:
                print("You have",len(data),"columns. These are: ")
                i = 1
                for name in data:
                    print(str(i)+'. '+name.strip())
                    names.append(name.strip())
                    i+=1
                return names


def load_column(path,column):
    with open(path, "r") as file:
        loaded_file = csv.reader(file)
        row=1
        for data in loaded_file:
            print(str(row)+'. '+data[int(column)-1])
            row+=1
        file.seek(0)
        next(loaded_file)
        data_values=[]
        for data in loaded_file:
            value = data[int(column)-1].strip()
            data_values.append(value)
        return(data_values)

def checking_data(path,column):
    with open(path,'r') as file:
        csv_r = csv.reader(file)
        next(csv_r)
        list = []
        for data in csv_r:
            list.append(data[int(column)-1].strip())
        for value in list:
            if value != '':
                try:
                    int(value)
                    isnumeric = 'True'
                except ValueError:
                    isnumeric = 'False'
            elif value == '':
                continue    
        return isnumeric

def clean_and_prepare(lst):
    list1 =[]
    empty_value = []
    index =0
    for value in lst:
        if value == "":
            empty_value.append(index)
            list1.append(value)
        else:
            list1.append(float(value))
        index+=1
    if empty_value !=[]:
        print("Your chosen column has empty value at: ")
        for i in empty_value:
            print('\tRow',i+2)
    return list1

def average(lst):
    n=len(lst)
    sum = 0
    for i in lst:
        try:
            sum = sum + float(i)
        except ValueError:
            continue
    average = sum/n
    return average

def minimum(list):
  
    smallest = list[0]
    for element in list:
        if smallest > element:
            smallest = element
        return smallest

def maximum(list):
    largest = list[0]
    for element in list:
        if largest < element:
            largest = element
        return largest
    
def replacing_avg(list):
    index = 0
    for value in list:
        if value == '':
            list[index] = average(list)
        index+= 1
    return list


def replacing_maximum(list):
    index = 0
    for value in list:
        if value == '':
            list[index] = maximum(list)
        index+= 1
    return list


def replacing_minimum(list):
    index = 0
    for value in list:
        if value == '':
            list[index] = minimum(list)
        index+= 1
    return list


def insertion_sort_ascend(list):
    for i in range(0,len(list)):
        j=i
        while j>0 and float(list[j-1]) > float(list[j]):
            list[j-1],list[j] = list[j],list[j-1]
            j-=1
    return list
def insertion_sort_descend(list):
    for i in range(0,len(list)):
        j=i
        while j>0 and float(list[j-1]) < float(list[j]):
            list[j-1],list[j] = list[j],list[j-1]
            j-=1
    return list

def visualization(list):
    for i in list:
        if int(i)<100:
            value= int(i)//5 + 1
        elif int(i)>=100:
            value=20
        bar="*"*value
        
        print(bar)
def main():
    print("""=========================================================================
Welcome to Data Analysis CLI
=========================================================================
Program stages:
1. Load Data 
2. Clean and prepare data
3. Analyse Data
4. Visualize Data"""
) 
    print('##############################################################################')
    print('Stage 1: Load Data ')
    path = input('Enter the path of your csv file: ') 
    while True:    
        try:  
            my_columns = loading_data(path)
            choice = ''
            for i in my_columns:
                choice+=i+'/'
            while True:
                column = input('Which column do you want to choose for the preparation stage? '+choice+' ' ).lower()
                column_num=0
                for name in my_columns:
                    column_num+=1
                    if name.lower() == column:
                        break
                is_numeric = checking_data(path,column_num)
                if is_numeric == 'False':
                    print("You have chosen a non numeric column ")
                    continue
                elif is_numeric == 'True':
                    data =load_column(path,column_num)
                else:
                    print('Input error! Please try again ')
                    continue
                print(data)
                print('##############################################################################')
                print('Stage 2: Clear and prepare data')
                data2 =clean_and_prepare(data)
                while True:
                    replace = input("""What do you want to do about the empty value? 
                                Do you want to replace with:
                                1. Average value
                                2. Maximum value
                                3. Minimum value 
                                Please choose one option. 1/2/3: """)
                    if replace == '1':
                        replaced = replacing_avg(data2)
                        print('Empty values are replaced by average value which is',average(data2))
                    elif replace == '2':
                        replaced = replacing_maximum(data2)
                        print('Empty values are replaced by maximum value which is',maximum(data2))
                    elif replace == '3':
                        replaced = replacing_minimum(data2)
                        print('Empty values are replaced by minimum value which is',minimum(data2))
                    else:
                        print("Input error. Please try again. ")
                        continue
                    break
                print(replaced)
                while True:
                    print('##############################################################################')
                    print('Stage 3: Analyse Data')
                    sort_choice = input("""Do you want to sort your data in 
                                    1. Ascending order 
                                    2. Descending order 
                                    Please choose one option 1/2: """)
                    if sort_choice == '1':
                        sorted = insertion_sort_ascend(replaced)
                    elif sort_choice == '2':
                        sorted = insertion_sort_descend(replaced)
                    else:
                        print("Input error. Please try again. ")
                        continue
                    break
                print('Here is your sorted data\n',sorted)
                print('##############################################################################')
                print('Stage 4: Visualise Data')
                print('Column: ',column)
                print('Legend: each * represents 5 units')

                visualization(sorted)
                print('Visualisation completed!')
                repeat = input("Do you want to go over to another numerical columns: yes/no: ").lower()
                if repeat == 'yes':
                    continue
                elif repeat == 'no':
                    break
                else:
                    print("Input Error ")
                    repeat = input("Do you want to go over to another numerical columns: yes/no: ").lower()
            restart = input("Do you want to start the program again from the first stage? yes/no: ").lower()
            if restart == 'yes':
                continue
            elif restart == 'no':
                print('Program is closed! ')
                print('Thank you and good bye!')
                break
            else:
                print("Input Error ")
                restart = input("Do you want to start the program again from the first stage? yes/no: ").lower()
                if restart == 'yes':
                    path = input('Enter the path of your csv file: ')
                elif restart == 'no':
                    break 
                else:
                    print('Input error ')
                    restart = input("Do you want to start the program again from the first stage? yes/no: ").lower()
        except FileNotFoundError:
            print('File does not exist ')
            path = input('Enter the path of your csv file: ')

if __name__ == '__main__':
    main()