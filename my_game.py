"""
classes for game
"""
from random import choice

class Room:
    """
    room
    """
    def __init__(self, name: str):
        """
        init
        __name - name of the room
        __links - rooms that are linked with the room
                  the list consists of (Room element, direction)
        character - character that lives in the room
        __item - item that is in the room
        """
        self.__name = name
        self.__links = {}
        self.character = None
        self.__item = None

    def set_description(self, description: str) -> None:
        """
        sets room's description that will be visible for user
        """
        self.__description = description

    def link_room(self, room, direction: str) -> None:
        """
        links rooms
        """
        self.__links[direction] = room

    def set_character(self, character):
        """
        sets characters to room
        """
        self.character = character

    def set_item(self, item):
        """
        sets item to room
        """
        self.__item = item

    def get_details(self):
        """
        prints room's details
        """
        print(self.__name)
        print('--------------------')
        print(self.__description)
        for direction, room in self.__links.items():
            print(f"The {room.__name} is {direction}")

    def get_character(self):
        """
        gets character that is in the room
        """
        return self.character

    def get_item(self):
        """
        gets item that is in the room
        """
        return self.__item

    def move(self, direction):
        """
        moves character to another room

        returns Room item that determines the room to which character has mooved
        """
        return self.__links[direction]

class Character:
    """
    character
    """
    defeated = 0

    def __init__(self, name, description):
        """
        init
        """
        self.__name = name
        self.__description = description

    def set_conversation(self, conversation):
        """
        sets enemie's conversation
        """
        self.__conversation = conversation

    def set_weakness(self, weakness):
        """
        sets enemie's weakness
        """
        self.__weakness = weakness

    def describe(self):
        """
        prints characters description
        """
        print(f"{self.__name} is here!")
        print(self.__description)

    def talk(self):
        """
        prints characters conversation
        """
        print(f"[{self.__name} says]: {self.__conversation}")

    def interact(self, weapon: str):
        """
        returns True if weapon is a weakness
        """
        if weapon == self.__weakness:
            Character.defeated += 1
            return True
        return False

    def get_defeated(self):
        """
        returns number of defreated enemies
        """
        return Character.defeated

    def get_name(self):
        """
        returns characters name
        """
        return self.__name

class Enemy(Character):
    """
    enemy
    """

class Friend(Character):
    """
    friend
    """

class Student(Friend, Character):
    """
    Student
    """
    def interact(self):
        """
        randomly drops something from a pocket
        """
        print("Tell me a joke:")
        joke = input(">")

        if len(joke) < 10:
            print(f"[{self.get_name()}]: Are all of the APPS students so boring?..")

        elif choice([True, True, True, False, False]):
            print(f"[{self.get_name()}]: you have great jokes, like Bohdan Borkivskiy!")
            print(f"{self.get_name()} has just given you a cigarette.")

            cigarette = Item("cigarette")
            cigarette.set_description("Usless piece of paper and dried tobacco.\
But gopniks like it")
            return cigarette
        else:
            print(f"[{self.get_name()}]: Good joke!")
        return None

class Item:
    """
    item
    """
    def __init__(self, name: str):
        """
        init
        """
        self.__name = name

    def set_description(self, description: str):
        """
        sets item's description
        """
        self.__description = description

    def describe(self):
        """
        prints items description
        """
        print(f"A [{self.__name}] is here - {self.__description}")

    def get_name(self):
        """
        gets items name
        """
        return self.__name
