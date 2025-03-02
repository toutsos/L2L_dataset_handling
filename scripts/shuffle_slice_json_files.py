import json
import random
import os

"""
Input: JSON file
Output: JSON file.

Suffles data and keep a specific number of sentences.
"""

# File paths
input_json = "/home/angelos.toutsios.gr/data/Thesis_dev/SUMO-terms/data/LatestDataSet/20-2-2025_generated_dataset/combined_35_plus_complexity.json"

number_of_data = 20000

output_file = os.path.splitext(input_json)[0]+"_shuffle_"+str(number_of_data)+".json"

# Load JSON data
with open(input_json, "r", encoding="utf-8") as f:
    data = json.load(f)

# Shuffle the list
random.shuffle(data)

# Keep only the first 20,000 items
sampled_data = data[:number_of_data]

# Save to a new JSON file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(sampled_data, f, indent=4)

print(f"Shuffled and saved {len(sampled_data)} items to {output_file}")