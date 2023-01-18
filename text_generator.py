from nltk import regexp_tokenize
import random

input_file = input()

with open(input_file, 'r') as corpus_file:
    text = corpus_file.read()

tokenized = regexp_tokenize(text, r"[^\s]+")

bigrams = []
i = 1
for token in tokenized:
    if i < len(tokenized):
        bigram = [token, tokenized[i]]
        bigrams.append(bigram)
    i += 1

markov = {}
for bigram in bigrams:
    markov.setdefault(bigram[0], {})
    markov[bigram[0]].setdefault(bigram[1], 0)
    markov[bigram[0]][bigram[1]] += 1

for head, tails in markov.items():
    markov[head] = dict(sorted(tails.items(), key=lambda x: x[1], reverse=True))

for _ in range(10):
    seed_word = random.choice(tokenized)
    while seed_word.capitalize() != seed_word or seed_word.startswith('-') or seed_word.endswith('.') or seed_word.endswith('!') or seed_word.endswith('?'):
        seed_word = random.choice(tokenized)
    sentence = [seed_word]
    while True:
        words = list(markov[sentence[-1]].keys())
        weights = list(markov[sentence[-1]].values())
        next_word = random.choices(words, weights=weights)[0]
        sentence.append(next_word)
        if len(sentence) >= 5 and (sentence[-1].endswith('.') or sentence[-1].endswith('!') or sentence[-1].endswith('?')):
            break
    print(" ".join(sentence), end="\n\n")
