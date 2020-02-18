import os
import sys
import re
import time
import PyPDF2
import numpy as np

def getPageCount(pdf_file):

    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.numPages
    return pages

def extractData(pdf_file, page):

    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    data = pageObj.extractText()
    return data


def isvalid(word, common_words_set):
    if word in common_words_set:
        return False
    if len(word) <= 3:
        return False
    if len(word) >= 15:
        return False
    if '.' in word:
        return False

    return True


def create_distances(dist_mat, words_list, paper_names, n):

    invalid = []
    i = -1
    for pdfFile in os.listdir('papers/'):
        if not pdfFile.endswith(".pdf"):
            continue
        i += 1
        print(str(pdfFile))

        # count the words in the pdf file
        word_dict = {}
        numPages = getPageCount('papers/'+pdfFile)
        for l in range(numPages):
            print(l, numPages)
            text = extractData('papers/'+pdfFile, l)
            # text = text.split()
            # for word in text:
            for j, match_word in enumerate(words_list):
            #         print(f'finding {match_word} in {word}')
            #         print(type(match_word))
            #         print(type(word))
            #         if match_word in str(word):
            #             dist_mat[i, j] += 1
                count = text.count(match_word)
                if count > 0:
                    print(match_word, str(pdfFile))
                    dist_mat[i, j] += text.count(match_word)

        counts = np.sum(dist_mat[i, :])
        if counts < 5:
            invalid.append([str(pdfFile), counts])

        time.sleep(1)
    with open("dist_mat.txt", "w") as f:
        f.write(','.join(paper_names))
        f.write('\n')
        np.savetxt(f, np.transpose(dist_mat).astype(int), fmt='%i', delimiter=",")
    print(dist_mat)

    return invalid


if __name__ == '__main__':

    paper_names = []
    invalid = []
    words_list = list(open("words.txt"))
    p = len(words_list)
    n = 0
    # Count number of pdfs
    for file in os.listdir('papers/'):
        if file.endswith(".pdf"):
            n += 1
            paper_names.append(str(file))
            # Check file is readable
            try:
                extractData('papers/'+file, 0)
                extractData('papers/'+file, 1)
            except Exception as e:
                invalid.append(str(file))

    if len(invalid) > 0:
        print("Remove invalid papers (unable to read first two pages):")
        for text in invalid:
            print(text)
        raise SystemExit

    # Get word counts from pdfs
    dist_mat = np.zeros((n, p), dtype=int)
    invalid2 = create_distances(dist_mat, words_list, paper_names, n)
    if len(invalid2) > 0:
        print("Remove invalid papers: (Number of word matches < 5)")
        for text in invalid2:
            print(text)
        raise SystemExit



    # references
    # https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt
    # https://github.com/adityashrm21/Pdf-Word-Count
    # elements of statistical learning
    # wget -e robots=off -H --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" -r -l 1 -nd -A pdf http://scholar.google.com/scholar?q=filetype%3Apdf+statistical+learning&btnG=&hl=en&as_sdt=0%2C23
