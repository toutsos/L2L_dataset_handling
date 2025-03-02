import json
import re
import sys
from pathlib import Path
import os

def convert_to_json(english_file):
    try:
        with open(english_file, 'r', encoding='utf-8') as eng_f:
            english_lines = eng_f.readlines()

        dataset = []
        for eng in english_lines:
            dataset.append({
                "input": eng.strip(),
            })

        output_file = os.path.splitext(english_file)[0] + ".json"


        with open(output_file, 'w', encoding='utf-8') as json_f:
            json.dump(dataset, json_f, indent=4, ensure_ascii=False)

        print(f"Dataset saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <valid_sentences.txt>")
    else:
        log_file = Path(sys.argv[1])

        if not log_file.exists():
            print("Error: Log file does not exist.")
        else:
            convert_to_json(log_file)