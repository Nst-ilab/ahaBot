import random

def lambda_handler(event, context):
    
    # TODO implement
    language = event["analysedMessage"]["language"]
    sentiment_score = event["analysedMessage"]["documentSentiment"]["score"]
    
    #分岐判断　ニュートラル、
    if  -1.0 <= sentiment_score <= -0.33:
        msg_sentiment = "negative"
    elif -0.33 < sentiment_score < 0.33:
        msg_sentiment = "neutral"
    else: 
        msg_sentiment = "positve"

    #辞書定義。あとでconstに移す
    aha_dic = {
        "あぁ...":{"sentiment":"negative","language":"ja"},
        "たいへんだね":{"sentiment":"negative","language":"ja"},
        "へぇ":{"sentiment":"neutral","language":"ja"},
        "たしかに!":{"sentiment":"positve","language":"ja"}
    }
    
    response = []
    #検索
    for word,word_attribute in aha_dic.items():
        if word_attribute["sentiment"] == msg_sentiment:
            response.append(word)
    
    return random.choice(response)

    #if sentiment_score in range(-1.0,-0.33):
    #    sentiment = "negative"
    #elif sentiment_score in range(-0.33,0.33):
    #    sentiment = "neutral"
    #else: 
    #    sentiment = "positve"
 #   aha_list = []
 #   aha_list = ['']
 #   return sentiment