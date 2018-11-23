# NLP-document-auto-clustering

Key features:

- Support most common document formats including pdf, word docx, powerpoint pptx, txt

- Auto-detection of file language

- NLP based POS tagging and word tokenization

- TF-IDF vecterization

- K-means clustering with auto K selection

- PCA and 2-D visualization

### Prerequisites

written with Python3.6.5 and tested under CentOS Linux release 7.5.1804 (Core) 

Note: some CentOS (7.5.1804) is not shipped with tkinter(required by pyplot), need to install it manually:

```
sudo yum install python36u-tkinter.x86_64
```

Other python dependencies can be found in requirement.txt

### How to run the code

The run.py file is under "/src" folder.  First install the pre-requisite packages, then use the following command line:

```
python3.6 run.py
```

the program will automatically start and finish the workflow

### Overall workflow

Step 1, open and parse all documents located inside "/src/files" folder 

a dedicated parser is used to parse any text from txt, docx, pptx, pdf files, return plain texts and file names

Step 2, determine document language

auto-detect language of file content using langdetect

Step 3, dealing with non-english files

there are several options to handle foreign language files

option 1. remove foreign languages and only keep English files for clustering study

option 2. perform separate clustering study, one for each language

Option 3. translate foreign language text to English (using goslate or similar package), then treat the traslated content as English text

Option 4. use word embedding to convert word space to abstract vector space (such as Word2Vec), then cluster files based on abstract vector space

currently support option 1, i.e. only cluster English files.  More features could be added in future to support other options.

Step 4, extract key words from text using POS

tokenize plain text with NLP tokenizer, use word-tokens to filter out the key words ("proper nouns" NNP as key words)

Step 5, stemming & lemmatization

reduce word-space by normalizing proper-noun words to stem form, first stemming, then lemmatization

Step 6, vectorize word space with tf-idf 

form overall corpus by combining file keywords, then vectorize word-space via tf-idf

Step 7, K-means clustering

auto select optimum K value using elbow method, with a pre-set threshold on elbow gradient

apply K-Means clustering with optimum k and find category label for each file

Note: The demo files have number of features less than 1000, dimension reduction is not necessary. If large number of features cause effeciency issues, PCA could be applied prior to K-means to reduce feature dimensions

Step 8, visualize clustering results in 2-D space

reduce feature dimension to 2-D using PCA

generate 2-D scatter plot visualization, each point represents one file, points are colored based on cluster category

Step 9, generate analysis report

An analysis.txt report is auto-generated and saved under "/src" folder, it contins all proccessed info and identified info of each document file, including file names, file languages, proper nouns found, and file clustering categories

### Acceptable file format in "files" folder

All files inside files" folder will be processed

Currently most common document formats are surpoorted, including:

.txt (utf-8)

.docx

.pdf

.pptx

incorrect file format may give errors

currently accept English, French and German files, other languages support can be added

### Example files for validation

Some example files are included under "src/files" for easy validation:

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

The word tokenization and K-means clustering did a good job to extract key words from files and cluster files based on content dimilarity

The 2-D visualization gives more intuitive illustration of clustering, nearby file points are grouped to same colors, suggesting sccessful clustering

### Discussion of future improvements

This project gives a preliminary demo of what can be done, several areas can be further improved:

the file parser can be imrpoved to accept more file formats and to include online text sources such as tweeter/wikipedia api

image text extraction module such as pytesseract can be added to the file parser to support parsing text from embedded images in files

currently the nltk POS tokenizer support English, it also works OK for most european languages, but the support for foreign languages still can be improved by adding dedicated modules for foreign languages

the current error handling mechanism could be improved, more error testings are needed

outlier detection/removal mechanism can be added before K-means to improve clustering accuracy












