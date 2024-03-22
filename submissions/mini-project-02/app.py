import os
import json

data_file_path = os.path.join(os.path.dirname(__file__), 'data.json')

class Password:
    def __init__(self, website, email, password):
        self.website = website
        self.email = email
        self.password = password

    def load_data(self):
        if os.path.exists(data_file_path):
            with open(data_file_path, 'r') as f:
                if f.read():
                    f.seek(0) 
                    return json.load(f)
        return {}
    
    def save_data(self, data):
        with open(data_file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def add_password(self):
        data = self.load_data()
        if self.website not in data:
            data[self.website] = [
                {
                    'email': self.email,
                    'password': self.password
                }
            ]
            self.save_data(data)
            print('Password added successfully')
        else:
            print('Website already exists, please update the password instead')

    def delete_password(self):
        data = self.load_data()
        if self.website in data:
            del data[self.website]
            self.save_data(data)
            print('Password deleted successfully')
        else:
            print('Website does not exist, please add the password instead')
        
    def update_password(self):
        data = self.load_data()
        if self.website in data:
            del data[self.website]
            self.email = input('Enter email: ')
            self.password = input('Enter password: ')
            data[self.website] = [{
                'email': self.email,
                'password': self.password
            }]
            self.save_data(data)
            print('Password updated successfully')
        else:
            print('Website does not exist, please add the password instead')

    def search_password(self):
        data = self.load_data()
        if self.website in data:
            for credentials in data[self.website]:
                print(' ')
                print(f'Website: {self.website}')
                print(f'\tEmail: {credentials["email"]}')
                print(f'\tPassword: {credentials["password"]}')
                print(' ')
        else:
            print('Website does not exist, please add the password instead')
    

    def show_all_passwords(self):
        data = self.load_data()
        if data:
            for website, credentials_list in data.items():
                for credentials in credentials_list:
                    print(f'Website: {website}')
                    print(f'\tEmail: {credentials["email"]}')
                    print(f'\tPassword: {credentials["password"]}')
                    print(' ')
        else:
            print('No passwords saved yet')



while True:
    print(' ')
    print('1. Add a new password')
    print('2. Delete a password')
    print('3. Update a password')
    print('4. Search a password')
    print('5. Show all passwords')
    print('6. Exit')
    print(' ')

    user_input = input('Enter your choice: ')
    print(' ')

    if user_input == '1':
        website = input('Enter website: ')
        email = input('Enter email: ')
        password = input('Enter password: ')
        credential = Password(website, email, password)
        credential.add_password()
    elif user_input == '2':
        website = input('Enter website: ')
        credential = Password(website, '', '')
        credential.delete_password()
    elif user_input == '3':
        website = input('Enter website: ')
        credential = Password(website, '', '')
        credential.update_password()
    elif user_input == '4':
        website = input('Enter website: ')
        credential = Password(website, '', '')
        credential.search_password()
    elif user_input == '5':
        credential = Password('', '', '')
        credential.show_all_passwords()
    elif user_input == '6':
        break
   