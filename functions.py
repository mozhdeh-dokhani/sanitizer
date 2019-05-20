#------------------------- Mozhdeh Dokhani ---------------------------------------
# date:    97/05/02
# version: 1.0
#---------------------------------------------------------------------------------

#------------------------------- Libraries ---------------------------------------
import csv
import sys
import string
import re
from num2words import num2words
#---------------------------------------------------------------------------------

#------------------------------- Initials ----------------------------------------
#Decrease the maxInt value by factor 10 as long as the OverflowError occurs.
maxInt    = sys.maxsize
decrement = True
while decrement:
    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt    = int(maxInt/10)
        decrement = True

#Define global result variable
result = []
#---------------------------------------------------------------------------------

#------------------------------------ Main ---------------------------------------
#Read CSV
def readCsv( path, delimiter = ',', huffingtonBool = False ):
    global result
    with open(path, newline='', encoding='utf8') as csvFile:
        reader = csv.DictReader(csvFile, delimiter = delimiter)
        for row in reader:
            url       = row["url"]
            category  = row["category"]
            reference = row["reference"]
            title     = sanitize(row["title"],huffingtonBool)
            subTitle  = sanitize(row['subTitle'],huffingtonBool)
            body      = sanitize(row['body'],huffingtonBool)
            # Append the new row as a dictionary to the result list
            result.append({'url': url, 'category': category, 'reference': reference, 'title': title, 'subTitle': subTitle,'body': body})
    return result
#=======================================
def sanitize( myStr, huffingtonBool, lowerCaseBool = True, removeApostrophesBool = True, removeExtraCharBool = True, removePuncBool = True, convertNumbersBool = True ):
    if ( huffingtonBool ):
        myStr = huffington(myStr)

    if ( lowerCaseBool ):
        myStr = lowerCase(myStr)

    if ( removeApostrophesBool ):
        myStr = removeApostrophes(myStr)

    if ( removeExtraCharBool ):
        myStr = removeExtraChar(myStr)

    if ( removePuncBool ):
        myStr = removePunc(myStr)

    if ( convertNumbersBool ):
        myStr = convertNumbers(myStr)

    return myStr
#=======================================
#Remove remainder scripts at the end of HuffingtonPost news (from ADVERTISEMENT word to the end)
def huffington( myStr ):
    i     = myStr.find("ADVERTISEMENT")
    myStr = myStr[:i]
    return myStr
#=======================================
#Convert all words to lower case
def lowerCase( myStr ):
    return myStr.lower()
#=======================================
#Covert all apostrophes into standard lexicons
def removeApostrophes( myStr ):
    myStr = myStr.replace("’", "'")
    myDictionary = {"i'm": "i am",
                    "i'll": "i will",
                    "i've": "i have",
                    "i'd": "i would",

                    "you're": "you are",
                    "you've": "you have",
                    "you'll": "you will",
                    "you'd": "you would",

                    "they're": "they are",
                    "they've": "they have",
                    "they'll": "they will",
                    "they'd": "they would",

                    "we're": "we are",
                    "we've": "we have",
                    "we'll": "we will",
                    "we'd": "we would",

                    "he's": "he is",
                    "he'd": "he would",
                    "he'll": "he will",

                    "she's": "she is",
                    "she'd": "she would",
                    "she'll": "she will",

                    "it's": "it is",
                    "it'd": "it would",
                    "it'll": "it will",

                    "that's": "that is",
                    "that'd": "that would",
                    "that'll": "that will",

                    "there's": "there is",

                    "could've": "could have",
                    "might've": "might have",
                    "must've": "must have",
                    "should've": "should have",
                    "would've": "would have",

                    "aren't": "are not",
                    "can't": "cannot",
                    "couldn't": "could not",
                    "didn't": "did not",
                    "doesn't": "does not",
                    "don't": "do not",
                    "hadn't": "had not",
                    "hasn't": "has not",
                    "haven't": "have not",
                    "isn't": "is not",
                    "mightn't": "might not",
                    "mustn't": "must not",
                    "shouldn't": "should not",
                    "wasn't": "was not",
                    "weren't": "were not",
                    "won't": "will not",
                    "wouldn't": "would not",

                    "let's": "let us",
                    "shan't": "shall not",

                    "who's": "who is",
                    "who'll": "who will",
                    "who'd": "who would",

                    "what're": "what are",
                    "what's": "what is",
                    "what'll": "what will",
                    "what'd": "what would",
                    "what've": "what have",

                    "where're": "where are",
                    "where's": "where is",
                    "where'll": "where will",
                    "where'd": "where would",
                    "where've": "where have",

                    "when're": "when are",
                    "when's": "when is",
                    "when'll": "when will",
                    "when'd": "where would",
                    "when've": "where have",

                    "why're": "why are",
                    "why's": "why is",
                    "why'll": "why will",
                    "why'd": "why would",
                    "why've": "why have",

                    "how're": "how are",
                    "how's": "how is",
                    "how'll": "how will",
                    "how'd": "how would",
                    "how've": "how have",
    }
    for key, value in myDictionary.items():
        if key in myStr:
            myStr = myStr.replace(key, value)
    return myStr
#=======================================
#Remove single quote, double quote, ...
def removeExtraChar( myStr ):
    return myStr.replace('"', '').replace("'","").replace('”', '').replace('“', '').replace('―', '')
#=======================================
#Remove all punctuations
def removePunc( myStr ):
    table = str.maketrans({key: None for key in string.punctuation})
    return myStr.translate(table)
#=======================================
#Convert numbers to words (cardinal and ordinal)
def convertNumbers( myStr ):
    #Ordinal numbers
    myStr = myStr.replace('1st', 'first').replace('2nd', 'second').replace('3rd', 'third')
    temp = "";
    for word in myStr.split():
        # Ordinal numbers
        ordinalFlag = False
        if ( re.match(r'\d+th$', word) ): #Ordinal numbers like 4th, 5th, ...
            ordinalFlag = True
            word = word.replace('th','')

        #Numbers
        if isInt(word): #Check if int, floats are not necessary to convert
            word = num2words(int(word))
            if (ordinalFlag):
                word += 'th' #Some misspelling happen, but I hope the spell checker fix them

        temp = " ".join([temp, word])

    # Remove the spaces from the end and at the begining and also duplicate spaces
    myStr = " ".join(temp.split())
    return myStr
#=======================================
#Check if the word is int or not
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
    return False
#=======================================
#Write CSV
def writeCsv( path, myList ):
    fieldNames = ['url','category','reference','title','subTitle','body']
    with open( path, 'w', newline = '', encoding = 'utf8' ) as csvFile:
        writer = csv.DictWriter( csvFile, fieldnames = fieldNames )
        writer.writeheader()
        writer.writerows(myList)
#---------------------------------------------------------------------------------