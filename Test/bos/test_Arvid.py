# import streamlit as st

# st.title("My Streamlit Test App")

# st.write("Welcome to my test page!")

# x = st.slider('Select a value:', 0, 100, 50)
# st.write('You selected:', x)

# if st.button('Double the value'):
#     x *= 2
#     st.write('New value:', x)

# import csv

# filename = "Test_sys - Test_sys.csv"    # replace with your CSV file name
# search_string = "göteborg"      # replace with the string you want to search for
# column_index = 8            # replace with the index of the column you want to search in

# count = 0
# with open(filename, 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if len(row) > column_index and row[column_index] == search_string:
#             count += 1

# with open(filename, 'r') as file:
#     csv_reader = csv.reader(file)
#     headers = next(csv_reader)
#     for i, header in enumerate(headers):
#         print(f"Column {i}: {header}")

# print(f"The string '{search_string}' appears {count} times in column {column_index} of the CSV file.")



# import csv

# filename = 'Test_sys - Test_sys.csv'
# column_index = 8
# search_string = 'kalix'

# count = 0
# try:
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         header = next(reader) # Get the header row
#         for row in reader:
#             if len(row) > column_index and row[column_index] == search_string:
#                 count += 1
# except FileNotFoundError:
#     print(f"Error: file '{filename}' not found")
# except Exception as e:
#     print(f"Error: {str(e)}")

# print(f"Found {count} occurrences of '{search_string}' in column {column_index}")



# import csv

# filename = 'Test_sys - Test_sys.csv'
# column_index = 7
# search_string = input("Enter value to search for: ")

# total = 0
# try:
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         header = next(reader) # Get the header row
#         for row in reader:
#             if len(row) > column_index and row[column_index] == search_string:
#                 total += int(row[2]) # Calculate the value in column 2 and add it to the total
# except FileNotFoundError:
#     print(f"Error: file '{filename}' not found")
# except Exception as e:
#     print(f"Error: {str(e)}")

# print(f"The total for rows where column {column_index} equals '{search_string}' is: {total}")



import csv

filename = 'Test_sys - Test_sys.csv'
place_column_indices = [7] # The columns containing place names
number_column_index = 2 # The column containing the number to calculate
place_name = 'Göteborg'

total = 0
try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader) # Get the header row
        for row in reader:
            for col_index in place_column_indices:
                if len(row) > col_index and row[col_index] == place_name:
                    total += int(row[number_column_index]) # Add the number in the specified column to the total
                    break # Once we've found a match, we don't need to search any more columns in this row
except FileNotFoundError:
    print(f"Error: file '{filename}' not found")
except Exception as e:
    print(f"Error: {str(e)}")

print(f"The total for {place_name} is: {total}")

