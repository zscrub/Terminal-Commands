import os
import sys

for root, dirs, files in os.walk('C:\\Users\\xacc'):
    for name in files:
        if name == sys.argv[1]:
            print(os.path.abspath(os.path.join(root, name)))

token = sys.argv[1]
print('My token is: ' + token)