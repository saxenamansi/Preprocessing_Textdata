# Preprocessing_Textdata

The aim of this activity is to learn Core Python and Data Preprocessing. Consider the given movie review file which contains set of users and their positive and negative reviews. Do the following,
       
1. Read the Review Content from File and extract only reviews (Exclude user ids and sentiment polarity)
2. Tokenize each words(without removing stop words) and create a collection (dictionary) for each word and its occurrences.
3. Remove the stop words and duplicate words,  Also find the translated word of the tokens and store the result in the form of tuple into a new file. 
            E.g. Filename: result.txt
            (nice, अच्छा)
            (funny, मजेदार)

reviews.txt
1101|I like this movie, it is funny.|postive
1102|I hate this movie.|negative
1103|This was awesome! I really liked it.|positive
1104|Nice one. I love it.|positive
1105|This is a poor film by any standard.|negative
