print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original=raw_input("Enter a word:")
print original
if len(original)< 0 and original.isalpha():
    print original
else:
    print "empty"

    pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha() :
     word = original.lower()
     first=word[0]
     new_word= word + first+ pyg
     print original
     new_word=new_word[1:len(new_word)]
     print new_word
else:
    print 'empty'

