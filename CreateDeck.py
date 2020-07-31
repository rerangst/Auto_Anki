#!/usr/bin/env python3

import csv
import random
import genanki
# lsSpan=[]
lsText=[]
def createText(frontText):
    lsWord = frontText.split()
    numberOfCloze = int(len(lsWord)/3)
    randomWords =random.sample(lsWord,numberOfCloze)
    for word in randomWords:
        frontText = frontText.replace(word, "{{c1::"+word+"}}")
    return frontText

def createBackExtra(lsSpan, parsed_html):
    resultNote =''
    for i,span in enumerate(lsSpan):
        if not isinstance(span.contents[-1], str):
            if span.contents[-1].text.isdigit():
                noteIdx= span.contents[-1].text
                hrefID= span.contents[-1].contents[-1]['href'].replace('#','')

                noteText = parsed_html.body.find("dl", {"id": hrefID}).text
                noteText= noteText.replace("[←"+noteIdx+"]",'')
                resultNote= resultNote+ "<br>" + "<div>" + noteText + "</div>"
    return resultNote

# Filename of the data file
# data_filename = "HSK Official With Definitions 2012 L1.txt"

# Filename of the Anki deck to generate
deck_filename = "TruyenKieu.apkg"

# Title of the deck as shown in Anki
anki_deck_title = "Doan Truong Tan Thanh"

# Name of the card model
anki_model_name = "Cloze_m4tbi3c"

# Create the deck model

model_id = random.randrange(1 << 30, 1 << 31)

style = """
.card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}

.cloze {
 font-weight: bold;
 color: blue;
}
.nightMode .cloze {
 color: lightblue;
}

"""

anki_model = genanki.Model(
    model_id,
    anki_model_name,
    fields=[{"name": "Text"}, {"name": "Back Extra"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": '{{cloze:Text}}',
            "afmt": '{{cloze:Text}}<br><hr>{{Back Extra}}',
        },        
    ],
    css=style,
)

# The list of flashcards
anki_notes = []

from bs4 import BeautifulSoup

# html = #the HTML code you've written above
parsed_html = BeautifulSoup(open('source/index.html'),features="html.parser")

# lsSpan = parsed_html.body.find_all('span')
lsSpan = parsed_html.body.find_all('p', attrs={'class':'block_2'})
# print(len(lsSpan))
for i,span in enumerate(lsSpan):
    out = span.text
    # out = str(span).replace(a.split(' ')[3], "{{c1::"+a.split(' ')[3]+"}}")
    # out = a.replace(a.split(' ')[3], "{{c1::"+a.split(' ')[3]+"}}")
    if not isinstance(span.contents[-1], str):
        if span.contents[-1].text.isdigit():
            noteTxt = str(span.contents[-1])
            noteTxt = span.contents[-1].text
            out = out.replace(noteTxt,'')
    lsText.append(out)
for i in range(0,len(lsSpan),5):
    backText=''
    frontText=''
    if i<3250:
        for j in range(5):
            frontText =frontText + "<div>" + createText(lsText[i+j]) + "</div>"
        for j in range(10):
            if i+j<len(lsText):
                backText =backText + "<div>"+ lsText[i+j] + "</div>"
                # print(lsText[i+j])
        backText = backText+ "<br>" +"<div>" + createBackExtra(lsSpan[i:i+4],parsed_html)+"</div>"
        # print("----------------------------------------")
        anki_note = genanki.Note(
            model=anki_model,
            # simplified writing, pinyin, meaning
            fields=[frontText, backText],
        )
        # if i==200:
        #     break
        anki_notes.append(anki_note)

# a =createBackExtra(lsSpan[0:5],parsed_html)
# Shuffle flashcards
# random.shuffle(anki_notes)
for i in range(12):
    if i==0:
        deck_filename = "TruyenKieu_I.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::I")
        lsNote= anki_notes[0:7]
    if i==1:
        deck_filename = "TruyenKieu_II.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::II")
        lsNote= anki_notes[7:48]
    if i==2:
        deck_filename = "TruyenKieu_III.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::III")
        lsNote= anki_notes[48:113]
    if i==3:
        deck_filename = "TruyenKieu_IV.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::IV")
        lsNote= anki_notes[113:155]
    if i==4:
        deck_filename = "TruyenKieu_V.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::V")
        lsNote= anki_notes[155:254]
    if i==5:
        deck_filename = "TruyenKieu_VI.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::VI")
        lsNote= anki_notes[254:340]
    if i==6:
        deck_filename = "TruyenKieu_VII.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::VII")
        lsNote= anki_notes[340:398]
    if i==7:
        deck_filename = "TruyenKieu_VIII.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::VIII")
        lsNote= anki_notes[398:432]
    if i==8:
        deck_filename = "TruyenKieu_IX.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::IX")
        lsNote= anki_notes[432:529]
    if i==9:
        deck_filename = "TruyenKieu_X.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::X")
        lsNote= anki_notes[529:547]
    if i==10:
        deck_filename = "TruyenKieu_XI.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::XI")
        lsNote= anki_notes[547:593]
    if i==11:
        deck_filename = "TruyenKieu_XII.apkg"
        anki_deck = genanki.Deck(model_id, anki_deck_title+"::XII")
        lsNote= anki_notes[593:649]

    anki_package = genanki.Package(anki_deck)
    # Add flashcards to the deck
    for anki_note in lsNote:
        anki_deck.add_note(anki_note)

    # Save the deck to a file
    anki_package.write_to_file(deck_filename)

    print("Created deck {0} with {1} flashcards".format(deck_filename, len(anki_deck.notes)))