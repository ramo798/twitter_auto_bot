import tweepy
import os
import random

CK = os.environ['CK']
CS = os.environ['CS']
AT = os.environ['AT']
AS = os.environ['AS']

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth,wait_on_rate_limit = True)

#実行時の呟き
random_no = random.randint(1,200)
api.update_status("フォロー絶対返します"+ str(random_no) +" #相互フォロー")

#検索して上からフォロー
search_results = tweepy.Cursor(api.search, q='#相互フォロー').items(20)
for result in search_results:
    user_id = result.user.id
    print (user_id)

    try:
        api.create_friendship(user_id)
    except:
        pass


# #自分のIDを取得
# myid = api.me().id
#
# #相互確認で、フォロー返ってなかったらアンフォロー
# followers = api.followers_ids(myid)
# friends = api.friends_ids(myid)
# for f in friends:
#     if f not in followers:
#         api.destroy_friendship(f)