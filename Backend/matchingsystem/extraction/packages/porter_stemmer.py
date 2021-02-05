from nltk.stem import PorterStemmer

def get_stemmed_keywords(keyword_list):
    '''
        Stems keywords and returns key words that are stemmed
    '''
    #Holder of stemmed keywords
    stemmed_keywords= []

    #Create an instance of the stemmer
    ps= PorterStemmer()

    #Need to loop the list
    for keyword in keyword_list:

        #Check if it's a phrase
        if len(keyword.split()) > 1:

            #This means its a phrase
            phrase= keyword.split()
            stemmed_phrase= ""
            stemmed_word=""

            #Loop through it
            for index,word in enumerate(phrase):

                #Stem the word
                stemmed_word = ps.stem(word= word)
                #Checks if its first index in order to remove left spaces
                if index < 1:
                    stemmed_phrase= stemmed_word
                    continue

                stemmed_phrase= " ".join([stemmed_phrase, stemmed_word])

            #Append the stemmed phrase
            stemmed_keywords.append(stemmed_phrase)
            continue

        #Stem and append to the list
        stemmed_word= ps.stem(word=keyword)
        stemmed_keywords.append(stemmed_word)


    return stemmed_keywords
