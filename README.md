# NLP-document-auto-clustering
NLP auto text extraction and clustering using document parsers, POS tokenization, TF-IDF, PCA and K-means

### Prerequisites

written with Python3.6.5 and tested under CentOS Linux release 7.5.1804 (Core) 

Note: some CentOS (7.5.1804) is not shipped with tkinter(required by pyplot), need to install it manually:

```
sudo yum install python36u-tkinter.x86_64
```

Other python dependencies can be found in requirement.txt

### How to run the code

First install the pre-requisite packages, then use the following command line:

```
python3.6 run.py
```

the program will automatically start and finish the workflow

### Overall workflow

Step 1, open and parse all documents located inside "files" folder 

a dedicated parser is used to parse plain text from txt, docx, pptx, pdf files, return plain texts and file names

Step 2, determine document language

auto-detect language of text string (using langdetect)

Step 3, dealing with non-english files

there are several options to handle foreign language files

If majority of files are in Englih, minority foreign language files will become outliers after tf-idf, (eg those french/german files will have no word match with majority of word-space). 

There are several options to resolve this:

1. We can remove french and german files from clustering study(somewhat equivalent to removing outliers)

2. we can do 3 separate clustering study, one for each language

3. we can translate German/French text to English (using goslate or similar package), then treat the traslated content as English text

4. we can do word embedding to convert words to abstract vectors (such as word2Vec), then the actual spelling of words won't matter, if we do clustering in abstract vector space.  (need word embedding modules that support French and German)

Currently support option 1, i.e. only cluster English files and ignore other language files.  More features could be added to support other options.

Step 4, extract proper nouns using POS

tokenize plain text to get word-tokens, only keep proper nouns for clustering analysis and discard unimportant words

Step 5, stemming & lemmatization

reduce word-space by normalizing proper-noun words to stem form, first stemming, then lemmatization

Step 6, vectorize word space with tf-idf 

first form corpus by combine file proper nouns, then vectorize via tf-idf (sklearn TfidfVectorizer)

Step 7, K-means clustering

first auto-detect optimum K value using elbow method, with a pre-set threshold on elbow gradient: see https://en.wikipedia.org/wiki/Elbow_method_(clustering)

then apply K-Means using optimum k to find category label of each file

Note: The demo files have number of features less than 1000, dimension reduction is not necessary. However if feature number is too large, PCA maybe applied prior to k-means to reduce features dimensions

Step 8, visualize clustering results in 2-D space

to visualize in 20D, first need to reduce feature dimension to 2 using PCA

then generate 2-D scatter plot with pyplot, each point represents one file, points are colored based on cluster category

Step 9, generate analysis report

An analysis.txt report is auto-generated and save to src folder, it contins all proccessed and identified info for each file, including file name, file language, proper nouns found, and clustering category

### Acceptable file format in "files" folder

All files inside files" folder will be processed by the script

Currently most commonly found document formats can be surpoorted, including:

.txt (utf-8)

.docx

.pdf

.pptx

incorrect file format may give rise to errors

Currently accept English, French and German files. Other languages support can be added

### Example files for validation

Some example files are provided under "src/files" for easy validation:

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

The word tokenization and K-means clustering did a good job to find key words and cluster files based on content.\

All chapters related to the same topics are clustered correctly.

Even the pdf file describing movie plot of "pride and prejudice" movie is clustered correctly with its book chapters.

The 2-D visualization also gives illustration of clustering success, all nearby file points are labeled with same color, suggesting strongly that clustering algorithm did group similar points together

### Discussion of future improvements

This project only gives a preliminary demo of what can be done, several areas can be improved in future:

the file parser only accept .pdf .txt .docx .pptx formats,  more robust parsers can be built to accept more file formats and online text source text feeds such as tweeter or wiki api

currently the parser can not process image contents in files, may add modules to extract text from image (such mudoles such as pytesseract)

the nltk.tokenize POS tagger only support English, it works OK-ish for some european languages, but may need to find better tokenizers to better support French and German files\

the error handling mechanism could be improved, more error hangling tests are required

an outlier detection/removal mechanism can be added before K-means












