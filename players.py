#-------------------------------------------------------------------------------
# Name:         players
# Purpose:      This contains the code to create and manage families.
#
# Author:      Nick Birney
#
# Created:     2 Dec. 2011
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
        """

    name            =   ""
    age             =   0
    gender          =   "male"
    isAlive         =   False

    def __init__(self):
        """Initializes and returns a new FamilyMember object.

            """
        self.name = ""
        self.age  = 0
        self.gender = "male"
        self.isAlive = False


#-------------------------------------------------------------------------------

class family:
    """The family unit.

        """
    name    = ""
    members = []

    def __init__(self,name):
        self.members = []
        self.name = ""

    def addMember(self,character,isLeader):
        self.members.append(character)

        if isLeader == True:
            self.makeLeader(self.members[len(self.members)-1])

    def addNewMember(self,name, age, gender,isAlive,isLeader):
        """Creates a new family member with all of the attributes defined.

            """
        new = character()
        new.name = name
        new.age = age
        new.gender= gender
        new.isAlive = isAlive

        self.members.append(new)

        if isLeader == True:
            self.makeLeader(self.members[len(self.members)-1])

    def makeLeader(self,character):
        self.leader = character

#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()