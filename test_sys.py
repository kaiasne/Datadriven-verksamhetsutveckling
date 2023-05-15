import csv

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

def find_similar_sentences(target_sentence, csv_file):
    # Open the CSV file and extract the sentences
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        sentences = [row['description'] for row in reader]

    # Search for the target sentence and similar sentences
    similar_sentences = []
    threshold_distance = 5  # Maximum edit distance for a sentence to be considered similar
    target_count = 0

    for sentence in sentences:
        if target_sentence in sentence:
            target_count += 1
        elif edit_distance(target_sentence.lower(), sentence.lower()) <= threshold_distance:
            similar_sentences.append(sentence)

    # Print the results
    print(f"The sentence '{target_sentence}' appears {target_count} times in the dataset.")
    print(f"There are {len(similar_sentences)} similar sentences:")
    for similar_sentence in similar_sentences:
        print(similar_sentence)



find_similar_sentences("sysselsättning", "datatest_nr1")