# Image Text Extractor & Visualizer (OCR)

A Python-based Optical Character Recognition (OCR) tool that utilizes **OpenCV** for advanced image preprocessing and **Tesseract OCR** to extract text from images. The application prints the extracted text to the console, saves it to a local text file, and displays the original image with bounding boxes drawn around detected words.

---

## 🚀 Features

* **Advanced Image Preprocessing:** Automatically enhances image contrast, removes noise using median blurring, and applies Otsu's thresholding for high-accuracy OCR text extraction.
* **Text Extraction:** Extracts structured text from images using PyTesseract.
* **Data Export:** Saves the recognized text directly into a `recognized_text.txt` file.
* **Visual Bounding Boxes:** Highlights recognized text in real-time by drawing green bounding boxes on the original image (filtering out low-confidence detections below 50%).

---

## 🛠️ Prerequisites & Installation

Before running the script, ensure you have Python installed and the required dependencies set up.

### 1. Install Tesseract OCR Engine
Tesseract is a binary executable required by the Python wrapper.
* **Windows:** Download and install the installer from [UB Mannheim Tesseract](https://github.com/UB-Mannheim/tesseract/wiki). 
* *Note:* The script assumes Tesseract is installed at: `C:\Program Files\Tesseract-OCR\tesseract.exe`. If yours is installed elsewhere, update the path on **Line 5** of the script.
* **macOS:** Install via Homebrew: `brew install tesseract`
* **Linux (Ubuntu/Debian):** Install via APT: `sudo apt install tesseract-ocr`

### 2. Install Python Packages
Install the required libraries using `pip`:

```bash
pip install opencv-python pytesseract numpy
