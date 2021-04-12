""" Example One """
try:
    with open("test.txt") as file:
        file = file.read()
except FileNotFoundError:
        print('file does not exist')
else:
    words = file.split()
    num_words = len(words)
    print('the file has '+ file + 'has about'+ str(num_words)+ ' words')


""" Example Two """
print("\n Example Two")
def countWords(fileName):
    try :
        with open(fileName) as file:
            file = file.read()
    except FileNotFoundError:
        msg = "Sorry, the file {} does not exit".format(fileName)
        print(msg)
    else :
        word = file.split()
        num_word = len(word)
        print(" The file {} has about {} words".format(fileName, num_word))
fileName = 'test.txt'
countWords(fileName)

