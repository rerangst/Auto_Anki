from bs4 import BeautifulSoup
import random

parsed_html = BeautifulSoup(open('source/index.html'),features="html.parser")

lsSpan = parsed_html.body.find_all('p', attrs={'class':'block_2'})
# print(len(lsSpan))
lsLine = []
for i,span in enumerate(lsSpan):
    out = span.text
    noteIdx=''
    if not isinstance(span.contents[-1], str):
        if span.contents[-1].text.isdigit():
            noteIdx= span.contents[-1].text
            hrefID= span.contents[-1].contents[-1]['href']
            hrefID = hrefID.replace('#','')
            noteText = parsed_html.body.find("dl", {"id": hrefID}).text
            # break
    out= out.replace(noteIdx,'')
    lsLine.append(out)

    print(i+1,":  ",out)
    lsWord = out.split()
    numberOfCloze = int(len(lsWord)/3)
    randomWords =random.sample(lsWord,numberOfCloze)
    for word in randomWords:
        out = out.replace(word, "{{c1::"+word+"}}")
