"""
Contact Card Reader Package.

A CLI application that extracts text from contact card images using OCR.
"""

__version__ = "1.0.0"
__author__ = "Contact Card Reader Team"

from .main import ContactCardReader, main
from .image_loader import ImageLoader

__all__ = ["ContactCardReader", "ImageLoader", "main"]
