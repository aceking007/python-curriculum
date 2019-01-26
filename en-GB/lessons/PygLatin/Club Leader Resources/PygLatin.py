#Welcome statement
print('Welcome to the PygLatin translator')
word = input('Enter a word:')

#Suffix
pyg = 'ay'

#Validating word
if (len(word) > 0) and (word.isalpha()):
  original = word.lower()
  first = original[0]
  new = original + first + pyg
  print ('The encoded word is: ' + new[1:])

else:
  #Error statement
  print ('This is not a valid word!')
