numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jacks", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


class card_object:
    def __init__(self, value, suit, file_name):
        self.value = value
        self.suit = suit
        self.file_name = file_name

    @staticmethod
    def parse_name(image_name):
        """Returns an array in the form [value, suit]"""
        # each image name is in the format: "num-suit.png"
        image_name = image_name[0:-4]

        image_name = image_name.split("-")  # splitting the value and suit
        image_name[0] = int(image_name[0])  # Turning the string into an integer

        return image_name

    def __str__(self):
        number_to_message={1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
                           11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace' }
        parsed=self.parse_name(self.file_name)
        return str(number_to_message[parsed[0]] + " of " + parsed[1])


class deck:
    def __init__(self):
        self.cards = []
        self.player_cards = []
        self.computer_cards = []

    @staticmethod
    def parse_image_name(image_name):
        return card_object.parse_name(image_name)


    def generate_deck(self):
        import os
        from random import shuffle

        original_directory = os.getcwd()
        # We will generate the deck from the file of card images:
        if "cards" not in os.getcwd():
            os.chdir("cards")
        cards = os.listdir()

        all_cards = []
        for card in cards:
            if card != "result.txt":
                parsed_form = self.parse_image_name(card)  # Parsing data from 'Cards' file
                card_obj = card_object(value=parsed_form[0], suit=parsed_form[1], file_name=card)
                all_cards.append(card_obj)

        shuffle(all_cards)  # we shuffle the order of cards
        self.cards = all_cards

        os.chdir(original_directory)  # We go back to the original directory
        # Returns nothing because the deck is already stored within the self.cards variable

    def split_deck(self):

        for i in range(len(self.cards)):

            if i < len(self.cards)/2:
                self.player_cards.append(self.cards[i])  # the first half of the deck is given to the player
            else:
                self.computer_cards.append(self.cards[i])  # the second half of the deck is given to the computer



class war_game:

    def __init__(self, player_cards, computer_cards):
        self.player_cards = player_cards
        self.computer_cards = computer_cards
        self.at_war = False

    def draw1(self):
        return [self.player_cards[0], self.computer_cards[
            0]]  # returns 2 outputs, the first is the player's card, the second is the computer's card

    def war(self):
        howmany=5
        if len(self.computer_cards) < 5 and len(self.player_cards) < 5:
            # Neither side has enough cards to go to war
            self.winner="draw"
            p_total = self.player_cards[-1].value  # player's card total
            c_total = self.computer_cards[-1].value  # computer's card total

        elif len(self.player_cards) < 5:
            # Only the player does not have enough cards to play, computer wins game
            c_total = self.computer_cards[4].value  # computer's card total
            p_total = self.player_cards[-1].value  # player's card total

            self.winner= "computer won all"

        elif len(self.computer_cards) < 5:
            # Only the computer does have enough cards to play, player wins game
            p_total = self.player_cards[4].value  # player's card total
            c_total = self.computer_cards[-1].value  # computer's card total

        else:

            p_total = self.player_cards[4].value  # player's card total
            c_total = self.computer_cards[4].value  # computer's card total


        if p_total > c_total:
            #Player has won war
            self.winner = "player war"
            return "player war"

        if p_total < c_total:
            #Computer has won war
            self.winner = "computer war"

            return "computer war"
        else:
            self.winner="draw"
            return "draw"

    def one_round(self):



        player, computer = self.draw1()  # player is the card the player drew, computer is the card the computer drew

        if player.value > computer.value:
            self.winner = "player"  # self.winner will be "player" if the player wins

        elif player.value < computer.value:
            # computer has a higher valued card_object
            self.winner = "computer"  # self.winner will be "computer" if the computer wins

        else:
            # the cards have equal value, they shall go to war
            self.winner = self.war()

        if self.winner == "draw":
            # If it is still a draw even after going to war, both players will put their first card to the back of their deck

            self.player_cards.pop(0)
            self.player_cards.append(player)

            self.computer_cards.pop(0)
            self.computer_cards.append(computer)
            return "KEEP GOING"

        # Both players pop their first cards
        self.computer_cards.pop(0)
        self.player_cards.pop(0)

        if self.winner == "player":
            # Player has lost round, all cards are appended to the players hand

            self.player_cards.append(computer)
            self.player_cards.append(player)
        elif self.winner == "computer":
            # Player has won round, all cards are appended to computer hand
            self.computer_cards.append(player)
            self.computer_cards.append(computer)

        else:
            if len(self.player_cards) < 4 and len(self.computer_cards) < 4:
                player_iterate = len(self.player_cards)
                computer_iterate = len(self.computer_cards)
            elif len(self.player_cards) < 4:
                player_iterate = len(self.player_cards)
                computer_iterate = 4

            elif len(self.computer_cards) < 4:
                player_iterate = 4
                computer_iterate = len(self.computer_cards)

            else:
                player_iterate = 4
                computer_iterate = 4


            player_popped = []
            computer_popped = []
            for i in range(player_iterate):
                player_popped.append(self.player_cards[0])
                self.player_cards.pop(0)

            for i in range(computer_iterate):
                computer_popped.append(self.computer_cards[0])
                self.computer_cards.pop(0)

            # The game has gone to war
            if self.winner == "computer war":
                # The computer has won at war, all cards will be added to computer's deck
                for i in range(len(player_popped)):
                    # Adding everything that was popped to the computer:
                    self.computer_cards.append(player_popped[i])

                for i in range(len(computer_popped)):
                    self.computer_cards.append(computer_popped[i])

                # Now we add the initial cards that were drawn (before they went to war)
                self.computer_cards.append(player)
                self.computer_cards.append(computer)

            elif self.winner == "player war":
                # Player has won war, everything will be added to the players hand

                for i in range(len(player_popped)):
                    # Adding everything that was popped to the player:
                    self.player_cards.append(player_popped[i])

                for i in range(len(computer_popped)):
                    self.player_cards.append(computer_popped[i])

                # Now we add the initial cards that were drawn (before they went to war)
                self.player_cards.append(player)
                self.player_cards.append(computer)

            elif self.winner == "computer won all":
                for card in self.player_cards:
                    self.computer_cards.append(card)
                self.player_cards = []
            elif self.winner == "player won all":
                for card in self.computer_cards:
                    self.player_cards.append(card)
                self.computer_cards = []

        # For debugging purposes:

        asdf = []
        asd = []
        for i in range(len(self.player_cards)):
            asdf.append(self.player_cards[i].file_name)
        for i in range(len(self.computer_cards)):
            asd.append(self.computer_cards[i].file_name)

        # print(asdf, len(self.player_cards))
        # print()
        # print(asd, len(self.computer_cards))
        # print(len(self.player_cards) + len(self.computer_cards))
        # print(self.winner)
        # print()
        # print()


        # checking to see if any of the players has won:
        if len(self.computer_cards) == 0:
            return "PLAYER HAS WON"
        if len(self.player_cards) == 0:
            return "COMPUTER HAS WON"

        return "NO WINNER"

