import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv('./prod.csv')

# Basic statistics
num_sentences = len(df)
avg_sentence_length = df['sentences'].apply(lambda x: len(x.split())).mean()

# Display basic statistics
print(f"Total number of sentences: {num_sentences}")
print(f"Average sentence length (in words): {avg_sentence_length:.2f}")

# Word frequency
word_frequency = df['sentences'].str.split(expand=True).stack().value_counts()

# Display the most common words
print("\nTop 5 most common words:")
print(word_frequency.head(5))

# Character count statistics
df['char_count'] = df['sentences'].apply(len)
max_char_count = df['char_count'].max()
min_char_count = df['char_count'].min()
avg_char_count = df['char_count'].mean()

# Display character count statistics
print(f"\nMaximum character count: {max_char_count}")
print(f"Minimum character count: {min_char_count}")
print(f"Average character count: {avg_char_count:.2f}")

# Calculate sentence lengths
df['sentence_length'] = df['sentences'].apply(lambda x: len(x.split()))

# Plot and save sentence length distribution histogram
plt.figure(figsize=(10, 6))
plt.hist(df['sentence_length'], bins=20, color='skyblue', edgecolor='black')
plt.title('Sentence Length Distribution')
plt.xlabel('Sentence Length (in words)')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('sentence_length_distribution.png')
plt.close()

# Calculate word frequency
word_frequency = Counter(" ".join(df['sentences']).split())

# Plot and save top 10 most common words bar chart
common_words = word_frequency.most_common(10)  # Top 10 most common words
plt.figure(figsize=(10, 6))
plt.bar([word[0] for word in common_words], [word[1] for word in common_words], color='orange')
plt.title('Top 10 Most Common Words')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_10_common_words.png')
plt.close()