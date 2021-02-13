import math
from collections import defaultdict
from matchingsystem import settings
import string
import codecs
import sys

def get_match(keywords):
    '''
        Get matching lecturers and return a list of lecturers
    '''
    #Load index
    main_index= defaultdict(list)
    f=open("/".join([settings.MEDIA_DIR,'indexfile.txt']), 'r', encoding="utf-8")
    for line in f:
        line=line.rstrip()
        term,documents= line.split('|')
        documents= documents.split(';')

        for doc in documents:
            postings= doc.split(',')
            main_index[term].append(postings)

    f.close()
    print(main_index)

    #Match keywords
    matching_lecturers=[]
    for term in keywords:
        for posting in main_index[term]:
            posting.append(len(main_index[term]))
            matching_lecturers.append(posting)

    #Check if there is no match
    if matching_lecturers:
        #Split the keywords and find match again
        #Check each keyword
        for keyword in keywords:
            # Check if its a phrase
            if len(keyword.split()) > 1:
                #Its a phrase
                #Split the words and find match
                words_split= keyword.split()

                #punctuation to remove from the keywords
                punctuations = string.punctuation
                punctuations_list= [char for char in punctuations]

                #Match keyword
                for word in words_split:
                    #remove punctuation marks
                    #Check if word is a punctuation and remove
                    if word in punctuations_list:
                        continue
                    else:
                        #Get a match
                        for posting in main_index[word]:
                            posting.append(len(main_index[word]))
                            matching_lecturers.append(posting)

    return matching_lecturers

def get_tfidf(postings, total_documents):
    '''
        Finds the tfidf of each posting and returns a posting list of lec_id and the tfidf
    '''
    tfidf_posting = []
    for posting in postings:
        #get the tf
        term_documents= posting[2]
        #get inverse document
        idf= math.log(total_documents/float(term_documents))
        tfidf= float(posting[1]) * idf

        #Get the tfidf
        tfidf_posting.append([posting[0], tfidf])

    return tfidf_posting


def rank_lecturers(postings):
    '''
        Returns a list of lecture_ids in descending order
    '''
    #Check each posting
    lecturer_score= defaultdict(int)

    #Add total score
    for posting in postings:
        lecturer_score[posting[0]] += posting[1]

    print(lecturer_score)

    #Arrange in descending order
    lec_ids= sorted(lecturer_score, key=lecturer_score.get, reverse=True)

    return lec_ids
