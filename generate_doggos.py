#!/usr/bin/env python
from random import randint

names = ['Woofter',
         'Greatfloof',
         'Stinkbreath',
         'Fuzzcloud',
         'Rosie',
         'Pixie',
         'Dougal',
         'Walter',
         'Scout',
         'Fly']

titles = ['Sir',
          'Madam',
          'TheGreatest',
          'TheOneAndOnly',
          'YourMajesty',
          'TheRoyalBorkness',
          'DeepChonk',
          'OhLawdHeComin']

good_dog_types = ['goodboi', 'pupper']
bad_dog_types = ['baddog', 'pupper']

signature_moves = ['mlem',
                   'bork',
                   'blep',
                   'mlam',
                   'buttwiggle',
                   'tailwaggle']

with open('good_doggos.txt', 'w') as f:
    for i in range(0, 20):
        title = titles[randint(0, len(titles) - 1)]
        name = names[randint(0, len(names) -1)]
        dog_type = good_dog_types[randint(0, len(good_dog_types) -1)]
        signature_move = signature_moves[randint(0, len(signature_moves) -1)]
        f.write('%s %s %s %s\n' % (title, name, dog_type, signature_move))


with open('bad_doggos.txt', 'w') as f:
    for i in range(0, 20):
        title = titles[randint(0, len(titles) - 1)]
        name = names[randint(0, len(names) -1)]
        dog_type = bad_dog_types[randint(0, len(bad_dog_types) -1)]
        signature_move = signature_moves[randint(0, len(signature_moves) -1)]
        f.write('%s %s %s %s\n' % (title, name, dog_type, signature_move))
