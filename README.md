# NLP-document-auto-clustering
text extraction and clustering using POS tokenization, TF-IDF, PCA and K-means

### Prerequisites

written and tested with Python3.6.5 and CentOS Linux release 7.5.1804 (Core) 

Note some CentOS (7.5.1804) is not shipped with tkinter(required by pyplot), need to install it manually:

```
sudo yum install python36u-tkinter.x86_64
```

Other required python dependencies are listed in requirement.txt

### How to run the code

Install the pre-requisite packages, then use the following command line:

```
python3 run.py
```

the program will automatically start the workflow

### Overall workflow

Step 1, load all documents under "files" folder 

(calling load_files.py, parse_pdf.py , parse_word.puy, parse_pptx.py)

open files and parse plain text, return plain texts and file names


Step 2, extract and print phone number

(calling parse_phone.py)

use regex to extract phone nuber from plain texts, print out phone number if found


Step 3, determine document language

(calling get_language.py)

detect language of text string (using langdetect). To speed-up for large files, only use first 1000 characters to decide file language 


Step 4, dealing with non-english files

Here we need to make a decision, how to handle German and French files

Since majority of files are in Englih, minority German and French files will become outliers when we do tf-idf based clustering study (french/german files have no word match with majority of word-space). 

There are several options to resolve this:

1. We can remove french and german files from clustering study(somewhat equivalent to removing outliers)

2. we can do 3 separate clustering study, one for each language

3. we can translate German/French text to English (using goslate or similar package), then treat the traslated content as English text

4. we can do word embedding to convert words to abstract vectors (such as word2Vec), then the actual spelling of words won't matter, if we do clustering in abstract vector space.  (need word embedding modules that support French and German)

For simplicity reason, this excercise will only do option 1, i.e. only cluster English files and ignore other language files


Step 5, extract proper nouns using POS

(calling proper_nouns.py)

tokenize the plain text to word-tokens(using nltk.tokenize), only keep proper nouns (labeled NNP) and remove the rest
 

Step 6, stemm & lemma

(calling stemm_lemma.py)

normalize proper-noun words to stem form (using nltk.stem), first stemming, then lemmatization


Step 7, vectorize word space with tf-idf 

(calling tfidf.py)

combine remaining nouns of all files to create corpus, then vectorize the word-space via tf-idf (using sklearn TfidfVectorizer)


Step 8, K-means clustering

(calling auto-cluster.py)

To do K-means, first we need to decide the optimum K value

The script will auto-detect optimum k using elbow method, with a pre-set threshold on elbow gradient:

see https://en.wikipedia.org/wiki/Elbow_method_(clustering)

We apply K-Means with optimum k and find category label of each file

Note: The number of features in word-space is less than 1000, dimension reduction is not necessary. However if feature number is too large, we may use PCA to reduce features before doing K-means


Step 9, visualize clustering results in 2-D space

(calling pca.py)

first reduce feature dimension to 2 using PCA (n=2)

generate 2-D scatter plot, each point represents one file, points are colored based on cluster category


Step 10, generate analysis report

generate and save "analysis.txt" to src folder


### Acceptable file format in "files" folder

All files inside files" folder will be processed by the script

Acceptable file formats include:

.txt (utf-8 only, currently do not support utf-16 or other)

.docx (only parse plain text, can not extract text from images) 

.pdf (only parse plain text, can not extract text from images)

.pptx (only parse plain text, can not extract text from images)

Other file formats will report error

Currently only accept English, French and German files. Other languages may report error

### Example files for validation

Some example files are provided in "files" folder for easy validation:

9 separate chapters of Shelock-Holmes,		.txt (utf-8) format

21 separate chapters of Pride-and-Prejudice,		.txt (utf-8) format

20 separate chapters of Tale-of-Two-Cities,		.txt (utf-8) format

20 separate chapters of The-Adventures-of-Tom-Sawyer,		.txt (utf-8) format

4 separate chapters of a random French book,		.txt (utf-8) format

3 separate chapters of a random German book,		.txt (utf-8) format

4 random texts related to finance and banking ,		.txt (utf-8) format

1 powerpoint slide file related to the book of Tom-Sawyer ,	.pptx format

1 pdf file related to pride and prejudice, the movie,	 .pdf format

1 txt file containing some random text and Singapore phone numbers	.txt (utf-8) format

In total about 80 files


### Discussion of results

The validation files in general fall into 5 broad categories (ignoring French and German books):

Tom Sayer

Pride and Prejudice

Tale of Two Cities

Shelock Holmes

Finance & credit

The K-means clustering did a good job to associate files to their correct categories.  All chapters related to a same book are clustered together.

All texts describing finacial credit and credit risks are clustered together.

Even the pdf file describing movie plot of pride and prejudice movie is clustered correctly with its book chapters.

The 2-D visualization shows nearby file points are labeled with same color, giving us a hint that the clustering is quite successful.

In 2-D visualization there appears to be some outlier points very far from the other points, these may or may not be actual outliers, because we have lost some information when collapsing high dimensional word-space into 2-D,  in the original word-space these "outlier" points may be quite close to other points, but it's difficult to visualize in the original word-space.

### Discussion of future improvements

This project only gives a preliminary demo of what can be done, many things can be improved:

the file parser only accept .pdf .txt .docx .pptx formats,  more robust parsers can be built to accept more file formats and wikipedia / tweet api

the parser can not process images in files, may include modules to extract text from image (such as pytesseract)

the nltk.tokenize POS tagger only support English, it works OK-ish for some european languages, may find better tools to tokenize French and German etc. if we cluster French/German files

the regex can be improved to better parse international phone numebrs

there is no error handling mechanism, may need more error testing and improve error handling

there is no outlier detection/removal mechanism before doing K-means.  The input files are selected by hand, so there are very few outliers and K-means work ok.  However, if large amount of random/messy files are used, the K-means algorithm can be quite sensitive to extreme outliers, and clustering accuracy may be low.

to improve this we can try to add some mechanism to detect outliers, such as :
https://pdfs.semanticscholar.org/4c68/4a9ba057fb7e61733ff554fe2975a2c91096.pdf

or use more robust clustering method that's more immune to outliers, such as K-median instead of K-means(but computation effeciency may be low due to the sort in K-median)












