"""
Contact Card Reader CLI Application.
Extracts text from contact card images using OCR.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List, Dict
import csv
from datetime import datetime

from .image_loader import ImageLoader


class ContactCardReader:
    """Main application class for processing contact card images."""
    
    def __init__(self):
        """Initialize the contact card reader."""
        self.image_loader = ImageLoader()
        self.results = []
    
    def process_single_file(self, file_path: str) -> Dict[str, str]:
        """
        Process a single image file.
        
        Args:
            file_path: Path to the image file
            
        Returns:
            Dictionary with file path and extracted text
        """
        print(f"Processing: {file_path}")
        text = self.image_loader.process_single_image(file_path)
        
        result = {
            'file_path': file_path,
            'text': text,
            'timestamp': datetime.now().isoformat()
        }
        
        self.results.append(result)
        return result
    
    def process_directory(self, directory_path: str) -> List[Dict[str, str]]:
        """
        Process all image files in a directory.
        
        Args:
            directory_path: Path to the directory containing images
            
        Returns:
            List of results for all processed images
        """
        if not os.path.exists(directory_path):
            print(f"Error: Directory not found: {directory_path}")
            return []
        
        # Supported image extensions
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif'}
        
        # Find all image files in directory
        image_files = []
        for file_path in Path(directory_path).iterdir():
            if file_path.is_file() and file_path.suffix.lower() in image_extensions:
                image_files.append(str(file_path))
        
        if not image_files:
            print(f"No image files found in directory: {directory_path}")
            return []
        
        print(f"Found {len(image_files)} image files to process")
        
        # Process each image file
        results = []
        for image_file in image_files:
            result = self.process_single_file(image_file)
            results.append(result)
        
        return results
    
    def print_to_terminal(self, results: List[Dict[str, str]]):
        """Print results to terminal."""
        print("\n" + "="*50)
        print("CONTACT CARD EXTRACTION RESULTS")
        print("="*50)
        
        for i, result in enumerate(results, 1):
            print(f"\n--- File {i}: {os.path.basename(result['file_path'])} ---")
            print(f"Path: {result['file_path']}")
            print(f"Timestamp: {result['timestamp']}")
            print("Extracted Text:")
            print("-" * 30)
            print(result['text'])
            print("-" * 30)
    
    def save_to_text_file(self, results: List[Dict[str, str]], output_file: str):
        """Save results to a text file."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("CONTACT CARD EXTRACTION RESULTS\n")
                f.write("="*50 + "\n\n")
                
                for i, result in enumerate(results, 1):
                    f.write(f"--- File {i}: {os.path.basename(result['file_path'])} ---\n")
                    f.write(f"Path: {result['file_path']}\n")
                    f.write(f"Timestamp: {result['timestamp']}\n")
                    f.write("Extracted Text:\n")
                    f.write("-" * 30 + "\n")
                    f.write(result['text'])
                    f.write("\n" + "-" * 30 + "\n\n")
            
            print(f"Results saved to: {output_file}")
        except Exception as e:
            print(f"Error saving to text file: {e}")
    
    def save_to_csv_file(self, results: List[Dict[str, str]], output_file: str):
        """Save results to a CSV file."""
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow(['File Path', 'File Name', 'Extracted Text', 'Timestamp'])
                
                # Write data
                for result in results:
                    writer.writerow([
                        result['file_path'],
                        os.path.basename(result['file_path']),
                        result['text'],
                        result['timestamp']
                    ])
            
            print(f"Results saved to: {output_file}")
        except Exception as e:
            print(f"Error saving to CSV file: {e}")


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description='Extract text from contact card images using OCR',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python contact_card_reader.py image.jpg
  python contact_card_reader.py /path/to/images/ --output text.txt
  python contact_card_reader.py /path/to/images/ --format csv --output results.csv
        """
    )
    
    parser.add_argument(
        'input_path',
        help='Path to image file or directory containing images'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output file path (optional)'
    )
    
    parser.add_argument(
        '--format', '-f',
        choices=['text', 'csv'],
        default='text',
        help='Output format: text or csv (default: text)'
    )
    
    parser.add_argument(
        '--print', '-p',
        action='store_true',
        help='Print results to terminal (default behavior)'
    )
    
    args = parser.parse_args()
    
    # Initialize the reader
    reader = ContactCardReader()
    
    # Determine if input is file or directory
    input_path = args.input_path
    
    if os.path.isfile(input_path):
        # Process single file
        results = [reader.process_single_file(input_path)]
    elif os.path.isdir(input_path):
        # Process directory
        results = reader.process_directory(input_path)
    else:
        print(f"Error: Input path does not exist: {input_path}")
        sys.exit(1)
    
    if not results:
        print("No results to process")
        sys.exit(1)
    
    # Handle output options
    if args.output:
        # Save to file
        if args.format == 'csv':
            reader.save_to_csv_file(results, args.output)
        else:
            reader.save_to_text_file(results, args.output)
    
    if args.print or not args.output:
        # Print to terminal
        reader.print_to_terminal(results)


if __name__ == '__main__':
    main()
