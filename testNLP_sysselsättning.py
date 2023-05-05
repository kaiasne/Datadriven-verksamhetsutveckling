import csv
from nltk.metrics.distance import edit_distance

# Define the target sentence and the distance threshold
target_sentence = "Annan sysselsättning"
threshold_distance = 5

# Open the input CSV file and create the output CSV file
with open('datatest_nr1.csv', newline='', encoding='utf-8') as input_file, open('output_kommun.csv', mode='w', newline='', encoding='utf-8') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write the header row to the output CSV file
    header = next(reader)
    writer.writerow(header)

    # Iterate over each row in the input CSV file
    for row in reader:
        sentence = row[0]  # Assuming the text is in the first column

        # Check if the target sentence is found or within threshold distance
        if target_sentence.lower() in sentence.lower() or edit_distance(target_sentence.lower(), sentence.lower()) <= threshold_distance:
            # Write the matching row to the output CSV file
            writer.writerow(row)

print("Sorting completed.")
