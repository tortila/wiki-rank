from Parser import Parser
from PageRanker import PageRanker
import numpy as np

TEST = "Test"
REAL_DATA = "oligo854"

def main():
    print "Welcome to wiki-rank!"
    parser = Parser(TEST)
    page_rank = PageRanker(parser.links)
    index = np.unravel_index(page_rank.x_ranks.argmax(), page_rank.x_ranks.shape)
    title = parser.titles[index[0]]
    print "Most popular movie has index ", index[0], "and title: ", title

if __name__ == "__main__":
    main()