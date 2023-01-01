# Email slicer

# Function to get and process email
def process_email():
    # Get email
    email = input('What is your email?')
    # Split
    email_split = email.split('@',1)
    print(f'Your email is {email_split}')

# run if main
if __name__ == '__main__':
    process_email()
