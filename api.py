import nlpcloud

def sentiment(text):

        token = "479520ccef150c2986b67ff0e9e0c32e58991a55"

        client = nlpcloud.Client("distilbert-base-uncased-emotion",token, gpu=False)
        response = client.sentiment(text)
        return response