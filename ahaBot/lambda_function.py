import random
import boto3
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Region指定しないと、デフォルトのUSリージョンが使われる
clientLambda = boto3.client('lambda', region_name='ap-northeast-1')

#定数確率の定義　0.5
RESPONSE = 0.5

def lambda_handler(event, context):
    
    msg_language = event["analysedMessage"]["language"]
    sentiment_score = event["analysedMessage"]["documentSentiment"]["score"]
    
    logger.info(msg_language)
    logger.info(sentiment_score)
    
    #分岐判断　ニュートラル、
    if  -1.0 <= sentiment_score <= -0.33:
        msg_sentiment = "negative"
    elif -0.33 < sentiment_score < 0.33:
        msg_sentiment = "neutral"
    else: 
        msg_sentiment = "positive"
   
    #辞書の読み込み
    aha_dic = load_dic("aha_dic.json")
    aha_stamp = load_dic("aha_stamp.json")
    
    logger.info(aha_stamp)
    
    #検索
    response = []
    for word,word_attribute in aha_dic.items():
        if word_attribute["sentiment"] == msg_sentiment:
            if word_attribute["language"] == msg_language: 
                response.append(word)
            
    logger.info(response)
#   return { "message" : random.choice(response) }
    ret =  { "message" : random.choice(response), "stamp" : random.choice(aha_stamp[msg_sentiment])}
    return ret

def load_dic(file_name):  
  #リアクションサービスのリストは別途Jsonにて管理
    with open(file_name, "r") as file:
        aha_dic = json.load(file)
        return aha_dic
