import PyPDF2

with open("/Users/smenezes/downloads/study_guide.pdf","rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("rotated.pdf","wb") as output:
        writer.write(output)
    
    merger = PyPDF2.PdfFileMerger()
    file_names = ["rotated.pdf","study_guide.pdf"]

    for file_name in file_names:
        merger.append(file_name)
    merger.write("combined.pdf")