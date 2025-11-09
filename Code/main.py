# main code
"""
Author: Ethan Mutsvairo
Task: ARC-TKT-002
Description: Basic CLI that welcomes the user and validates input.
"""

def format_user_info(user_info):
    """Format a single user's information for display."""
    return f"{user_info['User name']}'s favorite language is {user_info['Language']}"

def add_users(name, language):
    """Add a new user with their name and favorite language."""
    user_information = {"User name": name.strip(), "Language": language.strip()}
    return user_information

def main_code():
    # Initialize empty list to store user information
    key_info = []
    
    while True:
        print('\n1. Add users')
        print('2. View users')
        print('3. Exit')
        try:
            choice = input('What would you like to do: ').strip()
            if not choice:
                print('Please enter a choice (1, 2, or 3)')
                continue
                
            choice = int(choice)
            if choice == 1:
                user_name = input('What is your name: ').strip()
                user_language = input('What is your favorite language: ').strip()
                
                if not user_name or not user_language:
                    print('Name and language cannot be empty. Please try again.')
                    continue
                    
                data = add_users(user_name, user_language)
                key_info.append(data)
                print('User information saved successfully!')
                
            elif choice == 2:
                if not key_info:
                    print('There are no users to display yet.')
                else:
                    print('\nStored user information:')
                    for i, user in enumerate(key_info, 1):
                        print(f"{i}. {format_user_info(user)}")
                        
            elif choice == 3:
                decision = input('Are you sure you want to exit? (Y/n): ').strip().lower()
                if decision == 'y':
                    print('Goodbye!')
                    break
                    
            else:
                print('Invalid choice! Please enter 1, 2, or 3')
                
        except ValueError:
            print('Please enter a valid number!')

if __name__ == "__main__":
    main_code()