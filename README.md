# Natural Language Processing
This repo contains examples for below points related to NLP in Python. 

### Tokenization
Break up the text into component pieces called "tokens". They are the <b>basic building block</b> of a document object.

### Stemming
Defines a keyword and then find variations to find relations between them. For example, when you search for "boat" might also returns: "boating", "boats". There are two main approaches: Porter & Snowball.

### Lemmatization
Lemma is another word reduction approach but based on a morphological analysis of the words. For example, the lemma of "meeting" might be is "meet" or can be "meeting" depending on it is use in a sentence.

### Stop Words
The words which appears frequently and they are not nouns, verbs or modifiers. This words do not require tagging.

### Pattern Matching
Defines patterns to find if they exists in the document.

### Phrase Matching
Defines patterns to find if they exists in the document.

### Part of speech "POS"
The context defines the meaning of the words. Same words in different order can mean something completely different.

### Named Entity Recognition (NER)
Locate and classify named entity mentions in unstructured text into predefined categories like person names, organizations, locations, medical codes, time expressions, monetary, quantity, percentages and so on.

### Feature Extraction
Use SKLearn to pre-process text based on the frequency of the words.

### Topic Modelling using LDA (Unsupervised Learning) & Non Negative Matrix
Classify large volumes of text by clustering documents into topics. Use LDA - Latent Dirichlet Allocation to group the words in clusters. 

### Semantic Analysis
VADER (Valence Aware Dictionary for Sentiment Reasoning) is a model to use in sentimental analysis which is sensitive to both polarity (positive or negative) and intensity of emotion. The "score" will be calculated summing the intensity of each word in the text (positive, negative, strong)


# Installation using pip

pip install -r requirements.txt 

python3 -m spacy download en_core_web_sm



