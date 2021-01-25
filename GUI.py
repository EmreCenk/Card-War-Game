import tkinter as tk


class GUI:

    def __init__(self):
        self.BACKGROUND_COLOR = "#add8e6" #The background color
        self.HEIGHT = 500 #This is the initial window size, everything will be resized if you change the size of the
        # window
        self.WIDTH = 800

        self.root = tk.Tk()  # Initializing root
        self.root.title("War Game")  # setting window title name

        self.screen = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.screen.pack()

        # initializing background:
        self.main_frame = tk.Frame(self.root, bg=self.BACKGROUND_COLOR)

        # Placing the background:
        self.main_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor="n")

        # PLACE HOLDER VALUES:
        self.username = "12345678"

        self.list_of_objects = []  # we will store a list of objects so that we can delete things on the screen
        self.NEW_GAME=False
        self.user_displayed_cards = []  # we will store which cards are displayed
        self.computer_displayed_cards = []  # The same things applies for the computer's cards

    def clear_page(self):
        # This function deletes every object on the page. It will be used when transitioning between pages.
        for object in self.list_of_objects:
            object.destroy()

        self.list_of_objects = []  # Just to make sure everything is fully wiped from memory

    def create_card(self, card_name, what_to_align,border=10):
        # Variable what_to_align, is a frame. The card is going to be generated is automatically lined up with 'what_to_align'

        if "blank" in card_name:
            card_directory=r"other_cards\ "[0:-1]
        else:
            card_directory = r"cards\ "[0:-1]  # Directory for card

        img = tk.PhotoImage(file=card_directory + card_name)
        labelimg = tk.Label(what_to_align, image=img, bd=border, bg=self.BACKGROUND_COLOR)
        labelimg.photo = img

        labelimg.pack(side=tk.LEFT)

        if what_to_align == self.user_card_holder:
            self.user_displayed_cards.append(labelimg)
        else:
            self.computer_displayed_cards.append(labelimg)

    def quit(self,command_to_give="menu"):
        if command_to_give=="menu":
            command_to_give=self.create_menu
        else:
            command_to_give=self.play_window
        self.clear_page()
        quit_color = self.BACKGROUND_COLOR  # The background color for the quit interface
        question = tk.Label(self.main_frame,
                            text="Are you sure you would like to quit?",
                            bg=quit_color,
                            font=("Helvetica", 15),
                            )

        question.place(relx=0.5, rely=0.1, relheight=0.15, relwidth=0.7, anchor="n")

        # We declare a frame, inside this we will be placing the two answers.
        answer_frame = tk.Frame(self.root, bg=quit_color)
        answer_frame.place(relx=0.5, rely=0.4, height=100, width=400, anchor="n")

        # We place the quit
        verify = tk.Button(answer_frame,
                           text="Quit",
                           bg=quit_color,
                           font=("Helvetica", 40),
                           bd=0,
                           command=self.root.destroy
                           )
        verify.pack(side=tk.LEFT)  # We use pack, so we don't have to deal with aligning everything
        # The Quit button is stuck to the left of the 'answer_frame'

        cancel = tk.Button(answer_frame,
                           text="Go back",
                           bg=quit_color,
                           font=("Helvetica", 40),
                           bd=0,
                           command=command_to_give
                           )

        cancel.pack(side=tk.RIGHT, )

        # We add everything that was formed in this function to the list of objects
        self.list_of_objects.append(answer_frame)
        self.list_of_objects.append(question)
    def quit2(self):
        self.quit(command_to_give="anything else")
    def menu_button(self,relx=0.0,rely=0.0,relwidth=0.3,relheight=0.18,font_size=30,text="Menu"):
        if text=="Menu":
            command=self.create_menu
        else:
            command=self.play_window
        go_back = tk.Button(self.main_frame,  # Since this will be the child of the initial frame
                            text=text,
                            bg=self.BACKGROUND_COLOR,  # background color
                            font=("Helvetica", font_size),  # helvetica is the font, 60 is the font size
                            bd=0,
                            command=command)  # We don't want any borders

        go_back.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="nw")
        self.list_of_objects.append(go_back)
    def delete_expansion(self):
        self.drop_frame.destroy()
        self.drop_down_menu_button(relx=0,rely=0,relwidth=0.3,relheight=0.1,font_size=25) #Placing the dropdown menu
    def drop_down(self,relx=0.0,rely=0.0,relwidth=1,relheight=0.1,font_size=25):
        self.go_back.destroy() #Deleting the menu button
        self.drop_frame = tk.Frame(self.root, bg=self.BACKGROUND_COLOR)
        self.drop_frame.place(relx=relx,rely=rely, relwidth=relwidth, relheight=relheight, anchor="nw")

        self.CLOSE_EXPANSION=tk.Button(self.drop_frame,
                                       text="Close Expansion   ",
                                       bg=self.BACKGROUND_COLOR,
                                       bd=0,
                                       font=("Helvetica",font_size),
                                       command=self.delete_expansion)
        self.CLOSE_EXPANSION.pack(side=tk.LEFT)
        self.MENU_BUTTON=tk.Button(self.drop_frame,  # Since this will be the child of the initial frame
                            text="   Menu   ", #the spaces are for padding
                            bg=self.BACKGROUND_COLOR,  # background color
                            font=("Helvetica", font_size),  # helvetica is the font, 60 is the font size
                            bd=0,
                            command=self.create_menu)
        self.MENU_BUTTON.pack(side=tk.LEFT)

        self.QUIT=tk.Button(self.drop_frame,
                            text="   Quit   ",
                            bg=self.BACKGROUND_COLOR,  # background color
                            font=("Helvetica", font_size),  # helvetica is the font, 60 is the font size
                            bd=0,
                            command=self.quit2)
        self.QUIT.pack(side=tk.LEFT)

        self.RULES=tk.Button(self.drop_frame,
                             text="   Rules   ",
                             bg=self.BACKGROUND_COLOR,
                             font=("Helvetica",font_size),
                             bd=0,
                             command=self.rule_window2)
        self.RULES.pack(side=tk.LEFT)
        self.list_of_objects.append(self.drop_frame)


    def drop_down_menu_button(self,relx=0.0,rely=0.0,relwidth=0.3,relheight=0.18,font_size=25):
        self.go_back = tk.Button(self.main_frame,  # Since this will be the child of the initial frame
                            text="Options",
                            bg=self.BACKGROUND_COLOR,  # background color
                            font=("Helvetica", font_size),  # helvetica is the font, 60 is the font size
                            bd=0,
                            command=self.drop_down)  # We don't want any borders

        self.go_back.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="nw")
        self.list_of_objects.append(self.go_back)
    def rule_window(self,what_page="from menu"):
        if what_page=="from menu":
            text="Menu"
        else:
            text="Back to game"
        # The page is cleared before anything
        self.clear_page()


        rules = """\nEach player gets 26 cards. 
        Click NEXT to turn 2 cards from each player's deck.
        The player that turned the higher valued card gets the 2 cards.\n
        If cards are the same value,
        each player turns an additional three cards face down,
        and another face up. The player with the higher value
        wins all the cards.\nPlease note, the card values are as follows:\n
        1<2<3<4<5<6<7<8<8<9<10<Jack<Queen<King<Ace"""
        rules = tk.Label(self.main_frame,
                         text=rules,
                         bg=self.BACKGROUND_COLOR,
                         font=("Helvetica", 20),
                         )

        rules.place(relx=-0.01, rely=0, relwidth=1, relheight=1)
        if what_page=="from menu":
            self.menu_button()  # Menu button created to return
        else:
            self.menu_button(text="Back to Game",relwidth=0.7)
        # Now, we append everything we have made to the objects list:
        self.list_of_objects.append(rules)
    def rule_window2(self):
        self.rule_window("anything else")
    def destroy_cards(self):
        #This function deletes all cards on the screen (Only deletes the cards, everything else stays).
        for card in self.user_displayed_cards:
            card.destroy()
        for card in self.computer_displayed_cards:
            card.destroy()

        self.create_card(card_name="blank.png",what_to_align=self.user_card_holder,border=35)
        self.create_card(card_name="blank.png",what_to_align=self.computer_card_holder,border=35)

    def final_screen(self,text_to_display):
        self.clear_page()
        message=tk.Label(self.main_frame,
                         bg=self.BACKGROUND_COLOR,
                         text=text_to_display,
                         font=("Helvetica", 30),
                         bd=0, )
        message.place(anchor="nw", relx=0,rely=-0.15,relheight=1,relwidth=1)

        #Note: every widget must come after the message. Since 'message' takes up the entire screen, it will obscure
        # any widget added before it

        self.menu_button(relx=0.05,rely=0.6,relwidth=0.34,relheight=0.3, font_size=25) #Setting the menu button

        play_again=tk.Button(self.main_frame,  # Since this will be the child of the initial frame
                         text="Play Again",
                         bg=self.BACKGROUND_COLOR,  # background color
                         font=("Helvetica", 25),  # helvetica is the font, 60 is the font size
                         bd=0,  # We don't want any borders
                         command=self.username_window)
        play_again.place(anchor="nw",relx=0.4,rely=0.6,relwidth=0.25,relheight=0.3)

        #Setting the quit button:
        quit_button=tk.Button(self.main_frame,
                              text="Quit",
                              bg=self.BACKGROUND_COLOR,
                              font=("Helvetica", 25),
                              bd=0,
                              command=self.quit)

        #Setting the coordinates of the quit button
        quit_button.place(anchor="nw",relx=0.66,rely=0.6,relwidth=0.25,relheight=0.3)

        #Storing the widgets:
        self.list_of_objects.append(message)
        self.list_of_objects.append(play_again)
        self.list_of_objects.append(quit_button)

    def update_play(self):

        if len(self.game.computer_cards)<1:
            #The game is finished, we advance to the final screen
            self.final_screen(self.username+ " has won the game.\nCongratulations!")
            return None
        elif len(self.game.player_cards)<1:
            #The game is finished, we advance to the final screen
            self.final_screen("The Computer has won the game.\nBetter luck next time.")
            return None



        #UPDATING CARDS:
        self.destroy_cards() #Deleting all cards before we update
        #CREATING THE INITIAL 2 CARDS THAT ARE DRAWN:
        self.create_card(self.game.player_cards[0].file_name, self.user_card_holder)
        self.create_card(self.game.computer_cards[0].file_name, self.computer_card_holder)

        #We store the current states of each deck
        player_current=list(self.game.player_cards)
        computer_current=list(self.game.computer_cards)

        self.result = self.game.one_round()  # Winner of the game

        if "war" in self.game.winner or "won all" in self.game.winner or "draw" in self.game.winner:

            #we check one more time if anybody has won, since the output could be "won all"
            if len(player_current) < 1:
                # The game is finished, we advance to the final screen
                self.final_screen(self.username + " has won the game.\nCongratulations!")
                return None
            elif len(computer_current) < 1:
                # The game is finished, we advance to the final screen
                self.final_screen("The Computer has won the game.\nBetter luck next time.")
                return None

            #The game has gone to war
            if len(computer_current) < 5 and len(player_current) < 5:
                # Neither side has enough cards to go to war

                p_total = player_current[-1].file_name  # player's card to display
                c_total = computer_current[-1].file_name  # computer's card display

            elif len(player_current) < 5:

                c_total = computer_current[4].file_name  # computer's card display
                p_total = player_current[-1].file_name  # player's card display

            elif len(computer_current) < 5:

                p_total = player_current[4].file_name  # player's card display
                c_total = computer_current[-1].file_name  # computer's card display

            else:

                p_total = player_current[4].file_name  # player's card total
                c_total = computer_current[4].file_name  # computer's card total

            #How many blank cards for player:
            if len(player_current)<5:
                player_iterate=len(player_current)-2
            else:
                player_iterate=3

            #How many blank cards for computer:
            if len(computer_current)<5:
                computer_iterate=len(computer_current)-2
            else:
                computer_iterate=3
            #We create 3 blank card images:
            for i in range(player_iterate):
                self.create_card("blank.png",self.user_card_holder)
            for i in range(computer_iterate):
                self.create_card("blank.png",self.computer_card_holder)

            # We check to make sure that the last card and first card are different,
            # to avoid double printing:
            if len(player_current)>1:
                self.create_card(p_total,self.user_card_holder)
            if len(computer_current)>1:
                self.create_card(c_total, self.computer_card_holder)

            if "player" in self.game.winner:
                #Player has won
                displayr="At war, " + self.username

            elif "computer" in self.game.winner:
                #Computer has won
                displayr="At war, " + "Computer"
            else:
                #It is a draw.
                displayr="At war, nobody"

            if len(computer_current)<5:
                computer_current = computer_current[-1]
            else:
                computer_current=computer_current[4]

            if len(player_current)<5:

                player_current = player_current[-1]
            else:
                player_current=player_current[4]


        elif "player" in self.game.winner:
            #They have not gone to war
            displayr=self.username
            player_current = player_current[0]
            computer_current=computer_current[0]
        elif "computer" in self.game.winner:
            #They have not gone to war
            displayr="Computer"
            player_current = player_current[0]
            computer_current=computer_current[0]
        else:
            displayr="Nobody "
            player_current = player_current[0]
            computer_current=computer_current[0]

        if "player" in self.game.winner:
            result=str(player_current)+ " is greater than " +str(computer_current)
        elif "computer" in self.game.winner:
            result=str(computer_current)+ " is greater than " + str(player_current)
        else:
            result=str(computer_current)+ " is equal to " + str(player_current)
        self.result_window["text"]=result+".\n"+displayr+ " has won this round."  # winner of the round

        #UPDATING SCORES:
        self.username_display['text']=self.username+"\nScore: " + str(len(self.game.player_cards))
        self.computer_display['text']="Computer"+"\nScore: " + str(len(self.game.computer_cards))

        self.list_of_objects.append(self.result_window)


    def next_button(self):
        next = tk.Button(self.main_frame,  # Since this will be the child of the initial frame
                         text="Next",
                         bg="#97ADB4",  # background color
                         font=("Helvetica", 30),  # helvetica is the font, 60 is the font size
                         bd=0,  # We don't want any borders
                         command=self.update_play)

        next.place(relx=0.5, rely=0.83, relwidth=0.2, relheight=0.15, anchor="n")  # Placing menu
        self.list_of_objects.append(next)  # adding to the list of objects

    def take_username(self):

        potential_username = self.entry.get()
        if len(potential_username) > 9:
            self.prompt['text'] = "Your username is longer than 9 letters.\nTry another username"
        elif len(potential_username) < 1:
            self.prompt['text'] = "You have not entered a username."
        else:
            self.username = potential_username
            self.play_window()

    def username_window(self):
        self.NEW_GAME=True
        self.clear_page()
        # The prompt for username:
        self.prompt = tk.Label(self.main_frame,
                               bg=self.BACKGROUND_COLOR,
                               text="Enter a username. The maximum character limit is 9 characters. ",
                               font=("Helvetica", 15),
                               bd=0, )
        self.prompt.place(relx=0.5, rely=0.15, relheight=0.2, relwidth=1, anchor="n")

        self.entry = tk.Entry(self.main_frame,  # Since this will be the child of the frame

                              bg="#97ADB4",  # background color
                              font=("Helvetica", 30),  # helvetica is the font, 60 is the font size
                              bd=0,  # We don't want any borders
                              )
        self.entry.place(anchor="n", relx=0.5, rely=0.35, relheight=0.15, relwidth=0.6)  # Input field

        input_button = tk.Button(self.main_frame,
                                 bg="#97ADB4",
                                 font=("Helvetica", 20),
                                 bd=0,
                                 text="Enter",
                                 command=self.take_username)
        input_button.place(anchor="n", relx=0.5, rely=0.8, relwidth=0.3, relheight=0.1)

        self.menu_button() #Creating a menu button in case someone wants to go back

        self.list_of_objects.append(self.entry)
        self.list_of_objects.append(self.prompt)
        self.list_of_objects.append(input_button)

    def initialize_play_window(self):
        CARD_HEIGHT = 100
        self.clear_page()  # Clearing page

        # We create a Frame for the player cards holder as well:
        self.computer_card_holder = tk.Frame(self.root, bg=self.BACKGROUND_COLOR)
        self.computer_card_holder.place(relx=0.2, rely=0.3, height=CARD_HEIGHT + 10, relwidth=0.8, anchor="nw")

        # We create a Frame for the user card holder. All cards will automatically be stacked from left to right
        self.user_card_holder = tk.Frame(self.root, bg=self.BACKGROUND_COLOR)
        self.user_card_holder.place(relx=0.2, rely=0.8, height=CARD_HEIGHT + 10, relwidth=0.8, anchor="sw")

        # Player and computer display statistics:
        # DISPLAYING THE USERNAME OF THE PLAYER:
        self.username_display = tk.Label(self.main_frame,
                                    text=self.username+"\nScore: " + str(len(self.game.player_cards)),
                                    bg=self.BACKGROUND_COLOR,
                                    font=("Arial", 20),
                                    )

        # DISPLAYING USERNAME OF COMPUTER:
        self.username_display.place(anchor="nw", relx=0.01, rely=0.65, relwidth=0.19, relheight=0.14)

        self.computer_display = tk.Label(self.main_frame,
                                    text="Computer"+"\nScore: " + str(len(self.game.computer_cards)),
                                    bg=self.BACKGROUND_COLOR,
                                    font=("Arial", 20),
                                    )
        self.computer_display.place(anchor="nw", relx=0.01, rely=0.33, relwidth=0.19, relheight=0.14)
        # GOING BACK TO MENU:


        #Placing the window where the result is written:
        self.result_window=tk.Label(self.main_frame,
                            text="",
                            bg=self.BACKGROUND_COLOR,
                            font=("Helvetica", 20),
                            )

        self.result_window.place(relx=0.5, rely=0.1, relheight=0.15, relwidth=1, anchor="n")

        self.drop_down_menu_button(relx=0,rely=0,relwidth=0.3,relheight=0.1,font_size=25) #Placing the dropdown menu
        # button

        self.next_button() #placing next button
        # Appending everything we have made to the list of objects:

        self.list_of_objects.append(self.user_card_holder)
        self.list_of_objects.append(self.computer_card_holder)
        self.list_of_objects.append(self.username_display)
        self.list_of_objects.append(self.computer_display)

    def play_window(self):
        self.clear_page()  # We clear the page before starting

        if self.NEW_GAME:
            import Game_Logic as gl  # Importing game rules
            # Initializing stats:
            self.user_card_number = 26
            self.computer_card_number = 26
            self.rounds = 0  # New game, everything starts from scratch

            deck = gl.deck()  # Forming the deck object
            deck.generate_deck()  # The deck has been generated
            deck.split_deck()  # Deck has been split. now, there are two decks under self.player_cards,
            # and self.computer_cards
            # Starting game:


            #Initializing game object::
            self.game = gl.war_game(deck.player_cards, deck.computer_cards)
        self.NEW_GAME=False

        self.initialize_play_window()  # Placing widgets on the screen

        #Placing the first ever batch of cards:
        self.update_play()

    def create_menu(self):
        # We clear the page, in case the user comes from another screen:
        self.clear_page()

        # The play button:
        play = tk.Button(self.main_frame,  # Since this will be the child of the initial frame
                         text="Play",
                         bg=self.BACKGROUND_COLOR,  # background color
                         font=("Helvetica", 60),  # helvetica is the font, 60 is the font size
                         bd=0,  # We don't want any borders
                         command=self.username_window)  # When clicked, the play_window function will be called
        # Placing the play button
        play.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.7, anchor="n")

        # The 'rules' button:
        rules = tk.Button(self.main_frame,
                          text="Rules",
                          bg=self.BACKGROUND_COLOR,
                          font=("Helvetica", 60),
                          bd=0,
                          command=self.rule_window)

        # placing the rules button
        rules.place(relx=0.5, rely=0.4, relheight=0.2, relwidth=0.7, anchor="n")

        # The quit button:
        quit = tk.Button(self.main_frame,
                         text="Quit",
                         bg=self.BACKGROUND_COLOR,
                         font=("Helvetica", 60),
                         bd=0,
                         command=self.quit)

        # Placing the quit button:
        quit.place(relx=0.5, rely=0.7, relheight=0.2, relwidth=0.7, anchor="n")

        # We add all buttons formed into the list of objects, so that we know what we need to delete when the game
        # starts. Also, we need to store these variables so that they are not wiped from memory
        self.list_of_objects.append(quit)
        self.list_of_objects.append(rules)
        self.list_of_objects.append(play)


