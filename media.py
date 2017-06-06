#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import webbrowser


class Movie:
    """Class for storing movie details.
    Can also play the trailer video via show_trailer method.

    Arguments:
        title               -- Title of the movie
        storyline           -- Brief storyline of the movie
        runtime             -- Movie duration (in minutes)
        poster_image_url    -- URL for the poster image
        trailer_youtube_url -- URL for the youtube trailer
    """

    def __init__(self, title, storyline, runtime,
                 poster_image_url, trailer_youtube_url):
        """Initializes the class and sets attributes from given arguments"""
        self.title = title
        self.storyline = storyline
        self.runtime = runtime
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_details(self):
        """Displays all the movie's details"""
        for attr in ('title', 'storyline', 'runtime',
                     'poster_image_url', 'trailer_youtube_url'):
            attribute = attr.replace('_', ' ').replace('url', 'URL')
            value = getattr(self, attr)
            if attr == 'runtime':
                value = '%s minutes'%value
            print('Movie {0} - {1}'.format(attribute, value))

    def show_trailer(self):
        """Opens the movie's trailer video via the webbrowser"""
        webbrowser.open(self.trailer_youtube_url, new=2)
