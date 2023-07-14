# these are configurations to change for the script to automatically convert pdfs to readable txt files

# filepath to the parent directory of source pdf files
pdf_filepath = "pdf_sources/PC3131/"

# mapping of files to the range of page numbers to extract
# An entry should be of form ('filename', (start, end))
# The tuple (start, end) starts from index 1, and ending is inclusive.
# For example: chapter 18 of college physics 2e begins at 791, and ends at 833 (based on the PDF page number, not the
# page number on the bottom right). Therefore, the range of page numbers would be (791, 833).
# If None is passed in place of the (start, end) tuple, the entire PDF will be converted to text.
# The same PDF can be passed in multiple times with different ranges, to retrieve different PC3131.
pdf_files = [
    # chapter 18 Electric Charge and Electric Field
    ('College_Physics_2e-WEB_7Zesafu.pdf', (791, 833)),
    # chapter 20 Electric Current, Resistance and Ohm's law
    ('College_Physics_2e-WEB_7Zesafu.pdf', (875, 920)),
    # chapter 21 Circuits and DC instruments
    ('College_Physics_2e-WEB_7Zesafu.pdf', (921, 969)),
    # chapter 22 Magnetism
    ('College_Physics_2e-WEB_7Zesafu.pdf', (971, 1019)),
    # Physics Notes
    ('Sem 2 Notes (Teachers version).pdf', None)
]
