from abc import ABC, abstractmethod

import turtle
"""Make a MII"""
class MII:

    def __init__(self, ID, gender):
        "(MII, int, str) -> None"
        self.ID = ID
        self.MIIInfo = self.MIIInfo()
        self.BodyFeatures = self.BodyFeatures()
    
    def getID(self):
        "(MII) -> int"
        return self.ID

    def __str__(self):
        "(MII) -> str"
        return "I am a " + self.gender + ". "

    def __repr__(self):
        "(MII) -> str"
        return "(" + str(self.ID) + ", " + self.gender + ")"
    
    class MIIInfo:

        def __init__(self):
            "(MII.MIIInfo) -> None)"
            self.firstName = None
            self.lastName = None
            self.birthday = None
            
        def setInfo(self, firstName, lastName , birthday):
            "(MII.MIIInfo, str, str, tpl(int, int, int)) -> None)"
            self.firstName = firstName
            self.lastName = lastName
            self.birthday = birthday

       

        def getFirstName(self):
            "(MII.MIIInfo) -> str)"
            return self.firstName

        def getLastName(self):
            "(MII.MIIInfo) -> str)"
            return self.lastName

        def changeLastName(self, newLastName):
            "(MII.MIIInfo, str) -> None)"
            self.lastName = newLastName

        def getBirthday(self):# birthday is a tuple(month, day, year)
            "(MII.MIIInfo) -> tpl(int, int, int))"
            return self.birthday

        def getBirthdayString(self):
            "(MII.MIIInfo) -> str)"
            birthdayString = ""
            for i in range(len(self.birthday)):
                if i != len(self.birthday) -1:
                    birthdayString+=str(self.birthday[i]) + "/"

                else:
                    birthdayString+=str(self.birthday[i])

            return birthdayString

        def __str__(self):
            "(MII.MIIInfo) -> str)"
            return "My name is " + self.firstName + " " + self.lastName + " and my birthday is, " + self.getBirthdayString()

        def __repr__(self):
            "(MII.MIIInfo) -> str)"
            return "(" + self.firstName + ", " + self.lastName + ", " + str(self.birthday) + ")"

    class BodyFeatures:

        def __init__(self):
            "(MII.BodyFeatures) -> None)"
            self.colours = None
            self.height = None
            self.width = None
            self.shoeSize = None
            

        def setBodyFeatures(self, colours = {}, height = 160, width = 70, shoeSize = 30):
            "(MII.BodyFeatures, dict, int, int, int) -> None)"
            #Width IS 50-200
            #Height IS 50-200
            #shoesize = (self.shoeSize//2.5+24)//3
            self.colours = colours
            self.height = height
            self.width = width
            self.shoeSize = shoeSize

        def getDimensions(self):#abstract
            "(MII.BodyFeatures) -> abstract None)"
            pass

       

        def draw(self):#abstract
            "(MII.BodyFeatures) -> None)"
            pass

        def __str__(self):
            "(MII.BodyFeatures) -> str)"
            return "I am " + str(self.height) + " centimetres tall and " + str(self.width) + " centimetres fat."

        def __repr__(self):
            "(MII.BodyFeatures) -> str)"
            return "(" + str(self.colours) + ", " + str(self.height) + ", " + str(self.width) + ", " + str(self.shoeSize) + ")"
            
    

#class girl
class Girl(MII):
    def __init__(self, ID, gender):
        "(Girl) -> None)"
        self.gender = "girl"
        super().__init__(ID, gender)
        self.GirlInfo = self.GirlInfo()
        self.GirlBodyFeatures = self.GirlBodyFeatures()

    def getGender(self):
        "(Girl) -> str)"
        return self.gender

    def __repr__(self):
        "(Girl) -> str)"
        return "Girl" + super().__repr__()
            
    class GirlInfo(MII.MIIInfo):
        "(Girl,GirlInfo) -> None)"
        def __init__(self):
            super().__init__()

        def __repr__(self):
            "(Girl.GirlInfo) -> str)"
            return "GirlInfo" + super().__repr__()

    class GirlBodyFeatures(MII.BodyFeatures):
        def __init__(self):
            "(Girl.GirlBodyFeatures) -> None)"
            super().__init__()

        def __repr__(self):
            "(Girl.GirlBodyFeatures) -> str)"
            return "GirlBodyFeatures" + super().__repr__()

        

#class boy
class Boy(MII):
    def __init__(self, ID, gender):
        "(Boy) -> None)"
        self.gender = "boy"
        super().__init__(ID, gender)
        self.BoyInfo = self.BoyInfo()
        self.BoyBodyFeatures = self.BoyBodyFeatures()

    def getGender(self):
        "(Boy) -> str)"
        return self.gender

    def __repr__(self):
        "(Boy) -> str)"
        return "Boy" + super().__repr__()
            
    class BoyInfo(MII.MIIInfo):
        "(Boy.BoyInfo) -> None)"
        def __init__(self):
            super().__init__()

        def __repr__(self):
            "(Boy.BoyInfo) -> str)"
            return "BoyInfo" + super().__repr__()

    class BoyBodyFeatures(MII.BodyFeatures):
        def __init__(self):
            "(Boy.BoyBodyFeatures) -> None)"
            super().__init__()

        def __repr__(self):
            "(Boy.BoyBodyFeatures) -> str)"
            return "BoyBodyFeatures" + super().__repr__()

        def draw(self): 
            h = self.height*2
            w = self.width
            c = self.colours
            s = self.shoeSize
            x = 0
            y = 200

            t = turtle.Turtle()
            t.penup()

            t.goto(x,y)

            t.pendown()

            self.drawBody(t, s)

        def drawBody(self, t, s):
            t.circle(s*2)
#class other

b = Boy(0,  1)
b.BoyBodyFeatures.setBodyFeatures({}, 180, 200, 26)

