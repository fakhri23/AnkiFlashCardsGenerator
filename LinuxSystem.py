import genanki
import os 
# List of Linux directories and their descriptions
linux_dirs = [
    ('/', 'Root directory, starting point of the filesystem hierarchy.'),
    ('/bin', 'Contains essential system command executables.'),
    ('/sbin', 'Contains essential system administration command executables.'),
    ('/boot', 'Contains files needed to start the boot process.'),
    ('/etc', "Contains system-wide configuration files and scripts."),
    ('/dev', 'Contains device files representing hardware devices.'),
    ('/home', 'Contains personal directories for each user.'),
    ('/lib', 'Contains shared libraries and kernel modules.'),
    ('/opt', 'Optional directory for storing third-party software.'),
    ('/proc', 'Virtual filesystem providing an interface to kernel internal data structures.'),
    ('/sys', 'Virtual filesystem providing an interface to kernel internal data structures for devices, drivers, and other components.'),
    ('/tmp', 'Temporary directory for storing files deleted after a system reboot.'),
    ('/usr', 'Contains user-related files, shared libraries, header files, documentation, and non-essential software binaries.'),
    ('/var', 'Contains variable data files, such as logs, databases, and mail spools.'),
]

# Define Anki note model
 
model_id = 10000000 # must be unique, how to do it automatically 

model = genanki.Model(
    model_id, 
    'Linux filesystem folders' , 
    fields =[
        {'name': 'Directory'}, 
        {'name': 'Description'}
    ],  
    templates =[
        {
            'name' : 'Card 1', #has sth to do with the template
            'qfmt' : '{{Directory}}', #question 
            'afmt' : '{{Description}}' #answer 
        }, 
        {
            'name' : 'Card 2', 
            'afmt' : '{{Description}}',
            'qfmt' : '{{Directory}}'
        },
    ]
)

#Generate Anki cards and add them to the deck 

deck_id = 10000001
deck = genanki.Deck(deck_id, 'Linux FileSystem')

for dir_name , description in linux_dirs: 
    note = genanki.Note(model = model, fields = [dir_name, description])
    deck.add_note(note)
    
#save the deck to an Anki package (*.apkg) file 



def answerYesOrNoTo( message):
    yes = ["yes", "y"]
    no = ["no", "n"]
    print(message)
    input =""
    while True:
        userInput = input("do you want to contine? yes/no").lower()
        if(userInput in yes):
            return True
        elif(userInput in no): 
            return False
        else: 
            print("Type yes/no")    

def main():
    store_path = 'AnkiCards' 
    if(os.path.exists('AnkiCards\linux_filesystem.apkg')):
        answer = answerYesOrNoTo("this deck already exists do you want to overwrite it")
        if(answer) :
            genanki.Package(deck).write_to_file('AnkiCards\linux_filesystem.apkg')
        
    

if __name__=="__main__": 
    main()    
