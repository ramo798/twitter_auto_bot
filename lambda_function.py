import tweepy
import os
import random

CK = os.environ['CK']
CS = os.environ['CS']
AT = os.environ['AT']
AS = os.environ['AS']

COUNT = os.environ['COUNT']
ENIGMA_NO = os.environ['ENIGMA_NO']

def lambda_handler(event, context):
    print("Im enigma " + str(ENIGMA_NO) + " .")
    print("Im doing " + str(COUNT) + " tasks.")
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    err_count = 0
    task_no = 1

    #実行時の呟き
    random_no = random.randint(1,200)
    api.update_status("フォロー絶対返します" + str(random_no) + " #相互フォロー")

    #検索して上からフォロー
    search_results = tweepy.Cursor(api.search, q='#相互フォロー').items(int(COUNT))
    for result in search_results:
        user_id = result.user.id
        print("task no is " + str(task_no))
        try:
            api.create_friendship(user_id)
            print("I follow " + str(user_id))
        except:
            print("I lost " + user_id)
            err_count += 1

        task_no += 1

    if err_count > 10:
        print("enigma " + str(ENIGMA_NO) + " may be dead.")
