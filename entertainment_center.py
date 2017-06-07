#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

# Local, intra-project imports
from media import Movie
from fresh_tomatoes import open_movies_page

# Creating multiple movie instances to mimic a movie database

harry_potter_1 = Movie(
    title='Harry Potter and the Sorcerer\'s Stone',
    storyline="Rescued from the outrageous neglect of his aunt and uncle, a "
              "young boy with a great destiny proves his worth while "
              "attending Hogwarts School of Witchcraft and Wizardry.",
    runtime=152,
    poster_image_url='https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UX182_CR0,0,182,268_AL_.jpg',
    trailer_youtube_url='https://www.youtube.com/watch?v=VyHV0BRtdxo',
)

harry_potter_2 = Movie(
    title='Harry Potter and the Chamber of Secrets',
    storyline="Harry ignores warnings not to return to Hogwarts, only to find "
              "the school plagued by a series of mysterious attacks and a "
              "strange voice haunting him.",
    runtime=161,
    poster_image_url='https://images-na.ssl-images-amazon.com/images/M/MV5BMTcxODgwMDkxNV5BMl5BanBnXkFtZTYwMDk2MDg3._V1_UX182_CR0,0,182,268_AL_.jpg',
    trailer_youtube_url='https://www.youtube.com/watch?v=dmPrfYkpwTY',
)

harry_potter_3 = Movie(
    title='Harry Potter and the Prisoner of Azkaban',
    storyline="It's Harry's third year at Hogwarts; not only does he have "
              "a new \"Defense Against the Dark Arts\" teacher, but there "
              "is also trouble brewing. Convicted murderer Sirius Black "
              "has escaped the Wizards' Prison and is coming after Harry.",
    runtime=142,
    poster_image_url='https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UX182_CR0,0,182,268_AL_.jpg',
    trailer_youtube_url='https://www.youtube.com/watch?v=lAxgztbYDbs',
)

harry_potter_4 = Movie(
    title='Harry Potter and the Goblet of Fire',
    storyline="Harry finds himself mysteriously selected as an under-aged "
              "competitor in a dangerous tournament between three schools "
              "of magic.",
    runtime=157,
    poster_image_url='https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1NDMyMjExOF5BMl5BanBnXkFtZTcwOTc4MjQzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
    trailer_youtube_url='https://www.youtube.com/watch?v=PFWAOnvMd1Q',
)

# Accumulating all the movies into a list, for easy access
movies = [harry_potter_1, harry_potter_2, harry_potter_3, harry_potter_4]


# If file is run instead of importing, open the movies page
if __name__ == '__main__':
    open_movies_page(movies)
