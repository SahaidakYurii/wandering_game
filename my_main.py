import my_game

campus = my_game.Room("UCU Campus")
campus.set_description("A great teritory where you can forget about social life")

park = my_game.Room("Stryiskyi Park")
park.set_description("A lovely place to hang on hammocks")

sykhiv = my_game.Room("Sykhiv")
sykhiv.set_description("The most dangerous Lviv's region")

mall = my_game.Room("Victoria Gardens")
mall.set_description("A shopping mall with many shops")

campus.link_room(park, "north")
park.link_room(campus, "south")
campus.link_room(sykhiv, "south")
sykhiv.link_room(campus, "north")
sykhiv.link_room(mall, "west")
mall.link_room(sykhiv, "east")

serhii = my_game.Student("Serhii", "APPS UCU student. Likes jokes")
serhii.set_conversation("I need some coffe...")
campus.set_character(serhii)

gopnik = my_game.Enemy("Nikita", "Local gopnik. Wears adidas trousers and has a bat")
gopnik.set_conversation("Hey, do you have a cigarette?")
gopnik.set_weakness("cigarette")
sykhiv.set_character(gopnik)

seller = my_game.Friend("Denys", "Seller with a lot of goods, seems can he sell a hammock")
seller.set_conversation("I have anything you wish...")
seller.set_weakness("money")
mall.set_character(seller)

money = my_game.Item("money")
money.set_description("There's a lot of coins in the fountain. You can gather some")
park.set_item(money)



current_room = campus
backpack = []
defeated = 0
dead = False

while not dead:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "interact":
        if inhabitant is not None:
            if isinstance(inhabitant, my_game.Student):
                dropped_item = inhabitant.interact()
                if dropped_item:
                    backpack.append(dropped_item.get_name())
                    current_room.character = None
            else:    
                # Fight with the inhabitant, if there is one
                print("What will you interact with?")
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.interact(fight_with):
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_room.character = None
                        defeated += 1

                    else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the my_game")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
        else:
            print("There is no one here to interact with")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")

    else:
        print("I don't know how to " + command)

    if defeated == 2 and current_room == park:
        print("\nHorray, you set a hammock in park and can rest a little bit")
        dead = True
