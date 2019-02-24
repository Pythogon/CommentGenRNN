from textgenrnn import textgenrnn
clear = open('holding.txt', 'w')
clear.close()
final = []
comments = textgenrnn()
comments.train_from_file('comments.txt', num_epochs = 5, rnn_size = 140, rnn_layers = 4, verification = True)
for x in range(500):
        comments.generate_to_file('holding.txt')
        with open('holding.txt',encoding='utf-8') as file:
            final.append(file.read())
        print('tick', x)
towrite = '\n'.join(final)
with open('ai_gen.txt','w') as file:
    file.write(towrite)
    
