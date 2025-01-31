from pypdf import PdfReader

# Load the PDF
reader = PdfReader("data/grades_graphframes.pdf")

# Extract text from all pages
text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

# Write it to a text file
with open("data/grades_graphframes.txt", "w") as f:
    f.write(text)
