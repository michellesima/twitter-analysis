import csv
import numpy as np
import nltk
import sentiment_mod as s

test_sample = open("negative1.txt", "r")
total = 0.0

correct = 0.0
notsure = 0.0
for line in test_sample:
   sentiment_value, confidence = s.sentiment(line)
   total = total + 1.0
   if confidence > 0.65:
      if sentiment_value == "neg":
         correct = correct + 1.0
   else:
      notsure = notsure + 1.0 
      
   
accu = correct / (total - notsure)
print("sample of", total)
print("accuracy = ", accu)
print("percent unsure = ", notsure / total)