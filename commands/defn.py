import sys
from PyDictionary import PyDictionary

dictionary=PyDictionary()

def define(word):
    l=[]
    try:
        for key,value in dictionary.meaning(word).items():
            l=value
            print('\n{0}, {1}\n\nDefinitions:'.format(word, key))
        for dfn in l:
            print('{0}. {1}'.format((l.index(dfn)+1),dfn))
        print()
    except AttributeError:
        print('\nNo definition found for "{0}"\n'.format(word))

def synonym(word):
    try:
        print('\nSynonyms:')
        for s in dictionary.synonym(word):
            print('+{0}'.format(s))
        print()
    except TypeError:
        print('\nNo synonyms found for "{0}"\n'.format(word))


def antonym(word):
    try:
        print('\nAntonyms:')
        for a in dictionary.antonym(word):
            print('-{0}'.format(a))
        print()            
    except TypeError:
        print('\nNo antonyms found for "{0}"\n'.format(word))
  

if sys.argv[1]=='define' or sys.argv[1]=='dfn' or sys.argv[1]=='def':
    define(sys.argv[2])

if sys.argv[1]=='synonym' or sys.argv[1]=='syn' or sys.argv[1]=='syno':
    synonym(sys.argv[2])
if sys.argv[1]=='antonym' or sys.argv[1]=='ant' or sys.argv[1]=='anty':
    antonym(sys.argv[2])
