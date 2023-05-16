import pandas as pd
import random

def split_into_quarters(dataset, date_column):
    # Convert the date column to datetime type if needed
    if not pd.api.types.is_datetime64_any_dtype(dataset[date_column]):
        dataset[date_column] = pd.to_datetime(dataset[date_column])
    
    # Set the date column as the index
    dataset.set_index(date_column, inplace=True)
    
    # Extract year and quarter from the date column
    dataset['Year'] = dataset.index.year
    dataset['Quarter'] = dataset.index.quarter
    
    # Initialize an empty dictionary to store the quarters
    quarters_data = {}
    
    # Iterate over the quarters and store the data for each quarter
    for year in dataset['Year'].unique():
        for quarter in dataset.loc[dataset['Year'] == year, 'Quarter'].unique():
            # Filter the data for the current quarter
            data = dataset.loc[(dataset['Year'] == year) & (dataset['Quarter'] == quarter)]
            # Store the data for the quarter in the dictionary
            quarters_data[(year, quarter)] = data
    
    return quarters_data

def count_vacancies_by_workplace_quarterly(dataset, date_column, workplace_column, vacancy_column):
    # Split the dataset into quarters
    quarters_data = split_into_quarters(dataset, date_column)
    
    # Initialize an empty dictionary to store the vacancy counts for each quarter
    vacancy_counts_quarterly = {}
    
    # Iterate over each quarter and count the vacancies for each workplace
    for quarter, data in quarters_data.items():
        vacancy_counts = data.groupby(workplace_column)[vacancy_column].sum()
        vacancy_counts_quarterly[quarter] = vacancy_counts
    
    return vacancy_counts_quarterly

# Example usage
file_path = 'cleaned21.csv'  # Replace with the path to your dataset file
date_column = 'publication_date'  # Specify the column name for the date
workplace_column = 'workplace_address'  # Specify the column name for the workplace
vacancy_column = 'number_of_vacancies'  # Specify the column name for the vacancy count
headline_column = 'headline'  # Specify the column name for the headline
output_file_path = 'output.csv'  # Replace with the desired output file path

# Read the dataset into a DataFrame
dataset = pd.read_csv(file_path)

# Count the number of vacancies by workplace for each quarter
vacancy_counts_quarterly = count_vacancies_by_workplace_quarterly(dataset, date_column, workplace_column, vacancy_column)

# # Create an empty DataFrame to store the results
# output_df = pd.DataFrame(columns=['Year', 'Quarter', 'Workplace', 'VacancyCount', 'Headline'])

# # Iterate over the vacancy counts for each quarter and workplace
# for quarter, vacancy_counts in vacancy_counts_quarterly.items():
#     year, qtr = quarter
#     # Iterate over the workplace names and counts
#     for workplace, count in vacancy_counts.items():
#         # Select 5 random rows from the headline column
#         headlines = dataset.loc[dataset[workplace_column] == workplace, headline_column].sample(n=5, random_state=1)
#         # If there are fewer than 5 rows, select all available rows
#         if len(headlines) < 5:
#             headlines = dataset.loc[dataset[workplace_column] == workplace, headline_column]
#         # Append a row to the output DataFrame
#         output_df = output_df.append({'Year': year, 'Quarter': qtr, 'Workplace': workplace, 'VacancyCount': count, 'Head': headlines}, ignore_index=True)


# # Write the output
# output_df.to_csv(output_file_path, index=False)

# # Create an empty DataFrame to store the results
# output_df = pd.DataFrame(columns=['Year', 'Quarter', 'Workplace', 'VacancyCount', 'Headline'])

# # Iterate over the vacancy counts for each quarter and workplace
# for quarter, vacancy_counts in vacancy_counts_quarterly.items():
#     year, qtr = quarter
#     # Iterate over the workplace names and counts
#     for workplace, count in vacancy_counts.items():
#         # Get the matching rows from dataset
#         matching_rows = dataset.loc[dataset[workplace_column] == workplace, headline_column]

#         # If there are 5 or more matching rows, sample 5 rows without replacement
#         if len(matching_rows) >= 5:
#             headlines = matching_rows.sample(n=5, replace=False, random_state=1)
#         # If there are fewer than 5 matching rows, sample all available rows without replacement
#         else:
#             headlines = matching_rows.sample(n=len(matching_rows), replace=False, random_state=1)
#         # Append a row to the output DataFrame
#         output_df = output_df.append({'Year': year, 'Quarter': qtr, 'Workplace': workplace, 'VacancyCount': count, 'Headline': headlines}, ignore_index=True)


# # Write the output
# output_df.to_csv(output_file_path, index=False),

# Create an empty DataFrame to store the results
output_df = pd.DataFrame(columns=['Year', 'Quarter', 'Workplace', 'VacancyCount', 'Headline'])

# Iterate over the vacancy counts for each quarter and workplace
for quarter, vacancy_counts in vacancy_counts_quarterly.items():
    year, qtr = quarter
    # Iterate over the workplace names and counts
    for workplace, count in vacancy_counts.items():
        # Select 5 random rows from the headline column
        headlines = dataset.loc[(dataset[workplace_column] == workplace) & (dataset['Year'] == year) & (dataset['Quarter'] == qtr), headline_column].sample(n=1, random_state=1)
        # If there are fewer than 5 rows, select all available rows
        if len(headlines) < 5:
            headlines = dataset.loc[(dataset[workplace_column] == workplace) & (dataset['Year'] == year) & (dataset['Quarter'] == qtr), headline_column]
        # Append a row to the output DataFrame
        output_df = output_df.append({'Year': year, 'Quarter': qtr, 'Workplace': workplace, 'VacancyCount': count, 'Headline': headlines.tolist()}, ignore_index=True)

# Write the output
output_df.to_csv(output_file_path, index=False)

