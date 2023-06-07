This directory is used to process pdf files into a readable txt format that the model can accept.
converter.py contains the code to convert pdf files to txt files, and draws the parameters from config.py
To edit any parameters, simply check config.py and replace the arguments accordingly.

Sometimes the PDF files will lack the correct unicode character map, and we end up getting gibberish output like 
non-ascii characters and (cid:x), see below link. 
https://pdfminersix.readthedocs.io/en/latest/faq.html#why-are-there-cid-x-values-in-the-textual-output

In such a case the script will catch this and throw an exception. However, this can only be resolved by getting another
version of the pdf which has the character map. Sometimes the character map is removed from the document because the
PDF might be extracted pages from a larger PDF file (such as PC3131 College Physics 2e PDFs). The character mapping 
required to decode the correct text is in the original PDF, so we have to download the original PDF and specify which
relevant pages to extract.

The process for adding a new module's contents is simple, and is constructed to accept PDF files.
For example for PC3131 we have 2 sets of notes, College Physics 2e https://openstax.org/details/books/college-physics-2e
and the Sem 2 module notes. We simply create a folder in 'pdf_sources' called 'PC3131' and place the PDFs inside.
In config.py, we simply change pdf_filepath to "pdf_sources/PC3131/", or whichever folder name you have created.
The variable pdf_files specifies the names of the files, and the specific subset of pages which you want to extract, as
for the chatbot it is more efficient to extract distinct chapters which cover specific topics, instead of the entire
PDF at once. Follow the convention that is specified.

Once complete, open the command line and cd into the document_conversion directory (this one) and simply run the 
converter.py script from the command line with the following:
```
python converter.py
```
Alternatively you can right-click the script and run with python :)