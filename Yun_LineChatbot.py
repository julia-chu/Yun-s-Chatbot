#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, abort
from linebot.models import *
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('oNdosWDjzvLWH9Qyz2iVpw8usoNVdZtUG9skJPPBwe/wGGvjxA203rfG9sWPZjN+WyT4Saynv0QpFJEzLJyvKA1wlmmWc6xLkUFy3bXwqHYtmVe4YdO88RsTo2rKDNT1tzi0Dvf9O8OtBttUU9Lx/AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6bd35b50f2e091646b4db5ec9e032c0a')



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "🌝 About Chu-Yun":
        buttons_template = TemplateSendMessage(
            alt_text='About Chu-Yun template',
            
            template=ButtonsTemplate(
                title='About Chu-Yun',
                text='關於我想知道些什麼？',
                thumbnail_image_url='https://upload.cc/i1/2021/05/26/c05vwJ.jpeg',
                actions=[
                    MessageTemplateAction(
                        label='我的興趣',
                        text='我的興趣'
                    ),
                    MessageTemplateAction(
                        label='我的專長',
                        text='我的專長'
                    ),
                    MessageTemplateAction(
                        label='自我增進之處',
                        text='自我增進之處'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "我的興趣":
        text ='📍我的興趣：\n 1. 拉奏小提琴 \N{Violin} \n 2.參加流浪貓狗協會(喜歡貓咪和狗！) 🦮🐈 \n 3.看美國影集 \N{clapper board}'
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text))
        return 0
    if event.message.text == "我的專長":
        text ='📍我的專長：\n 1. 運用Python或SAS進行數據資料分析💻 \n\n 2. 使用Tableau進行圖形報表 \N{bar chart} \n\n 3.繪畫繪圖 🖍'
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text))
        return 0
    if event.message.text == "自我增進之處":
        text ='📍自我增進之處：\n 1. 想要自我學習做APP、學會C語言🔎 \n\n 2. 提升英文能力並且學習第二語言 🗣 \n\n 3.閒暇之餘閱讀書籍以增進自我 🌎'
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text))
        return 0
    
    
        
    if event.message.text == '防疫期間來聽我喜歡的音樂！':
        buttons_template = TemplateSendMessage(
            alt_text='防疫期間來聽我喜歡的音樂！template',
            
            template=ButtonsTemplate(
                title='🎵🎶 近期最喜歡的音樂歌單！',
                text='防疫在家最適合聽音樂了',
                thumbnail_image_url='https://upload.cc/i1/2021/05/26/c05vwJ.jpeg',
                actions=[
                    URIAction(
                        label='古典音樂',
                        text='古典音樂',
                         uri='https://www.youtube.com/watch?v=6TwmRfeQD6M'
                    ),
                    URIAction(
                        label='西洋音樂',
                        text='西洋音樂',
                        uri='https://www.youtube.com/watch?v=8RvAKRoIDqU'
                    ),
                    URIAction(
                        label='華語音樂',
                        text='華語音樂',
                        uri='https://www.youtube.com/watch?v=mXf3Klcn-sM'
                    ),
                     URIAction(
                        label='台語音樂',
                        text='台語音樂',
                        uri='https://www.youtube.com/watch?v=0rp3pP2Xwhs'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text == '心理測驗開始！':
        buttons_template = TemplateSendMessage(
            alt_text='心理測驗開始！template',
            
            template=ButtonsTemplate(
                title='🌟 如果你跟戀人到水族館約會，會想先看什麼「哪個動物」？',
                text='來測驗你對愛情的渴望！💕💕 \n',
                thumbnail_image_url='https://upload.cc/i1/2021/05/26/c05vwJ.jpeg',
                actions=[
                    MessageTemplateAction(
                        label='A.水母',
                        text='A.水母'
                    ),
                    MessageTemplateAction(
                        label='B.海豚表演',
                        text='B.海豚表演'
                    ),
                    MessageTemplateAction(
                        label='C.企鵝',
                        text='C.企鵝'
                    ),
                     MessageTemplateAction(
                        label='D.熱帶魚',
                        text='D.熱帶魚'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text == "A.水母":
        text ='你對激情和性事比起大多數人更為好奇和感興趣，對於和另一半能一起享受性生活有著強烈希望。\n 但是這類型的人平時比較害羞😇，也不擅長耍浪漫，不太敢表現出如此大膽的一面。'
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text))
        return 0
    if event.message.text == "B.海豚表演":
        text ='代表你在愛情中會把另一半看成能互相協力攜手的「夥伴關係」👩‍❤️‍👨。\n在你的理想情況下，希望兩人之間的關係應該是平等公正，彼此相互支持、互補對方的不足，共同增進彼此的生活。\n因此你在選擇戀愛對象時，對方是否可靠是最重要的。'
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text))
        return 0
    if event.message.text == "C.企鵝":
        text ='如果你在水族館中比起魚類更想看企鵝🐧，代表你喜歡尋找與自己非常不同的另一半，你常會被與你相差很多、感覺是不同世界的人所吸引，例如年紀相差大的或是異國戀。\n兩個差異很大的人慢慢走近彼此、成為伴侶的過程，會讓你感受到戀愛的美好，更能以寬容的心去接納包容另一個人。'
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text))
        return 0
    if event.message.text == "D.熱帶魚":
        text ='你理想中的戀愛，彼此要是全心全意的，像是跟兒時一起長大的青梅竹馬結婚，或是能跟初戀走到最後的專一愛情🐠。\n對你來說，愛情中最重要的是能找到在心靈上彼此吸引、契合的靈魂伴侶。'
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text))
        return 0


if __name__ == "__main__":
    app.run()


# In[ ]:




