# Email slicer to split email into username and domain

# Function gets and splits email into username and domain
def process_email():
    # Get email
    email = input('What is your email?')
    # Split email into username and domain
    email_split = email.split('@', 1)
    # Print username and domain separately
    print(f'Your username is {email_split[0]}')
    print(f'Your domain is {email_split[1]}')

# Run if main
if __name__ == '__main__':
    # Run function to split email into username and domain
    process_email()
