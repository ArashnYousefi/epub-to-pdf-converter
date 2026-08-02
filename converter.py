import os
import fitz


def convert_epub_to_pdf(epub_path, pdf_path):
    """Convert a single EPUB file to PDF using PyMuPDF."""
    try:
        # Opening the EPUB document
        doc = fitz.open(epub_path)
        # Converting the document to a PDF bytes object
        pdf_bytes = doc.convert_to_pdf()
        # Saving the PDF
        with open(pdf_path, "wb") as pdf_file:
            pdf_file.write(pdf_bytes)

        print(
            f"✓ Converted: {os.path.basename(epub_path)} -> {os.path.basename(pdf_path)}")

    except Exception as e:
        print(f"✗ Failed to convert {epub_path}: {e}")


def batch_convert():
    """Find all .epub files in the current directory and convert each to PDF."""
    # Getting the current working directory
    current_dir = os.getcwd()

    # Finding all files ending with .epub
    epub_files = [f for f in os.listdir(
        current_dir) if f.lower().endswith('.epub')]

    if not epub_files:
        print("No .epub files found in the current directory.")
        return

    print(f"Found {len(epub_files)} EPUB file(s). Converting...")
    for epub_file in epub_files:
        # Creating the PDF filename by replacing the extension
        pdf_file = os.path.splitext(epub_file)[0] + ".pdf"
        convert_epub_to_pdf(epub_file, pdf_file)


if __name__ == "__main__":
    batch_convert()
