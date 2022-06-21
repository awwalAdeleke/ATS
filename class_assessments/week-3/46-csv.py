import csv
from email import header

# with open("file.csv", "r") as file:
#     handler = csv.reader(file)
#     for row in handler:
#         print(row)


# with open("newline.csv", "a") as file:
#     handler = csv.writer(file)
#     handler.writerow(["big-boy" , "Theo" , "Marcus"])

# with open("file.csv", "r") as file:
#     handler = csv.DictReader(file)
#     for row in handler:
#         print(row["First_name"])

with open('newerline.csv', 'w') as file:
    header = ["Last_name", "First_name"]
    handler = csv.DictWriter(file, fieldnames=header)
    handler.writeheader()
    handler.writerow({"Last_name": "Alalade","First_name": "Aderoju"})