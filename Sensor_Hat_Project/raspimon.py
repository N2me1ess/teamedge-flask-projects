from sense_hat import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep
from app.py import text

#this is how you load the sense object so you can use it in this script.
sense = SenseHat()

#this is how you scroll a message
sense.show_message(text)