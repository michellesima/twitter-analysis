import csv
import numpy as np
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import sentiment_mod as s

def process(text,array, spamwriter):
      sentiment_value, confidence = s.sentiment(text)
      if confidence > 0.65:
         array = np.append(array, sentiment_value)
      else:
         array = np.append(array, "neutral")
      spamwriter.writerow(array)   
         
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    with open('wordtype.csv', newline='') as csvfile2:
     reader1 = csv.reader(csvfile2)
     for row in reader1:
        myarray0 = np.asarray(row)
        twitter = myarray0[2].lower()
        process(twitter, myarray0, spamwriter)

print("finish")