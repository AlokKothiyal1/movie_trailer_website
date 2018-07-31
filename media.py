##########################################
# Project : Movie Website
# Date Started: 07/28/2016
# Date Completed: 07/30/2016
# Submitted by: Alok Kothiyal
##########################################

# Media_File
# Description: This file creates the class Movie to allow for instances of this
# class to be used in the entertainment.py file.

##########################################
import webbrowser


class Movie():
    """ Takes in 4 Arguments-
                -Movie Title
                -StoryLine
                -Poster Image Url
                -Youtube Trailer Url
        From the Instances of the Class Movie() & Initializes -
        Instance variables and Instance Methods """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # noqa
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Opens Up WebBrowser To play youtube Trailer
        webbrowser.open(self.trailer_youtube_url)
