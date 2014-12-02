import numpy as np
from Parser import Parser
from PageRanker import PageRanker

TEST = "Test"
REAL_DATA = "oligo854"
EXAMPLE = "Example"

def main():
    print "Welcome to wiki-rank!"
    parser = Parser(EXAMPLE)
    page_rank = PageRanker(parser.links)
    index = np.unravel_index(page_rank.x_ranks.argmax(), page_rank.x_ranks.shape)
    title = parser.titles[index[0]]
    print "---\nMost popular article has index", index[0] + 1, "and title:", title

if __name__ == "__main__":
    main()