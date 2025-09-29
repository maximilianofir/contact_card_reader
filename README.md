# Contact Card Reader

A CLI application that extracts text from contact card images using OCR (Optical Character Recognition).

## Features

- Extract text from single images or batch process directories
- Multiple output formats: terminal display, text file, or CSV file
- Image preprocessing for better OCR accuracy
- Support for common image formats (JPG, PNG, BMP, TIFF)

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR:
   - **Windows**: Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

## Usage

### Basic Usage

Process a single image:
```bash
python contact_card_reader.py image.jpg
```

Process all images in a directory:
```bash
python contact_card_reader.py /path/to/images/
```

### Output Options

Print results to terminal (default):
```bash
python contact_card_reader.py image.jpg --print
```

Save to text file:
```bash
python contact_card_reader.py image.jpg --output results.txt
```

Save to CSV file:
```bash
python contact_card_reader.py /path/to/images/ --format csv --output results.csv
```

### Command Line Arguments

- `input_path`: Path to image file or directory containing images
- `--output, -o`: Output file path (optional)
- `--format, -f`: Output format - 'text' or 'csv' (default: text)
- `--print, -p`: Print results to terminal (default behavior)

## Examples

```bash
# Process single image and display results
python contact_card_reader.py tests/images/IMG_3780.jpg

# Process directory and save to CSV
python contact_card_reader.py tests/images/ --format csv --output contact_cards.csv

# Process directory and save to text file
python contact_card_reader.py tests/images/ --output extracted_text.txt
```

## Testing

Run the test suite:
```bash
python test_image_loader.py
```

## Dependencies

- opencv-python: Image processing and preprocessing
- Pillow: Image handling for OCR
- pytesseract: OCR engine wrapper
- Tesseract OCR: The actual OCR engine (system dependency)

## Notes

- The application automatically preprocesses images for better OCR accuracy
- Supported image formats: JPG, JPEG, PNG, BMP, TIFF
- Results include file path, extracted text, and timestamp
- CSV output includes separate columns for file path, filename, text, and timestamp
