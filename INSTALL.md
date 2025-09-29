# Installation Guide

## Development Installation

To install the package in development mode:

1. Clone the repository:
```bash
git clone <repository-url>
cd contact_card_reader
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Production Installation

To install the package from source:

```bash
pip install .
```

## Dependencies

The package requires Tesseract OCR to be installed on your system:

- **Windows**: Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)
- **macOS**: `brew install tesseract`
- **Linux**: `sudo apt-get install tesseract-ocr`

## Usage

After installation, you can use the CLI command:

```bash
contact-card-reader --help
contact-card-reader image.jpg
contact-card-reader /path/to/images/ --output results.csv --format csv
```

## Building Distribution Packages

To build distribution packages:

```bash
pip install build
python -m build
```

This will create `dist/` directory with wheel and source distribution files.
