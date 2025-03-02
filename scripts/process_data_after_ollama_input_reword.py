import json
import re
import os

file_name = "/home/angelos.toutsios.gr/data/Thesis_dev/SUMO-terms/data/LatestDataSet/20-2-2025_generated_dataset/20k_shuffled_from_each_complexity/merged_01_Mar_var_replaced_ollama_reword.json"

output_file = output_file = os.path.splitext(file_name)[0]+"_final.json"

# Load JSON file
with open(file_name, "r", encoding="utf-8") as f:
    data = json.load(f)

dataset = []

# Apply transformations to "input" and "output" fields
for entry in data:
    input_text = entry["input"]
    if (input_text.startswith('"') and input_text.endswith('"')):
      input_text = input_text[1:-1]
      result = {
          "input": input_text.strip(),
          "output": entry["output"]
      }
      dataset.append(result)

print(f"Final Dataset length: {len(dataset)}")

# Save the processed JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=4)

print("Processed data saved to processed_file.json")
