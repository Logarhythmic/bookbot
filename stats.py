def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text=text.lower()
    characters = {}
    for char in text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_character_counts(char_counts):
    listed_counts = []
    for key in char_counts:
        new_dict = {'character': key, 'count': char_counts[key]}
        listed_counts.append(new_dict)
    listed_counts.sort(key=lambda x: x['count'], reverse=True)
    return listed_counts