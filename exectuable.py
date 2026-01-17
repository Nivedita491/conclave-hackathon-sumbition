import sys #to read what the user upload as pdf.
import json
import time 

def main(pdf_path):
    start_time = time.time()

    # Dummy placeholder result (we will replace everything later)
    result = {
        "doc_id": pdf_path,
        "fields": {
            "dealer_name": {"value": None, "confidence": 0.0},
            "model_name": {"value": None, "confidence": 0.0},
            "horse_power": {"value": None, "confidence": 0.0},
            "asset_cost": {"value": None, "confidence": 0.0},
            "signature": {"present": False, "bbox": None, "confidence": 0.0},
            "stamp": {"present": False, "bbox": None, "confidence": 0.0}
        },
        "confidence": 0.0,
        "processing_time_sec": round(time.time() - start_time, 2), #To calculate how long the program took to run, and store it in seconds with 2 decimal accuracy.”
        "cost_estimate_usd": 0.0
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python executable.py <input_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    main(pdf_path)
