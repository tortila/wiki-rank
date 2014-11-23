from Parser import Parser
from PageRanker import PageRanker

TEST = "Test"
REAL_DATA = "oligo854"

def main():
    print "Welcome to wiki-rank!"
    parser = Parser(TEST)
    page_rank = PageRanker(parser.links)

if __name__ == "__main__":
    main()