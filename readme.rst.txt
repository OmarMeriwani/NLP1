Part 1: Tokenization, Part of speech
The (set) function used for finding the unique number of tokens (types). While WordNetLemmatizer used for lemmatization. Other techniques assessed during the work as well, including two types of stemmers. In addition, the difference between lemmatization and stemming. For part of speech tagging the Unigram tagger (UnigramTagger) used and trained using the entire news category from (brown) text in NLTK libraries. The reason behind using the news category is for the nature of the analyzed article. Although, multiple tagging errors were found and stated in the code, due to the limitation of the training data.
The article converted to text using the library of (html-to-text), while the other unwanted parts eliminated by understanding the general structure of “The guardian” articles, so a number of lines removed as well as the social media tags. All these details were documented in (tokentypes.py) file.
This questions answer and code finds that the number of words caught gets less after lower casing due to the increased similarity between the words. Moreover, it gets less after lemmatization, due to the change in the words.
Part 2: Regular expression:
Many tests applied to the phone numbers format until reaching a final approach that include: 
-	First part: either to be an international code prefix, zero or nothing.
-	Second part: First, I have proposed a method to get only the correct international code, that include a regular expression for the correct numbers only (see appendix.zip), but for expecting new international codes to appear even rarely, the method changed to accepting one to six digits number (see the national codes.txt file in Appendix.zip).
-	The third last part contains groups of numbers ranging from two to six, separated by either a space or a dash (-).
Solution exists in P1.py file
Part 3: N-gram models
Many libraries were tested to do this part, but finally, FreqDist was used for getting unigram counts, which were then divided by the total count. Laplace smoothing applied later to the resulting probabilities of FreqDist.
Some changes in text processing and tokens preparing happened for the bigram part. That includes keeping the ending and starting tags. ConditionalFreqDist used to get the counts of the bigram, and then the probability and it’s smoothing value done by depending on the unigram values.
