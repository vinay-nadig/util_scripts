#!/usr/bin/env python

from nltk.corpus import wordnet as wn
import pynotify
import commands
import sys
from pynotify import URGENCY_CRITICAL as CRIT


def main():
    # Creating a pynotify instance
    pynotify.init("Basic")

    status, word = commands.getstatusoutput("xclip -o")
    word = word.strip()

    # If xclip has a problem
    if(not(status == 0)):
        n = pynotify.Notification("Dictionary", "Sorry! xclip encountered an error.\nError code = %s"%status)
        n.set_urgency(CRIT)
        n.show()
        sys.exit(1)

    #If there is more than one word
    word_length = len(word.strip().split(" "))
    if(word_length > 1):
        n = pynotify.Notification("Dictionary", "Sorry! Only single words are permitted.")
        n.set_urgency(CRIT)
        n.show()
        sys.exit(2)

    # Search for the word
    print word
    synsets = wn.synsets(word)

    # If no results found
    if(not synsets):
        n = pynotify.Notification("Dictionary", "Sorry! No word found\nPlease check the spelling")
        n.set_urgency(CRIT)
        n.show()
        sys.exit(3)
    else:
        for synset in synsets:
            if(synset.examples):
                no_of_examples = len(synset.examples)
                if(no_of_examples > 3):
                    no_of_examples = 3
                n = pynotify.Notification("Dictionary", "Name : " + synset.name + "\nLexical type : " + synset.lexname + "\nDefinition : " + synset.definition + "\n" + print_example(synset, no_of_examples))
                n.set_urgency(CRIT)
                n.show()
            else:
                n = pynotify.Notification("Dictionary", "Name : " + synset.name + "\nLexical type : " + synset.lexname + "\nDefinition : " + synset.definition)
                n.set_urgency(CRIT)
                n.show()

def print_example(synset, n):
    text = ""
    for i in range(0, n):
        text += "Example : " + synset.examples[i] + "\n"
    return text

if __name__ == "__main__":
    main()
