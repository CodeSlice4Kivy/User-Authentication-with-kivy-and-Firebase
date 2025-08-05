# Import the main Kivy App class, which is the entry point for any Kivy application
from kivy.app import App

# Import ScreenManager to manage multiple screens (pages), and Screen for creating individual screens
from kivy.uix.screenmanager import ScreenManager, Screen

# Import Builder to load the KV file (which contains UI design written in Kivy language)
from kivy.lang import Builder

# Import the signup and login functions from our custom Firebase API module
from firebase_api import signup, login

# Load the UI layout defined in the 'main.kv' file
# This file contains the Kivy language code for the interface (buttons, text fields, etc.)
Builder.load_file("main.kv")


# -------------------------------
# Define Login Screen
# -------------------------------
class LoginScreen(Screen):
    """
    This class represents the Login screen.
    It inherits from Kivy's Screen class and provides functionality for user login.
    """

    def do_login(self):
        """
        This method is called when the user clicks the Login button.
        It takes the email and password input and attempts to authenticate the user via Firebase.
        """

        # Retrieve the email entered by the user from the TextInput with id='email' in main.kv
        email = self.ids.email.text

        # Retrieve the password entered by the user from the TextInput with id='password'
        password = self.ids.password.text

        # Call the login function from firebase_api.py, passing the email and password
        # This function returns a dictionary response from Firebase
        result = login(email, password)

        # Check if login was successful
        # Firebase returns an 'idToken' if the authentication succeeds
        if "idToken" in result:
            print("Login successful!")

            # Switch to the 'chat' screen by changing the ScreenManager's current screen
            App.get_running_app().root.current = "chat"
        else:
            # If login fails, print the error message from the Firebase response
            # result.get("error", {}) gets the error dictionary (or empty dict if not found)
            # .get("message", "") gets the actual error message (or empty string if not found)
            print("Login failed:", result.get("error", {}).get("message", ""))


# -------------------------------
# Define Signup Screen
# -------------------------------
class SignupScreen(Screen):
    """
    This class represents the Signup screen for creating new accounts.
    """

    def do_signup(self):
        """
        Called when the user clicks the Signup button.
        Attempts to register the user using Firebase Authentication.
        """

        # Get email and password from the TextInputs defined in main.kv
        email = self.ids.email.text
        password = self.ids.password.text

        # Call the signup function from firebase_api.py
        result = signup(email, password)

        # Check if signup was successful
        if "idToken" in result:
            print("Signup successful!")

            # If successful, navigate back to the Login screen
            App.get_running_app().root.current = "login"
        else:
            # Print the error message if signup fails
            print("Signup failed:", result.get("error", {}).get("message", ""))


# -------------------------------
# Define Chat Screen
# -------------------------------
class ChatScreen(Screen):
    """
    This class represents the Chat screen.
    Currently empty but will later contain chat functionalities.
    """
    pass


# -------------------------------
# Define the Main App
# -------------------------------
class WhatsAppCloneApp(App):
    """
    The main application class.
    Inherits from Kivy's App and manages the app lifecycle.
    """

    def build(self):
        """
        This method is automatically called when the app starts.
        It returns the root widget (ScreenManager) that contains all screens.
        """

        # Create an instance of ScreenManager
        sm = ScreenManager()

        # Add the Login screen to the ScreenManager with the name 'login'
        sm.add_widget(LoginScreen(name='login'))

        # Add the Signup screen with the name 'signup'
        sm.add_widget(SignupScreen(name='signup'))

        # Add the Chat screen with the name 'chat'
        sm.add_widget(ChatScreen(name='chat'))

        # Return the ScreenManager as the root widget
        return sm


# -------------------------------
# Run the Application
# -------------------------------
if __name__ == '__main__':
    # Create an instance of WhatsAppCloneApp and start the application loop
    WhatsAppCloneApp().run()
