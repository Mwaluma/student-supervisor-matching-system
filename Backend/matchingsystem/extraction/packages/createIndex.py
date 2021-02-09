from collections import defaultdict

class CreateIndex:
    def __init__(self):
        # Creates the inverted index
        self.index=defaultdict(list)

    def writeIndexToFile(self):
        '''
            write the inverted index to the file
        '''
        #Open the file to write index on
        f=open(self.indexFile, 'w')
        for term,value in index.items():
            postinglist=[]

            for p in value:
                lecID=p[0]
                tf=p[1]
                postinglist.append(':'.join([str(lecID), ','.join(map(str,tf))]))

            string= ''.join((term,'|',';'.join(postinglist)))

            #write to file
            f.write(f"{string}\n")

        f.close()
