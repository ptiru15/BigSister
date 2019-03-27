
from flask import Flask, render_template, request
import requests
import tweepy

app = Flask("MyApp")

def send_simple_message(address):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox2fae016e6e294ce38e8d427233810d6d.mailgun.org/messages",
        auth=("api", "17557645b7115460f806a045374c0315-985b58f4-a3204d0f"),
        data={"from": "Excited User <mailgun@sandbox2fae016e6e294ce38e8d427233810d6d.mailgun.org>",
              "to": [address],
              "subject": "Subscription successful",
              "text": "Testing some Mailgun awesomness!"})


@app.route("/")
def hello():
    return "Hello World"

@app.route("/form")
def formMethod():
    return render_template("Page2.html")


@app.route("/<name>")
def helloStranger(name):
    return render_template("Page3.html", name = name.title())




@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print(form_data["email"])
    send_simple_message(form_data["email"])
    return "All OK"


def myTweetMethod():
   #twitter apps
   auth=tweepy.OAuthHandler(“Zi0zR6Y3kw2ly98wE7majMb55”,“9bA2086tHojvAUQL4EzMhMPnv3Wr4Lsnc6LbjyR8KaJY7btphB”)
   auth.set_access_token(“1011888746009067520-CEER93u9rCyHTe3Vu5BOiu13g7pXiT”,“sZU3fium2Lk9xS13T50uW0psFOxb97KuvyHqwnGuTYKoN”)

   twitter_api=tweepy.API(auth)

   bigSister_tweets=twitter_api.search(
   q="BigSister"
   )
   
   return bigSister_tweets[:3]


@app.route("/tweet”")
def hellostranger4():
   myTweets = myTweetMethod()
   return render_template(Page3.html”, tweets = myTweets)

if __name__ == '__main__':
    app.run(debug=True)

