list_profiles = [{"f_name" : "Awwal", "l_name" : "Adeleke", "date": {"day": 20, "month": 5}, "attendance": 11, "height": 190, "weight": 70, "age": 23}, 
                 {"f_name" : "Abraham", "l_name" : "Adekunle", "date": {"day": 25, "month": 3}, "attendance": 11, "height": 183, "weight": 65, "age": 23},
                 {"f_name" : "Abdulwali", "l_name" : "Tajudeen", "date": {"day": 16, "month": 7}, "attendance": 11, "height": 193, "weight": 75, "age": 20},
                 {"f_name" : "Adebusola", "l_name" : "Adeyeye", "date": {"day": 10, "month": 4}, "attendance": 10, "height": 178, "weight": 55, "age": 21},
                 {"f_name" : "Yusuff", "l_name" : "Oyedele", "date": {"day": 14, "month": 8}, "attendance": 9, "height": 180, "weight": 63, "age": 26},
                 {"f_name" : "Basheer", "l_name" : "Balogun", "date": {"day": 16, "month": 7}, "attendance": 10, "height": 180, "weight": 60, "age": 25},
                 {"f_name" : "Abdullahi", "l_name" : "Salaam", "date": {"day": 2, "month": 1}, "attendance": 11, "height": 172, "weight": 68, "age": 25},
                 {"f_name" : "Faith", "l_name" : "Adeosun", "date": {"day": 5, "month": 5}, "attendance": 7, "height": 168, "weight": 61, "age": 23},
                 {"f_name" : "Ahmad", "l_name" : "Sharafudeen", "date": {"day": 12, "month": 2}, "attendance": 11, "height": 178, "weight": 61, "age": 24},
                 {"f_name" : "Lukman", "l_name" : "Abisoye", "date": {"day": 15, "month": 6}, "attendance": 10, "height": 175, "weight": 62, "age": 23},
                 {"f_name" : "Toluwanimi", "l_name" : "Ogunbiyi", "date": {"day": 9, "month": 12}, "attendance": 9, "height": 188, "weight": 81, "age": 24}]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


# # FUNCTION TO ADD PROFILE TO THE CLASS LIST
def add_profile():
    new_profile = {}
    f_name = input("What is your first name? ")
    l_name = input("What is your last name? ")
    day = int(input("What day were you born? "))
    month = int(input("What month were you born, as a number? "))
    attendance = int(input("How many days did you come for? "))
    height = int(input("How tall are you in cm? "))
    weight = int(input("What is your weight in kg? "))
    age = int(input("How old are you? "))
    
    new_profile["f_name"] = f_name
    new_profile["l_name"] = l_name
    new_profile["day"] = day
    new_profile["month"] = month
    new_profile["attendance"] = attendance
    new_profile["height"] = height
    new_profile["weight"] = weight
    new_profile["age"] = age
    
    list_profiles.append(new_profile)
    
# add_profile()

# FUNCTION TO INCREASE ATTENDANCE
def attended(name):
    for i in list_profiles:
        if name.title() == i["f_name"]:
            i["attendance"] += 1
            break
        

# FUNCTION TO UPDATE NAMES
def update_names(name):
    for i in list_profiles:
        if name.title() == i["f_name"]:
            i["f_name"] = input("What is the new first name? ")
            i["l_name"] = input("What is the new last name? ")
            break
# update_names("Awwal")
# print(list_profiles[0])

# FUNCTION TO PRINT LIST OF FULL NAMES
def list_names():
    names = []
    for i in list_profiles:
        names.append(i["f_name"] + " " + i["l_name"])
    return names
# print(list_names())

# FUNCTION TO RETURN NUMBER OF PEOPLE IN THE CLASS
def size():
    return len(list_profiles)

# print(size())

# FUNCTION TO REMOVE PROFILE
def remove_profile(name):
    for i in list_profiles:
        if name.title() == i["f_name"]:
            list_profiles.remove(i)
            break

# remove_profile("Awwal")
# print(list_profiles)

# FUNCTION TO RETURN NAME OF BIRTH OF MONTH
def month(name):
    for i in list_profiles:
        if name.title() == i["f_name"]:
            month_num = i["date"]["month"]
            return months[month_num - 1]

print(month("Awwal"))

# # FUNCTION TO GROUP PROFILES BY MONTH
# def month_group():
#     new_class = []
#     class_months = []
#     for i in list_profiles:
#         class_months.append(i["date"]["month"])
#     for i in range(len(class_months)):
#         for j in range(len(months)):
#             if class_months[i] == months[j].index:
#                 new_class.append(list_profiles[i])
#     return new_class

# print(month_group())




# # FUNCTION TO RETURN A LIST OF INITIALS
def initials():
    names = []
    for i in list_profiles:
        names.append(i["f_name"][0] + "." + i["l_name"][0] + ".")
    return names



# FUNCTION TO CALCULATE BMI
def bmi(name):
    for i in list_profiles:
        if name.title() == i["f_name"]:
            bmi = (i["weight"])/((i["height"]/100)**2)
            return bmi

# # FUNCTION TO FIND AVERAGE AGE
def age_average():
    ages = []
    sum = 0
    for i in list_profiles:
        ages.append(i["age"])
    for i in ages:
        sum += i
    return sum/len(ages)



# # FUNCTION TO FIND MAX AGE
def max_age():
    max_age = list_profiles[0]["age"]
    for i in list_profiles:
        if i["age"] > max_age:
            max_age = i["age"]
            
    return f"{max_age} is the maximum age."


# # FUNCTION TO FIND MIN AGE
def min_age():
    min_age = list_profiles[0]["age"]
    for i in list_profiles:
        if i["age"] < min_age:
            min_age = i["age"]

    return f"{min_age} is the minimum age."

# # FUNCTION TO CALCULATE BIRTH YEAR OF A PROFILE
def birth_year(name):
    current_year = int(input("What year are we at? "))
    for i in list_profiles:
        if name.title() == i["f_name"]:
            birth_year = current_year - i["age"]
            return birth_year
        
# print(birth_year("Awwal"))

# DESCRIBE THE CLASS IN A FEW WORDS
def describe():
    print(f"The class has {size()} students in the class.")


# describe()
