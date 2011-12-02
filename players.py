#-------------------------------------------------------------------------------
# Name:         players
# Purpose:      This contains the code to create and manage families.
#
# Author:       Nick Birney
#
# Created:      2 Dec. 2011
# Updated:      2 Dec. 2011
# Copyright:   (c) Nick Birney 2011
# Licence:     GNU General Public License (see text file named COPYING)
#-------------------------------------------------------------------------------



class character:
    """An individual family member.

    Member Variables:
        name            (str)
        age             (int)
        gender          (str)
        isFamilyLeader  (boolean)
        description     (str)

    Methods:
        payCharacter(playerName (character),amount (int)) -> amount left, -1 if insufficient funds
        payFamily(familyName (family), amount(int)) -> amount left, -1 if insufficient funds
        """

    name            =   ""
    age             =   0
    gender          =   "male"
    isAlive         =   False
    description     =   ""
    money           =   0

    def __init__(self):
        """Initializes and returns a new FamilyMember object.

            """
        self.name = ""
        self.age  = 0
        self.gender = "male"
        self.isAlive = False
        self.description = ""
        self.money = 0

    def payCharacter(self,playerName,amount):
        if (amount > money):
            return -1
        else:
            self.money = self.money - amount
            playerName.money = playerName.money + amount
            return self.money

    def payFamily(self,familyName,amount):
        if (amount > money):
            return -1
        else:
            self.money = self.money - amount
            familyName.money = familyName.money + amount
            return money



#-------------------------------------------------------------------------------

class family:
    """The family unit.

        Member Variables:
            name            (str)
            members         (["character" objects])
            treasury        (int)
            leader          ("character" object)

        Methods:
            addMember(character, isLeader (boolean))
            addNewMember(name (str), age (int), gender (str), isAlive (boolean), isLeader(boolean))
            makeLeader(character)
        """
    name    = ""
    members = []
    treasury = 0

    def __init__(self,name):
        self.members = []
        self.name = name

    def addMember(self,character,isLeader):
        self.members.append(character)

        if isLeader == True:
            self.makeLeader(self.members[len(self.members)-1])

    def addNewMember(self,name, age, gender,isAlive,money,isLeader,):
        """Creates a new family member with all of the attributes defined.

            """
        new = character()
        new.name = name
        new.age = age
        new.gender= gender
        new.isAlive = isAlive
        new.money = money

        self.members.append(new)

        del new

        if isLeader == True:
            self.makeLeader(self.members[len(self.members)-1])

    def makeLeader(self,character):
        self.leader = character

    def payCharacter(self,character,amount):
        if (amount > self.treasury):
            return -1
        else:
            self.treasury= self.treasury - amount
            character.money = character.money + amount
            return self.treasury

    def payFamily(self,family,amount):
        if (amount > self.treasury):
            return -1
        else:
            self.treasury = self.treasury- amount
            family.treasury = family.treasury + amount
            return self.treasury

#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()