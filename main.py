import emailvalid
import laughs

def main():

    print("Welcome to Michael Pace's Random Joke Sender")
    x = input('Enter your email address: ')

    joke = laughs.get_joke()
    userEmail = emailvalid.check_email(x)

    if userEmail is False:
        print("You entered an invalid Email, Try again later")
    else:
        print("Email is valid.")
        print()
        print(joke)


main()