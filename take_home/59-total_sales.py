import sys
import numpy as np


record = [
    [34,56,87,89,0],
    [45,56,90,79,0],
    [67,34,84,94,0],
    [90,45,63,47,0],
    [23,45,90,95,0],
    [0,0,0,0,0]]


def total_sales_person():
    sales = np.array(record[0])
    for i in range(1, len(record) - 1):
        sales += record[i]
    record[5] = list(sales)

    return record[5][:-1]

def total_sales_each_person(sales_person_num:int):
    sales = total_sales_person()
    return sales[sales_person_num - 1]

def total_sales_product():
    for i in range(len(record) - 1):
        record[i][-1] = sum(record[i][0:-1])
    return

def total_sales_each_product(product_num:int):
    total_sales_product()
    return record[product_num - 1][-1]

def record_table():
    response = input("Click 1 or 2 or 3 or 4\n\
        1. Summarize total sales by salesperson\n\
        2. Summarize total sales by each salesperson\n\
        3. Summarize total sales by product\n\
        4. Print in tabular form, the records\n")
    if response == "1":
        return total_sales_person()
    elif response == "2":
        sales_person_num = int(input("Enter the salesperson's number: "))
        return total_sales_each_person(sales_person_num)
    elif response == "3":
        product_num = int(input("Enter the product number: "))
        return total_sales_each_product(product_num)
    elif response == "4":
        return f"{'Salesperson'.center(60, '=')}\n\n\
                        {1}   |  {2}   |  {3}   |  {4}   |  {5}\n\n\
            Product1:   {record[0][0]}  |  {record[0][1]}  |  {record[0][2]}  |  {record[0][3]}  |  {total_sales_each_product(1)}\n\
            Product2:   {record[1][0]}  |  {record[1][1]}  |  {record[1][2]}  |  {record[1][3]}  |  {total_sales_each_product(2)}\n\
            Product3:   {record[2][0]}  |  {record[2][1]}  |  {record[2][2]}  |  {record[2][3]}  |  {total_sales_each_product(3)}\n\
            Product4:   {record[3][0]}  |  {record[3][1]}  |  {record[3][2]}  |  {record[3][3]}  |  {total_sales_each_product(4)}\n\
            Product5:   {record[4][0]}  |  {record[4][1]}  |  {record[4][2]}  |  {record[4][3]}  |  {total_sales_each_product(5)}\n\
            Totals:     {total_sales_each_person(1)} |  {total_sales_each_person(2)} |  {total_sales_each_person(3)} |  {total_sales_each_person(4)} |\n"
    else:
        print("You have clicked an invalid option! The system will now shut down!")
        sys.exit()


if __name__ == '__main__':
    print(record_table())

# def sales():
#     sales1 = []
#     for i in range(len(record) - 1):
#         sales1.append(record[i][0])
#     sales_1 = sum(sales1)

#     sales2 = []
#     for i in range(len(record) - 1):
#         sales2.append(record[i][1])
#     sales_2 = sum(sales2)

#     sales3 = []
#     for i in range(len(record) - 1):
#         sales3.append(record[i][2])
#     sales_3 = sum(sales3)

#     sales4 = []
#     for i in range(len(record) - 1):
#         sales4.append(record[i][3])
#     sales_4 = sum(sales4)

#     record[5][0] += sales_1
#     record[5][1] += sales_2
#     record[5][2] += sales_3
#     record[5][3] += sales_4





