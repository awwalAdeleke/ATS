class Time:
    """Time abstract data type (ADT) definition"""

    def __init__( self ):
        """Initializes hour, minute and second to zero"""

        self.hour = 0 # 0-23
        self.minute = 0 # 0-59
        self.second = 0 # 0-59

    def printMilitary( self ):
        """Prints object of class Time in military format"""

        print("%.2d:%.2d:%.2d" % ( self.hour, self.minute, self.second ))

    def printStandard( self ):
        """Prints object of class Time in standard format"""

        standardTime = ""

        if self.hour == 0 or self.hour == 12:
            standardTime += "12:"
        else:
            standardTime += "%d:" % ( self.hour % 12 )

        standardTime += "%.2d:%.2d" % ( self.minute, self.second )

        if self.hour < 12:
            standardTime += " AM"
        else:
            standardTime += " PM"

        print(standardTime)
        
    def tick(self):
        self.second += 1
        if self.second > 59:
            self.minute += 1
            self.second %= 60
        if self.minute > 59:
            self.hour += 1

# time = Time()
# print(time.printStandard())
