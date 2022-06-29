import datetime

list_profiles = {"aadeleke@afexnigeria.com": {"f_name" : "Awwal", "l_name" : "Adeleke", "date": {"day": 20, "month": 5}, "attendance": 11, "height": 190, "weight": 70, "age": 23}, 
                 "aadekunle@afexnigeria.com": {"f_name" : "Abraham", "l_name" : "Adekunle", "date": {"day": 25, "month": 3}, "attendance": 11, "height": 183, "weight": 65, "age": 23},
                 "atajudeen@afexnigeria.com": {"f_name" : "Abdulwali", "l_name" : "Tajudeen", "date": {"day": 16, "month": 7}, "attendance": 11, "height": 193, "weight": 75, "age": 20},
                 "aadeyeye@afexnigeria.com": {"f_name" : "Adebusola", "l_name" : "Adeyeye", "date": {"day": 10, "month": 4}, "attendance": 10, "height": 178, "weight": 55, "age": 21},
                 "yoyedele@afexnigeria.com": {"f_name" : "Yusuff", "l_name" : "Oyedele", "date": {"day": 14, "month": 8}, "attendance": 9, "height": 180, "weight": 63, "age": 26},
                 "bbalogun@afexnigeria.com": {"f_name" : "Basheer", "l_name" : "Balogun", "date": {"day": 16, "month": 7}, "attendance": 10, "height": 180, "weight": 60, "age": 25},
                 "asalaam@afexnigeria.com": {"f_name" : "Abdullahi", "l_name" : "Salaam", "date": {"day": 2, "month": 1}, "attendance": 11, "height": 172, "weight": 68, "age": 25},
                 "aadeosune@afexnigeria.com": {"f_name" : "Faith", "l_name" : "Adeosun", "date": {"day": 5, "month": 5}, "attendance": 7, "height": 168, "weight": 61, "age": 23},
                 "asharafudeene@afexnigeria.com": {"f_name" : "Ahmad", "l_name" : "Sharafudeen", "date": {"day": 12, "month": 2}, "attendance": 11, "height": 178, "weight": 61, "age": 24},
                 "labisoye@afexnigeria.com": {"f_name" : "Lukman", "l_name" : "Abisoye", "date": {"day": 15, "month": 6}, "attendance": 10, "height": 175, "weight": 62, "age": 23},
                 "togunbiyi@afexnigeria.com": {"f_name" : "Toluwanimi", "l_name" : "Ogunbiyi", "date": {"day": 9, "month": 12}, "attendance": 9, "height": 188, "weight": 81, "age": 24}}

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


class ProfileList:

    def __init__(self, list_profiles, email):
        self.whole = list_profiles
        self.email = email
        self.details = list_profiles[email]
        self.first_name = self.details["f_name"]
        self.last_name = self.details["l_name"]
        self.birth_day = self.details["date"]["day"]
        self.birth_month = self.details["date"]["month"]
        self.attendance = self.details["attendance"]
        self.height = self.details["height"]
        self.weight = self.details["weight"]
        self.age = self.details["age"]

    def add_profile(self, email):
        self.whole[email] = {}
        f_name = input("What is your first name? ")
        l_name = input("What is your last name? ")
        day = int(input("What day were you born? "))
        month = int(input("What month were you born, as a number? "))
        attendance = int(input("How many days did you come for? "))
        height = int(input("How tall are you in cm? "))
        weight = int(input("What is your weight in kg? "))
        age = int(input("How old are you? "))

        date = {"day": day, "month": month}

        self.whole[email]["f_name"] = f_name
        self.whole[email]["l_name"] = l_name
        self.whole[email]["date"] = date
        self.whole[email]["attendance"] = attendance
        self.whole[email]["height"] = height
        self.whole[email]["weight"] = weight
        self.whole[email]["age"] = age

        return self.whole

    def attended(self):
        self.details["attendance"] += 1
        return self.details

    def update_names(self):
        self.details["f_name"] = input("What is the new first name? ")
        self.details["l_name"] = input("What is the new last name? ")
        return self.details

    def list_names(self):
        return "{} {}".format(self.first_name, self.last_name)

    def remove_profile(self):
        del self.whole[self.email]
        return self.whole

    def month(self):
        return months[self.birth_month - 1]

    def group_by_month(self):
        month_group = []
        for i in range(len(months)):
            for email in self.whole:
                if (i+1) == self.whole[email]["date"]["month"]:
                    month_group.append(self.whole[email])
            if month_group != []:                                             #
                print(f"The students born in {months[i]} are {month_group}")  #
            month_group.clear()                                               #
        # return month_group

    def initials(self):
        names = []
        names.append(self.first_name[0] + "." + self.last_name[0] + ".")
        return names

    def bmi(self):
        bmi = (self.weight)/((self.height/100)**2)
        return bmi

    def age_average(self):
        ages = []
        sum = 0
        for email in self.whole:
            ages.append(self.whole[email]["age"])
        for age in ages:
            sum += age
        return sum/len(ages)

    def max_age(self):
        max_age = self.whole["aadeleke@afexnigeria.com"]["age"]
        for email in self.whole:
            if self.whole[email]["age"] > max_age:
                max_age = self.whole[email]["age"]
        return f"{max_age} is the maximum age."

    def min_age(self):
        min_age = self.whole["aadeleke@afexnigeria.com"]["age"]
        for email in self.whole:
            if self.whole["age"] < min_age:
                min_age = self.whole[email]["age"]
        return f"{min_age} is the minimum age."

    def birth_year(self):
        current_year = datetime.date.today().year
        birth_year = current_year - self.age
        return birth_year

me = ProfileList(list_profiles, "togunbiyi@afexnigeria.com")
print(me.group_by_month())