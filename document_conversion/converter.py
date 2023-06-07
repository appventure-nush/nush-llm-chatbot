from pdfminer.high_level import extract_text
import config
import os
from os.path import dirname, normpath, basename, join, exists, splitext

if __name__ == "__main__":
    # create the destination directory for processed txt files
    output_docs_filepath = join('output_docs', basename(normpath(config.pdf_filepath)))
    print(f'Processing files into destination folder {output_docs_filepath}')
    if not exists(output_docs_filepath):
        os.makedirs(output_docs_filepath)

    # iterate through all source pdf files
    for filename, pages in config.pdf_files:
        # path to a source pdf file
        infile = open(join(config.pdf_filepath, filename), 'rb')
        # create equivalent txt file in output directory
        outfile = open(join(output_docs_filepath, splitext(filename)[0] + f'_pages{pages}.txt'),
                       'w', encoding='utf-8')
        print(f'Processing {infile.name}...')

        page_numbers = list(range(pages[0] - 1, pages[1])) if pages else None
        text = extract_text(infile, codec='utf-8', page_numbers=page_numbers)

        # checking if there are unparsable characters
        if '(cid:' in text:
            print(f'Warning, {outfile.name} contains unparsable characters, likely due to lack of character map in the'
                  f' PDF. Double check if file output has sufficient text converted for use.'
                  f' Check README for more details. ')

        outfile.write(text)

        infile.close()
        outfile.close()

'''


for filename in os.listdir(pdf_filepath):
    f = os.path.join(pdf_filepath, filename)
    reader = PdfReader(f)
    with open(os.path.join(output_docs_filepath, os.path.splitext(filename)[0] + '.txt'), 'w', encoding="utf-8") as f:
        for page in reader.pages:
            f.write(page.extract_text() + "\n")
'''