import os
filesList=[]

for root, dirs, files in os.walk('commands'):
    for name in files:
        # print(os.path.join(root, name))
        # print(name)
        filesList.append(name)

for file in filesList:
    if file[-3:] == '.py':
        print('Building {0}...\n'.format(file))
        os.system('cmd /c pyinstaller --onefile C:\\Users\\xacc\\Desktop\\TermCommands\\commands\\{0}'.format(file))
        print('{0} is now compiled!'.format(file))
