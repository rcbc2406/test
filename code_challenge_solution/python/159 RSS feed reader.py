import feedparser

# URL of the RSS feed
url = "https://example.com/rss/feed"

# Function to read the RSS feed
def read_rss_feed(url):
    # Parse the RSS feed
    feed = feedparser.parse(url)
    
    # Print the feed title
    print("Feed Title:", feed.feed.title)

    # Iterate over each entry in the feed
    for entry in feed.entries:
        # Print the entry title and link
        print("Title:", entry.title)
        print("Link:", entry.link)
        print("----------")

# Read the RSS feed
read_rss_feed(url)