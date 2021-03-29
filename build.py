import os
import getpass

filesList=[]

for root, dirs, files in os.walk('commands'):
    for name in files:
        # print(os.path.join(root, name))
        # print(name)
        filesList.append(name)

for file in filesList:
    if file[-3:] == '.py':
        print('\nBuilding {0}...\n'.format(file))
        ## Add path to scripts here: 
        os.system('cmd /c pyinstaller --onefile C:\\Users\\{0}\\Desktop\\TermCommands\\Terminal-Commands\\commands\\{1}'.format(getpass.getuser(), file))
        print('{0} is now compiled!\n'.format(file))
