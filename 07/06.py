text = 'should, I subscribe? Yes. should, I subscribe? Yes!'
sentences = text.split('.')

new_sentences = []
for sentence in sentences:
    sentence = sentence.strip()
    if sentence:
        sentence = sentence[0].upper() + sentence[1:]
        if not sentence.endswith('.'):
            sentence += '.'
        new_sentences.append(sentence)

print(' '.join(new_sentences))


