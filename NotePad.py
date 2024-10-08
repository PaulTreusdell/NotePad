from pathlib import Path
import json

class NotePad:

    def __init__(self, noteFile = 'notes.json', accFile = 'login.json'):
        self.noteFile = Path(noteFile)
        self.accFile = Path(accFile)
        self.loadNote = self.load_Note()
        self.loadAcc = self.load_Acc()

    def load_Acc(self):
        if self.accFile.exists():
            with open(self.accFile, 'r') as f:
                return json.load(f)
        else:
            return []

    def load_Note(self):
        if self.noteFile.exists():
            with open(self.noteFile, 'r') as f:
                return json.load(f)
        else:
            return []
    
    def save(self, file_to_save):
        #Save The Account File
        if file_to_save == 'account':
            with open(self.accFile, 'w') as f:
                json.dump(self.loadAcc, f, indent = 2)
        #Save The Notes File
        elif file_to_save == 'notes':
            with open(self.noteFile, 'w') as f:
                json.dump(self.loadNote, f, indent = 2)
    
    def createAcc(self):
        #Username
        username = input('Enter in a username you would like to use! ')

        #Password
        lenVerify = False
        sCharVerify=  False
        sChars = ['!', '@', '#', '$', '%', '&', '*']
        print(f'In order to create a password, it must be a minimum of 8 characters and have one of the following characters: {sChars}')
        while True:
            password = input('Enter in a password that meets the requirements mentioned above: ')
            #Check Length
            if len(password) >= 8:
                lenVerify = True
            else:
                print('Your password is of an incorrect length!')
            #Check if Special Character Inside
            for chr in password:
                if chr in sChars:
                    sCharVerify = True
                    break
            if not sCharVerify:
                print('You are missing a special character from your password!')
            #Ensure both requirements met
            if sCharVerify and lenVerify:
                self.loadAcc.append({'Username': username, 'Password': password})
                self.save('account')
                break

    def writeNotes(self):
        title = input('Enter in the title of the note: ')
        note_to_add = input('Enter in what you would like to add to your notes: ')
        self.loadNote.append({'Title': title, 'Notes': note_to_add})
        self.save('notes')
    
    def delNotes(self):
        note_to_delete = int(input('Enter in the number of the note would you like to delete: '))
        if 0 <= note_to_delete < len(self.loadNote):
            del self.loadNote[note_to_delete]
            self.save('notes')
            print('Note Deleted')
        else:
            print('Invalid Note Number')

    def viewNotes(self):
        if not self.loadNote:
            print('No Notes Found')
        else:
            for noteIndex in range(len(self.loadNote)):
                print(f"Note #{noteIndex}:\n{self.loadNote[noteIndex]}")

    def viewAccs(self):
        if not self.loadAcc:
            print('No Accounts Created')
        else:
            for account in self.loadAcc:
                print(account)
    
    def login(self):
        username = input('Enter in your username: ')
        password = input('Enter in your password: ')
        check = {'Username': username, 'Password': password}
        if check in self.loadAcc:
            print(f"Welcome {username}, enjoy your time here!")
            return True
        else:
            print('Account Not Found. Try to Create an Account.')
        return False
    
def main():
    note_pad = NotePad()

    #Logging In
    check = True
    while check:
        inp = input('Do you have an account? y/n')
        if inp == 'y':
            boolean = note_pad.login()
            if boolean:
                check = False
        else:
            note_pad.createAcc()
    while True:
        decision = int(input('\nWould you like to:\n1. Write Notes\n2. Delete Notes\n3. View Notes\n4. View Accounts\n5. Exit\n'))
        if decision > 0 and decision <= 5:
            if decision == 1:
                note_pad.writeNotes()
            elif decision == 2:
                note_pad.delNotes()
            elif decision == 3:
                note_pad.viewNotes()
            elif decision == 4:
                note_pad.viewAccs()
            elif decision == 5:
                print('Exiting...')
                break
            else:
                print('Invalid')
        else:
            print('Enter in a valid category number')

if __name__ == "__main__":
    main()
