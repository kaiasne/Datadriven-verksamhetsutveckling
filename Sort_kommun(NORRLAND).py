import csv

# Define the target value and threshold
target_key = 'municipality_code'
threshold_value = 1999

# Open the input file and create the output file
with open('datatest_nr1.csv', 'r', newline='') as input_file, open('output.csv', 'w', newline='') as output_file:
    # Define the input and output CSV readers/writers
    input_reader = csv.DictReader(input_file)
    output_writer = csv.writer(output_file)

    # Write the header row to the output file
    output_writer.writerow(input_reader.fieldnames)

    # Loop through each row in the input file
    for row in input_reader:
        # Extract the workplace address column
        workplace_address = row['workplace_address']

        # Check if the target key is in the workplace address
        if target_key in workplace_address:
            # Extract the target value from the workplace address
            target_value = int(workplace_address.split(target_key + "': '")[1].split("', '")[0])

            # Check if the target value is greater than the threshold
            if target_value > threshold_value:
                # Write the row to the output file
                output_writer.writerow(row.values())
