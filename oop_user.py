# Create a file with the User class, including the __init__ with all the attributes, parameters and default values.
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name     = first_name
        self.last_name      = last_name
        self.email          = email
        self.age            = age
        self.is_rewards_member   = False
        self.gold_card_points    = 0
    
    # Add the display_info(self) method to the User class
    def display_info(self):
        print(f"""First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nReward Member: {self.is_rewards_member}\nGold Card Points: {self.gold_card_points}\n\n""")
    
    def enroll(self):

        # Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
        if(not self.is_rewards_member):
        
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User already a member.")

        return self.is_rewards_member


    def spend_points(self, amount):
        difference = self.gold_card_points - amount

        # Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
        if(not difference < 0):
            self.gold_card_points = difference
        else:
            print("Insufficient gold card points!")

UserJeffrey = User("Jeffrey", "Carl", "jcsbugnay@gmail.com", 27)

# In the outer scope, create a user instance and call the display_info method to test.
UserJeffrey.display_info()

# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
UserJeffrey.enroll()

# Make 2 more instances of the User class.
UserClaire = User("Jan", "Claire", "janclaire@gmail.com", 25)
UserJerson = User("Jerson", "Son", "jefferson@gmail.com", 18)

# Have the first user spend 50 points
UserJeffrey.spend_points(50)

# Have the second user enroll.
UserClaire.enroll()

# Have the second user spend 80 points
UserClaire.spend_points(80)

# Call the display method on each of the users
UserJeffrey.display_info()
UserClaire.display_info()
UserJerson.display_info()

# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.
UserJeffrey.enroll()

# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.
UserJerson.spend_points(40)