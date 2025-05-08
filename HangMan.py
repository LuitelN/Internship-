import random
import datetime 
import csv 
import pandas as pd
df = pd.read_csv("Words.csv")
print("Welcome to Hangman")
name = input("Enter your name to continue: ")
print("Welcome " + name + ", Let's begin")
