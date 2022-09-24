sixte = {'hello': 2, 'sixte': 1, 'how': 4, 'are': 2, 'no': 43, 'r': 3, 'hey': 2}

markList = sorted(((freq, word) for (word, freq) in sixte.items()), reverse=True)
sorted_words = dict([(k, v) for (v, k) in markList])

print(sorted_words)
