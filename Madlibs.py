"""
This program generates passages that are generated in mad-lib format.
Author:Zorawar 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print (STORY)
print ("Mad Libs has started")
name = input("Enter a name: ")
print ("Based on the story, input 3 adjectives & 1 b..")
adj1  = input("Enter adjective 1: ")
adj2 = input("Enter adjetive 2: ")
adj3 = input("Enter adjective 3: ")
ver1 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
print ("Let make this game more fun by entering the following: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter your fav superhero: ")
country = input("Enter the country you want to travel next: ")
dessert = input("Enter the name of a desert: ")
year = input("Enter a year: ")

print (STORY % (name, adj1, adj2, animal, food, ver1, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name,year, noun2))