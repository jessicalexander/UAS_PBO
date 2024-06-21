from logger import log_activity

class User:
    def __init__(self, user_id, name, email, password):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._password = password
        self._logged_in = False 

    @log_activity
    def login(self, email, password):
        if email == self._email and password == self._password:
            self._logged_in = True
            print("Succesful Login!")
        else:
            print("Enter the correct email and password combination") 

    @log_activity
    def logout(self): 
        self._logged_in = False
        return "User has logged out"

    def is_logged_in(self): 
        return self._logged_in

    @log_activity
    def get_user_id(self):
        return self._user_id
    
    @log_activity
    def get_name(self):
        return self._name
    
    @log_activity
    def report_issue(self, description, et_system):
        et_system.create_ticket(self._name, description)

    @log_activity
    def view_announcement(self, announcement_system):
        announcement_system.view_announcement()

    @log_activity
    def search_books(self, keyword, library):
        library.get_book_results(keyword)

    @log_activity
    def view_book_content(self, keyword, library):
        library.get_book_content(keyword)

# # Create a User object
# user1 = User(user_id="prof001", name="John Doe", email="john@example.com", password="password123")
# user2 = User(user_id="stu001", name="Peter", email="peter@example.com", password="a123a")

# # Log in
# user1.login("john@example.com", "password123")
# user2.login("peter@example.com", "12345")

# # Logout
# user1.logout()

