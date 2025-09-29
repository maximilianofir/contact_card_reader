# Contact Card Reader

A CLI application that extracts text from contact card images using OCR (Optical Character Recognition).

## Features

- Extract text from single images or batch process directories
- Multiple output formats: terminal display, text file, or CSV file
- Image preprocessing for better OCR accuracy
- Support for common image formats (JPG, PNG, BMP, TIFF)

## Installation

### From Source

1. Clone the repository and install the package:
```bash
git clone <repository-url>
cd contact_card_reader
pip install -e .
```

2. Install Tesseract OCR:
   - **Windows**: Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

### Development Installation

For development, install in editable mode:
```bash
pip install -e .
```

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

## Usage

### Basic Usage

Process a single image:
```bash
contact-card-reader image.jpg
```

Process all images in a directory:
```bash
contact-card-reader /path/to/images/
```

### Output Options

Print results to terminal (default):
```bash
contact-card-reader image.jpg --print
```

Save to text file:
```bash
contact-card-reader image.jpg --output results.txt
```

Save to CSV file:
```bash
contact-card-reader /path/to/images/ --format csv --output results.csv
```

### Command Line Arguments

- `input_path`: Path to image file or directory containing images
- `--output, -o`: Output file path (optional)
- `--format, -f`: Output format - 'text' or 'csv' (default: text)
- `--print, -p`: Print results to terminal (default behavior)

## Examples

```bash
# Process single image and display results
contact-card-reader tests/images/generated_card.png

# Process directory and save to CSV
contact-card-reader tests/images/ --format csv --output contact_cards.csv

# Process directory and save to text file
contact-card-reader tests/images/ --output extracted_text.txt
```

## Testing

Run the test suite:
```bash
# Run unit tests
python tests/test_image_loader.py

# Run application tests
python tests/test_application.py
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
