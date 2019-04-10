import time
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from stop_words import get_stop_words

def drawn_wordcloud_from_data(data, language, user, output_directory= "WordCloud"):
    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white",
                          height=800,
                          width=1600,
                          max_words=100,
                          stopwords=get_stop_words(language)) \
        .generate(data)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    plt.savefig(output_directory + "/" + user + "_" + str(time.time()) + ".png")
    # plt.show()