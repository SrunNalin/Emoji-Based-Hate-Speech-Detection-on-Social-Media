# -*- coding: utf-8 -*-

# The api will be always updated, so this script is suitable for the V3.15 tikhub.api
import emoji
import asyncio
import pandas as pd
from tikhub.api import *
import nest_asyncio

# Read a file with a list of TikTok video URLs, one URL per line
input_file = r'C:\Users\lvshu\Downloads\input_urls.txt' 
with open(input_file, 'r') as f:
    urls = f.readlines()

nest_asyncio.apply() # Avoid error about "asyncio" in the next step

async def async_test() -> None:
    # Async test
    print("Test start...\n")

    # Get TikHub request header
    r = await api.user_login()
    # Print("Running test : API.user_login()")

    # Get all comment data of TikTok video
    print("Running test : API.get_tiktok_video_comments()")
    global all_comments
    all_comments = []
    for url in urls:
        url = url.strip() # Remove newline characters from the end of the URL
        one_comments_info = await api.get_tiktok_video_comments(url, cursor=None, count=None, get_all=True)
        comments = [(url, element['text']) for element in one_comments_info]
        all_comments += comments
    print(all_comments)
    # After testing, it is found that this updated API can only retrieve all the direct comments and the author's reply of the comments
    # The replies of the comments created by other users cannot be retrieved
    # Therefore, I only retrieve the main (direct) comments under the videos
    
    # Filter the comments to only include those with at least one emoji
    def contains_emoji(string):
      for character in string:
        if character in emoji.EMOJI_DATA:
          return True
      return False
    emoji_comments = [(url, comment) for (url, comment) in all_comments if contains_emoji(comment)]

    print(emoji_comments)

    # Save a csv file
    output_file = r'C:\Users\lvshu\Downloads\url_comments.csv'
    comments_df = pd.DataFrame(emoji_comments, columns=['source_url', 'comment_text'])
    comments_df.to_csv(output_file, index=False, encoding='UTF-8')
    print("Comments saved to", output_file)


from tikhub.api import API
# You can create your own account to use this API https://api.tikhub.io/
if __name__ == '__main__':
    api = API(email='shuweilyu97@gmail.com',
        password='311224lsw',
        proxy=None,
    )
    asyncio.run(async_test())