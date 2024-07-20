import PyPDF2

# get text from pdf
filename = "owasp-api-security-top-10.pdf"
with open(filename, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.getNumPages()

    print(f"Number of pages in {filename}: {num_pages}")

    # get the first page
    page = pdf_reader.getPage(2)
    print(page)
    print('Page type: {}'.format(str(type(page))))
    text = page.extractText()
    print(text)

    # reading all the pages content one by one
    # for page_num in range(pdf_reader.numPages):
    #    pdf_page = pdf_reader.getPage(page_num)
    #    print(pdf_page.extractText())

# Extract pdf info
with open(filename, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    print(f'Number of Pages in PDF File is {pdf_reader.getNumPages()}')
    #print(f'PDF Metadata is {pdf_reader.documentInfo}')
    try:
        print(f'PDF File Title is {pdf_reader.documentInfo["/Title"]}')
        print(f'PDF File Author is {pdf_reader.documentInfo["/Author"]}')
        print(f'PDF File Creator is {pdf_reader.documentInfo["/Creator"]}')
    except Exception as e:
        print(f'Issue while fetching pdf info :{e}')

