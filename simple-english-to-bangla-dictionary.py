import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_bengali_meaning(word):
    url = f"https://www.english-bangla.com/dictionary/{word}"
    response = requests.get(url)

    if response.status_code == 404:
        return f"Sorry, '{word}' not found in the dictionary."
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        span_tags = soup.find_all('span', class_='format1')
        meanings = [span.text.strip() for span in span_tags]
        return f"Bengali meanings of '{word}': {', '.join(meanings)}"

# Prompt the user to enter the words (multiple lines)
print("Enter the words (multiple lines). Enter 'q' to finish:")
lines = []
while True:
    line = input()
    if line == 'q':
        break
    lines.append(line.strip())

# Combine lines into a single line of words
user_input = ' '.join(lines)

words = user_input.split()

bengali_meanings = []

# Add progress bar
with tqdm(total=len(words), desc="Processing") as pbar:
    for word in words:
        bengali_meanings.append(get_bengali_meaning(word))
        pbar.update(1)

# Print the Bengali meanings
for meaning in bengali_meanings:
    print(meaning)
