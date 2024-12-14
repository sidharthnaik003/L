import nltk
from nltk import CFG
from nltk.parse.chart import ChartParser, TopDownChartParser, BottomUpChartParser

# Print the version of nltk
print(nltk.__version__)

# Define the grammar
grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | "Rahil" | "Moon" | "terrace"
    Det -> "a" | "an" | "the" | "my" | "his"
    N -> "man" | "dog" | "cat" | "telescope" | "park" | "Moon" | "terrace"
    P -> "in" | "on" | "by" | "with" | "from"
""")

# Create parsers
top_down_parser = TopDownChartParser(grammar)
bottom_up_parser = BottomUpChartParser(grammar)

# Parse a sentence
sentence = "Rahil saw the Moon with the telescope from his terrace".split()

print("Top-Down Parsing:")
for tree in top_down_parser.parse(sentence):
    print(tree)
    tree.pretty_print()

print("\nBottom-Up Parsing:")
for tree in bottom_up_parser.parse(sentence):
    print(tree)
    tree.pretty_print()
