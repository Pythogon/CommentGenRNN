from textgenrnn import textgenrnn
final = [] # Defining variables
clear = open('holding.txt', 'w') # Clearing the cache
clear.close()
comments = textgenrnn() # New instance
comments.train_from_file('comments.txt', num_epochs = 5, rnn_size = 140, rnn_layers = 4, verification = True) # Training magic (thank textgenrnn for that)
for x in range(500):
        comments.generate_to_file('holding.txt') # Generates to cache
        with open('holding.txt') as file:
            final.append(file.read()) # Takes from cache (it's inneficient but it's the best I could do :3)
        print('tick', x)
towrite = '\n'.join(final) # Preparing the string.
with open('ai_gen.txt','w') as file:
    file.write(towrite) # Done!
