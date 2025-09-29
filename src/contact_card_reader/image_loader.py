"""
Image loader module for contact card text extraction.
Handles loading and processing images using OCR.
"""

import cv2
import numpy as np
from PIL import Image
import pytesseract
import os
from typing import Optional, Tuple


class ImageLoader:
    """Handles loading and preprocessing images for OCR."""
    
    def __init__(self):
        """Initialize the image loader."""
        self.tesseract_config = '--oem 3 --psm 6'
    
    def load_image(self, image_path: str) -> Optional[np.ndarray]:
        """
        Load an image from file path.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Loaded image as numpy array or None if failed
        """
        try:
            if not os.path.exists(image_path):
                print(f"Error: Image file not found: {image_path}")
                return None
            
            # Load image using OpenCV
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error: Could not load image: {image_path}")
                return None
            
            return image
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            return None
    
    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """
        Preprocess image for better OCR results.
        
        Args:
            image: Input image as numpy array
            
        Returns:
            Preprocessed image
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Apply threshold to get binary image
        _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Morphological operations to clean up the image
        kernel = np.ones((2, 2), np.uint8)
        cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        
        return cleaned
    
    def extract_text(self, image: np.ndarray) -> str:
        """
        Extract text from preprocessed image using OCR.
        
        Args:
            image: Preprocessed image as numpy array
            
        Returns:
            Extracted text as string
        """
        try:
            # Convert numpy array to PIL Image for pytesseract
            pil_image = Image.fromarray(image)
            
            # Extract text using pytesseract
            text = pytesseract.image_to_string(pil_image, config=self.tesseract_config)
            
            # Clean up the text
            cleaned_text = self._clean_text(text)
            
            return cleaned_text
        except Exception as e:
            print(f"Error extracting text: {e}")
            return ""
    
    def _clean_text(self, text: str) -> str:
        """
        Clean extracted text by removing extra whitespace and empty lines.
        
        Args:
            text: Raw extracted text
            
        Returns:
            Cleaned text
        """
        # Remove extra whitespace and normalize line breaks
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        return '\n'.join(lines)
    
    def process_single_image(self, image_path: str) -> str:
        """
        Complete pipeline to process a single image and extract text.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Extracted text from the image
        """
        # Load image
        image = self.load_image(image_path)
        if image is None:
            return ""
        
        # Preprocess image
        processed_image = self.preprocess_image(image)
        
        # Extract text
        text = self.extract_text(processed_image)
        
        return text
