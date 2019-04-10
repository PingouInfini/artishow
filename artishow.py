import sys
import os
import common.twitter_treatment

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    user = sys.argv[1]

    timeline_tweets_path = os.path.join(os.getcwd(),"samples","timeline","json")
    keywords_tweets_path = os.path.join(os.getcwd(),"samples","keywords","json")

    common.twitter_treatment.draw_wordcloud_from_tweet(user, timeline_tweets_path, keywords_tweets_path)
    common.twitter_treatment.plot_data_in_map(user, timeline_tweets_path, keywords_tweets_path)