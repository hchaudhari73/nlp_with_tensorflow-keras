import re
from string import punctuation

def clean_data(tweet):
    """cleaning text(remove hashtags, mentions, links, bitlinks, shortlinks, punctuations)

    Args:
        tweet (string): string containing #,@,www.,...

    Returns:
        text: clean text
    """
    tweet = tweet.lower()
    
    hashtag_pat = r"#[a-z0-9_\-]+"
    tweet = re.sub(pattern=hashtag_pat, repl="", string=tweet, flags=re.I)
    
    mention_pat = r"@[a-z0-9_\-]+"
    tweet = re.sub(pattern=mention_pat, repl="", string=tweet, flags=re.I)
    
    link_pat = r"http://[a-z0-9\-_\.]+ | https://[a-z0-9_\-\.]+ | www.[a-z0-9]+"
    tweet = re.sub(pattern=link_pat, repl="", string=tweet, flags=re.I)
    
    short_link_pat = r"bit.ly[a-z0-9\.]+"
    tweet = re.sub(pattern=short_link_pat, repl="", string=tweet, flags=re.I)
    
    number_pat = r="\d+"
    tweet = re.sub(pattern=number_pat, repl="", string=tweet, flags=re.I)

    garbage_pattern = "[^a-z0-9]+"
    tweet = re.sub(garbage_pattern, " ", tweet, re.I)
    
    tweet = " ".join(word.strip(punctuation) for word in tweet.split())
    return tweet


def HashMen(df, col):
    """Extracting hashtags and mentions

    Args:
        df (dataframe): dataframe from of tweets
        col (string): column name from which hashtags and mentions are to be extracted
    """ 
    mention_pattern = "@[a-z0-9]+"
    df["tweet_hash"] = df[col].map(lambda row: re.sub(mention_pattern, " ", row, re.I))
    
    df["tweet_hash"] = df["tweet_hash"].map(lambda row: " ".join([word.strip("#") for word in row.split()]))

    garbage_pattern = "[^a-z0-9]+"
    df["tweet_hash"] = df["tweet_hash"].map(lambda row: re.sub(garbage_pattern, " ", row, re.I))

    return df