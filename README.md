# QuickDoc
QuickDoc is a command-line tool that allows you to convert documents between different formats, such as DOCX to PDF, PDF to DOCX, and PPT to PDF. It leverages LibreOffice, the default office suite in many Linux distributions, for handling document conversions. QuickDoc supports searching for input files across the entire system and saves output files in the same directory as the input file, ensuring seamless and efficient document management.

I created QuickDoc because I found it frustrating that LibreOffice doesn't offer a direct option to convert PDF files to DOCX or other formats in my ubuntu. It was inconvenient to rely on websites for file conversions, so I developed this command-line tool to simplify the process. QuickDoc makes it easy to convert files directly from the terminal, saving time and effort.

## Features

- Convert DOCX files to PDF
- Convert PDF files to DOCX
- Convert PPT files to PDF
- Search for input files across the system
- Save output files in the same directory as the input file

## Requirements

- Python 3.x
- LibreOffice (for PPT to PDF and DOCX to PDF conversion)
- Required Python packages(will be automatically installed after you run the script):
  - `pdf2docx`
  - `docx2pdf`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/aarinz/Quickdoc.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Quickdoc
    ```

3. run these commands:

    ```bash
    chmod +x quickdoc.sh
    ./quickdoc.sh
    ```
## Usage

### General Command Structure

```bash
quickdoc <conversion_type> --i <input_file> --o <output_file>
```

## Example

```bash
quickdoc pdf2docx --i EX3.pdf --o EX3.docx
```

### If File name is with spaces

```bash
quickdoc pdf2docx --i "EX 3.pdf" --o "EX 3.docx"
```

