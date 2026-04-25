# Invoice-processing-pipeline
This repo is end-to-end documented pipeline for invoice PDFs.It converts PDF to images,runs OCR,detects key fields,validates and cleans data,computes confidence,and outputs structured JSON via a single executable.py.This is whole of the problem statement given by choosing track of HDFC challange.
## Tech Stack
Python, PaddleOCR, OpenCV, PyMuPDF

## Features
- PDF to Image conversion
- OCR-based text extraction
- Key field detection
- Data validation & cleaning
- Confidence scoring

## Workflow
PDF → Image → OCR → Field Extraction → Validation → JSON Output

## Use Case
Automates invoice processing and reduces manual effort.

## Sample Output
(Add screenshot or JSON sample)

## How to Run
python main.py
