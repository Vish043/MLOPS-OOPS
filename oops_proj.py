class chatbook:
    def __init__ (self):
        self.username = ''
        self.password = ''
        self.loggedIn = False
        self.menu()

    def menu(self):
        user_inpt = input('''Welcome to Chatbook how would you like to proceed?
                               1. Press 1 to SignUp.
                               2. Press 2 to SignIn.
                               3. Press 3 to write a post.
                               4. Press 4 to message a friend.
                               5. Press any other key to exit \n''')
        if user_inpt == "1":
            self.signup()
        elif user_inpt == "2":
            self.signin()
        elif user_inpt == "3":
            self.my_post()
        elif user_inpt == "4":
            self.sending()
        else:
            exit()

    def signup(self):
        email = input("enter your email here -> ")
        pwd = input ("setup your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signedup successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing  1 in the min menu ")
        else :
            uname = input("Enter yout email/username here -> ")
            pwd = input("Enter your password here -> ")
            if self.username == uname and self.password == pwd:
                print("You have SignedIn successfully !!")
                self.loggedIn = True
            else:
                print("Please input correct credentials")
            print("\n")
            self.menu()

    def my_post(self):
        if self.loggedIn == False:
            print("Please SignIn first before writing a post")
        else:
            post = input("Enter your message here:\n")
            print(f"{self.username} posted * {post} * ")
        print("\n")
        self.menu()

    def sending(self):
        if self.loggedIn == True:
            txt = input("Enter your message here -> ")
            frnd = input("Who to send this msg? -> ")
            print (f"Your message has been sent to {frnd}")
        else:
             print("Please SignIn first before sending a msg")
        print("\n")
        self.menu()

#obj = chatbook()