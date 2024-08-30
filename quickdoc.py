import argparse
import os
import glob
from pdf2docx import Converter as PDF2DOCXConverter
from docx2pdf import convert as DOCX2PDFConverter
from pptx import Presentation
import subprocess

def ppt_pdf(input_file, output_file):
    try:
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', input_file], check=True)
        pdf_file = input_file.replace('.pptx', '.pdf')
        os.rename(pdf_file, output_file)
        print(f"Converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file} to PDF: {e}")

def pdf_docx(input_file, output_file):
    try:
        converter = PDF2DOCXConverter(input_file)
        converter.convert(output_file)
        print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file} to DOCX: {e}")

def docx_pdf(input_file, output_file):
    try:
        DOCX2PDFConverter(input_file, output_file)
        print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file} to PDF: {e}")

def search_files(search_pattern, search_path='.'):
    found_files = False
    print(f"Searching for files matching '{search_pattern}' in '{search_path}'...")
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if glob.fnmatch.fnmatch(file, search_pattern):
                print(os.path.join(root, file))
                found_files = True
    if not found_files:
        print("No files found matching the pattern.")

def main():
    parser = argparse.ArgumentParser(description='QuickDoc: A CLI tool for document conversion and file search.')
    subparsers = parser.add_subparsers(dest='command')

    convert_parser = subparsers.add_parser('convert', help='Convert files between formats.')
    convert_parser.add_argument('type', choices=['ppt2pdf', 'pdf2docx', 'docx2pdf'], help='Type of conversion.')
    convert_parser.add_argument('--input', required=True, help='Input file path.')
    convert_parser.add_argument('--output', required=True, help='Output file path.')

    search_parser = subparsers.add_parser('search', help='Search for files matching a pattern.')
    search_parser.add_argument('pattern', help='Filename pattern to search for.')
    search_parser.add_argument('--path', default='.', help='Directory path to start the search.')

    args = parser.parse_args()

    if args.command == 'convert':
        if args.type == 'ppt2pdf':
            ppt_pdf(args.input, args.output)
        elif args.type == 'pdf2docx':
            pdf_docx(args.input, args.output)
        elif args.type == 'docx2pdf':
            docx_pdf(args.input, args.output)
    elif args.command == 'search':
        print(f"Running search with pattern '{args.pattern}' in path '{args.path}'")
        search_files(args.pattern, args.path)

if __name__ == '__main__':
    main()
