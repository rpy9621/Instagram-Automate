#instagaram automation 

# impoting the instabot module as Bot

from instabot import Bot
import time

#making a funtion to acces bot module
bot = Bot()
 
# giving the used_id and name of the id
bot.login(username = "user_id", password = "password")

#to follow anyone use this along with it's username
#bot.follow('incindia')

#to follow anyone use this along with it's username
#bot.unfollow('user_name')

'''#When the photo is directly aviliable on the project directory then you have to just give
the name of the photo otherwise if you five it path then you have to convert the forward slash
into black slash like that (C:/Users/rpy96/OneDrive/Pictures/WhatsApp Image 2022-09-25 at 12.33.18.jpeg)'''

# in caption section you write whatever you want to add into a caption

#bot.upload_photo("C:/Users/rpy96/OneDrive/Pictures/WhatsApp Image 2022-09-25 at 12.33.18.jpeg", caption="Hii ❤️❤️")

# to send message to multiple person

#bot.send_messages("Hii, Good Morning !",['_akash_tiwari_003', 'ankita7814yadav', 'namratayadav_00' ])

# to get all the follower user_id

# followers = bot.get_user_followers("ramendra192")

# for follower in followers:
#     follower_details = bot.get_user_info(follower)
#     print(follower_details)

# to get all the info about user following

following = bot.get_user_following("ramendra192")
for follow in following:
    following_info = bot.get_user_info(follow)
    print(following_info)
    time.sleep(10)
