# NLP-document-auto-clustering

written in Python3.6.5 and tested in CentOS Linux release 7.5.1804 (Core); (partially tested in Ubuntu 16.0.4 )

### Drop any document files into  "/src/files" folder and this script will auto analyse and cluster files based on their related topics

Key features:

- Support most document formats including pdf, word docx, powerpoint pptx, txt

- Auto-detection of file language

- NLP based file processing and feature extraction (POS tagging and tokenization)

- Visualization of file clustering results

### Prerequisites

Python dependencies can be found in requirement.txt

Note: some CentOS (7.5.1804) is not shipped with tkinter(required by pyplot), need to install it manually:

```
sudo yum install python36u-tkinter.x86_64
```

### How to run the code

The run.py file is under "/src" folder.  First install the pre-requisite packages, then use the following command line:

```
python3.6 run.py
```

the program will automatically start and finish the workflow

### Overall workflow

The overall workflow includes file parser => language detect => process foreign language files => NLP POS tokenization and word filtering => stemming/lemmatization => vecterize word space (tf-idf) => k-means clustering => visualize results

Below are step by step detailed descriptions

Step 1, a dedicated parser is used to parse any text from txt, docx, pptx, pdf files, return plain texts and file names

Step 2, auto-detect language of file content using langdetect

Step 3, there are several options to handle foreign language files

option 1. remove foreign languages and only keep English files for clustering study

option 2. perform separate clustering study, one for each language

Option 3. translate foreign language text to English (using goslate or similar package), then treat the traslated content as English text

Option 4. use word embedding to convert word space to abstract vector space (such as Word2Vec), then cluster files based on abstract vector space

currently support option 1, i.e. only cluster English files.  More features could be added in future to support other options.

Step 4, tokenize plain text with NLP tokenizer, use word-tokens to filter out the key words ("proper nouns" NNP as key words)

Step 5, reduce word-space by normalizing proper-noun words to stem form, first stemming, then lemmatization

Step 6, form overall corpus by combining file keywords, then vectorize word-space via tf-idf

Step 7, auto select optimum K value using elbow method, with a pre-set threshold on elbow gradient

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

### Demo files for clustering

Some example files are included under "src/files" for easy validation

### Discussion of future improvements

- This project gives a preliminary demo of finding patterns among unstructured random files using NLP, the code is preliminary and several areas can be improved in future:

- more features could be added to the file parser to support more input file formats, web apis could also be added to allow parsing and clustering of online contents 

- image OCR text extraction module such as pytesseract could be implemented to the file parser to support parsing text from embedded images in pdf, pptx and word docx

- currently the nltk POS tokenizer has native support for English, some other european languages has been tested and it works ok, the support for foreign language can be improved by using dedicated POS tokenizers for particular language

- outlier detection/removal mechanism can be added before K-means to improve clustering accuracy

- the current error handling mechanism could be improved, more error testings are needed

