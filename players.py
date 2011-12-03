#-------------------------------------------------------------------------------
# Name:         players
# Purpose:      This contains the code to create and manage families.
#
# Author:       Nick Birney
#
# Created:      2 Dec. 2011
# Updated:      3 Dec. 2011
# Copyright:   (c) Nick Birney 2011
# Licence:     GNU General Public License (see text file named COPYING)
#-------------------------------------------------------------------------------

import sys

class character:
    """An individual family member.

    Member Variables:
        name            (str)
        age             (int)
        gender          (str)
        isAlive         (boolean)
        description     (str)
        money           (int)

    Methods:
        payCharacter(playerName (character),amount (int)) -> amount left, -1 if insufficient funds
        payFamily(familyName (family), amount(int)) -> amount left, -1 if insufficient funds
        """

    def __init__(self):
        self.name = ""
        self.age  = 0
        self.gender = "male"
        self.description = ""
        self.money = 0

    def payCharacter(self,playerName,amount):
        if (amount > self.money):
            return -1
        else:
            self.money = self.money - amount
            playerName.money = playerName.money + amount
            return self.money

    def payFamily(self,familyName,amount):
        if (amount > self.money):
            return -1
        else:
            self.money = self.money - amount
            familyName.treasury = familyName.treasury + amount
            return self.money



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
            addNewMember(name (str), age (int), gender (str), money(int), isAlive (boolean), isLeader(boolean))
            makeLeader(character)
            payCharacter(playerName (character), amount (int)) -> amount left, -1 if insufficient funds
            payFamily(familyName (family), amount (int)) -> amount left, -1 if insufficient funds
            getMemberByName(name (str)) -> character whose name matches, character with the name "ERROR" if it was not found
        """

    def __init__(self,name,money):
        self.members = []
        self.deadMembers = []
        self.name = name
        self.treasury = money

    def addMember(self,character,isLeader):
        self.members.append(character)

        if isLeader == True:
            self.makeLeader(self.members[len(self.members)-1])

    def addNewMember(self,name, age, gender,money,isAlive,isLeader,):
        new = character()
        new.name = name
        new.age = age
        new.gender= gender
        new.money = money

        if isAlive == True:
            self.members.append(new)
        else:
            self.deadMembers.append(new)

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

    def killMember(self,member):
        self.deadMembers.append(member) 
        
        return self.members.pop(self.members.index(member))

    def getMemberByName(self,name):
        for x in self.members:
            if x.name == name:
                return x

        error = character()
        error.name = "ERROR"
        return error



#-------------------------------------------------------------------------------

def main():
    newFam = family("Birney",500000)
    newFam.addNewMember("Nick",22,"male",200,True,False)
    newFam.addNewMember("Mike",57,"male",2000,True,True)
    newFam.addNewMember("Jess",18,"female",100,True,False)
    print(newFam.getMemberByName("Jess").name)
    newFam.payCharacter(newFam.getMemberByName("Mike"),5000)
    newFam.getMemberByName("Nick").payFamily(newFam,100)
    newFam.getMemberByName("Jess").payCharacter(newFam.getMemberByName("Nick"),50)
    print(newFam.treasury)
    print(newFam.getMemberByName("Nick").money)
    print(newFam.getMemberByName("Mike").money)
    print(newFam.getMemberByName("Jess").money)
    exit()

if __name__ == '__main__':
    main()
