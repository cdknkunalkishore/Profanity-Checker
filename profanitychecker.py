import urllib
def readtext():

    quotes = open("C:\Users\KK\Desktop\kk.txt")
    content = quotes.read()
    
    quotes.close()
    checkprofanity(content)

def checkprofanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
    output = connection.read()
    print(output)
    connection.close()
    
                        

readtext()
