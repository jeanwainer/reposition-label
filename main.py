import sys
from PyPDF4.pdf import PdfFileReader, PdfFileWriter

def space_pdf(filename):
    output_filename = filename[:-4].lower() + '_result.pdf'

    pdf = PdfFileReader(open(filename, 'rb'))
    output = PdfFileWriter()
    for page in pdf.pages:
        new_page = output.addBlankPage(page.mediaBox.getWidth(), page.mediaBox.getHeight())

        half_width = page.mediaBox.getWidth() / 2
        height = page.mediaBox.getHeight()
        page.trimBox.upperRight = (half_width, height)
        page.cropBox.upperRight = (half_width, height)
        new_page.mergeTranslatedPage(page, half_width, 0)

    outputStream = open(output_filename, "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ == '__main__' and sys.argv[1][-3:].upper() == 'PDF':
    filename = sys.argv[1]
    space_pdf(filename)

else:
    print('EXAMPLE: pdfcrop.py label.pdf')