import argparse
import os
import glob
from pdf2docx import Converter as PDF2DOCXConverter
from docx2pdf import convert as DOCX2PDFConverter
import subprocess

def search_file(filename, search_path='/'):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def ppt_pdf(input_file, output_file):
    found_file = search_file(input_file)
    if found_file:
        try:
            subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', found_file], check=True)
            pdf_file = found_file.replace('.pptx', '.pdf')
            os.rename(pdf_file, output_file)
            print(f"Converted {found_file} to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {found_file} to PDF: {e}")
    else:
        print(f"No file found matching '{input_file}'")

def pdf_docx(input_file, output_file):
    found_file = search_file(input_file)
    if found_file:
        try:
            converter = PDF2DOCXConverter(found_file)
            converter.convert(output_file)
            print(f"Converted {found_file} to {output_file}")
        except Exception as e:
            print(f"Error converting {found_file} to DOCX: {e}")
    else:
        print(f"No file found matching '{input_file}'")

def docx_pdf(input_file, output_file):
    found_file = search_file(input_file)
    if found_file:
        try:
            DOCX2PDFConverter(found_file)
            pdf_file = found_file.replace('.docx', '.pdf')
            os.rename(pdf_file, output_file)
            print(f"Converted {found_file} to {output_file}")
        except Exception as e:
            print(f"Error converting {found_file} to PDF: {e}")
    else:
        print(f"No file found matching '{input_file}'")

def main():
    parser = argparse.ArgumentParser(description="QuickDoc CLI Tool")
    parser.add_argument('command', choices=['convert'], help='Command to execute')
    parser.add_argument('conversion_type', choices=['ppt2pdf', 'pdf2docx', 'docx2pdf'], help='Type of conversion')
    parser.add_argument('--input', required=True, help='Input file name')
    parser.add_argument('--output', required=True, help='Output file name')

    args = parser.parse_args()

    if args.command == 'convert':
        if args.conversion_type == 'ppt2pdf':
            ppt_pdf(args.input, args.output)
        elif args.conversion_type == 'pdf2docx':
            pdf_docx(args.input, args.output)
        elif args.conversion_type == 'docx2pdf':
            docx_pdf(args.input, args.output)

if __name__ == '__main__':
    main()
