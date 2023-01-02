# Email slicer

# Function to get and split email
def process_email():
    # Get email
    email = input('What is your email?')
    # Split
    email_split = email.split('@', 1)
    print(f'Your username is {email_split[0]}')
    print(f'Your domain is {email_split[1]}')

# Run if main
if __name__ == '__main__':
    process_email()
