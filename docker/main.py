import os
from textractor import Textractor
from pprint import pprint

directory = '/images'
filelist = []
resultfile = open("/images/result.txt","w")

for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
         filelist.append(os.path.join(directory, filename))
filelist.sort()

extractor = Textractor(profile_name="default")

for fileitem in filelist:
    print(fileitem)
    resultfile.write('-----[ ' + fileitem + ' ]-----\n')
    document = extractor.detect_document_text(fileitem)
    resultfile.write(document.text)
    resultfile.write('\n')

resultfile.close()
