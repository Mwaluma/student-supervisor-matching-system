import PyPDF2
from docx import Document
from nltk.tokenize import wordpunct_tokenize
from extraction.packages.porter_stemmer import get_stemmed_keywords
import string


def extract_text_from_document(url):
    '''
        Func that extracts text form document and return a body of text
    '''
    #Check if its pdf
    if url.endswith('.pdf'):
        text= ""

        #Extract content from pdf
        pdfFileObject= open('f:/University/Project 4th year/AI_Projects.pdf', 'rb')
        pdfReaderObject= PyPDF2.PdfFileReader(pdfFileObject)

        #Loop through each page
        for page in range(pdfReaderObject.numPages):
            #Get the page
            pageObj= pdfReaderObject.getPage(page)

            #Extract the page content and append to the previous content
            text += pageObj.extractText()

        #Close the file being read
        pdfFileObject.close()

        #Completed extracting the whole document
        #Return the text
        return text


    if url.endswith('.docx'):

        text= ""
        text_list= []
        document= Document(url)
        for line in document.paragraphs:
            text_list.append(line.text)

        text= " ".join(text_list)

        return text

    if url.endswith('.txt'):
        #Open the document
        f=open(url, 'r')
        text= f.read()

        #Close connection
        f= close()

        return text


def extract_tf(keywords, text):
    '''
        Gets the keywords term frequency
    '''

    #tokenize
    text= text.lower()
    words= wordpunct_tokenize(text)

    #remove punctuations
    punctuations = string.punctuation
    punctuations_list= [char for char in punctuations]

    for index,word in enumerate(words):
    #Check if word is a punctuation
        if word in punctuations_list:
            words.pop(index)
    #get unique words
    wordset= set(words)

    #Create dictionary for the words
    worddict= dict.fromkeys(wordset, 0)
    #Get the count of occurence of each term
    for word in words:
        worddict[word] += 1

    #Calculate the tf
    tfDict= {}
    total_count= len(words)

    #Check each keyword
    for keyword in keywords:
        # Check if its a phrase
        if len(keyword.split()) > 1:
            average= [0,0]
            #Its a phrase
            #Split the words and find the term frequency
            words_split= keyword.split()
            #Check for each word
            for word in words_split:
                #remove punctuation marks
                #Check if word is a punctuation
                if word in punctuations_list:
                    continue
                else:
                    average[0] += worddict[word]/total_count
                    average[1] += 1

            #get the average
            average[0] /= average[1]

            #Stem the keywords
            keyword= get_stemmed_keywords([keyword])
            tfDict[keyword[0]]= average[0]

        else:
            tf= worddict[keyword]/float(total_count)
            keyword= get_stemmed_keywords([keyword])
            tfDict[keyword[0]]= tf

    return tfDict
