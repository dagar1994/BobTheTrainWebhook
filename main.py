from flask import Flask
from flask_assistant import Assistant, tell, request,ask
from flask_assistant import context_manager


app = Flask(__name__)
assist = Assistant(app)

with open("trackList" , "r") as f:
        trackData = f.read()

trackData = trackData.splitlines()

tracksList = []

for track in trackData:
        tracksList.append(track.strip().lower())



tracksLength = 32

tracksData = {
                "1" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Friendship.mp3",
                        "name" : "Friendship song",
                        "que" : "whom do you like to hang out with?",
                        "ans" : ["favourite friends" , "favourite friend"],
                        "token" : "1",
                        "optionOne" : "favourite friends",
                        "optionTwo" : "nobody",
                        "optionThree" : "teachers",
                        "optionFour" : "birds"
                        },
                "2" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Head_shoulders.mp3",
                        "name" : "Head shoulder knees and toes",
                        "que" : "what comes first in the rhyme",
                        "ans" : ["head" , "heads"],
                        "token" : "2",
                        "optionOne" : "shoulder",
                        "optionTwo" : "head",
                        "optionThree" : "knees",
                        "optionFour" : "toes"
                        },
                
                "3" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Rain_Rain_Go_Away.mp3",
                        "name" : "Rain rain go away",
                        "que" : "What does little Johnny want to do?",
                        "ans" : ["play"],
                        "token" : "3",
                        "optionOne" : "sleep",
                        "optionTwo" : "eat",
                        "optionThree" : "play",
                        "optionFour" : "homework"
                        },
                "4" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Five_Little_Ducks.mp3",
                        "name" : "Five little ducks",
                        "que" : "there were how many little ducks",
                        "ans" : ["five", "5" , 5],
                        "token" : "4",
                        "optionOne" : "one",
                        "optionTwo" : "five",
                        "optionThree" : "two",
                        "optionFour" : "zero"
                        },
                
                "5" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Humpty_Dumpty.mp3",
                        "name" : "Humpty Dumpty",
                        "que" : "where did Humpty Dumpty fall from",
                        "ans" : ["wall"],
                        "token" : "5",
                        "optionOne" : "house",
                        "optionTwo" : "stairs",
                        "optionThree" : "slide",
                        "optionFour" : "wall"
                        },
        
                "6" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Johnny_Johnny.mp3",
                        "name" : "Johny Johny",
                        "que" : "what is Jhonny hiding from his papa",
                        "ans" : ["sugar"],
                        "token" : "6",
                        "optionOne" : "sugar",
                        "optionTwo" : "cake",
                        "optionThree" : "homework",
                        "optionFour" : "milk"
                        },

                "7" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/BobNumbersSong.mp3",
                        "name" : "Numbers song",
                        "que" : "which number comes before 2",
                        "ans" : ["one", "1" , 1],
                        "token" : "7",
                        "optionOne" : "ten",
                        "optionTwo" : "five",
                        "optionThree" : "seven",
                        "optionFour" : "one"
                        },
        
                "8" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Happy_Birthday.mp3",
                        "name" : "Birthday song",
                        "que" : "who is wishing you birthday",
                        "ans" : ["bob"],
                        "token" : "8",
                        "optionOne" : "bob",
                        "optionTwo" : "gifts",
                        "optionThree" : "kids",
                        "optionFour" : "parents"
                        },
        
                "9" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/bob_pussy_cat.mp3",
                        "name" : "pussy cat",
                        "que" : "Whom did the cat visit",
                        "ans" : ["queen"],
                        "token" : "9",
                        "optionOne" : "father",
                        "optionTwo" : "old man",
                        "optionThree" : "queen",
                        "optionFour" : "farmer"
                        },
                "10" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Teddy_Bear.mp3",
                        "name" : "Teddy bear",
                        "que" : "What does Teddy Bear polish?",
                        "ans" : ["shoes","shoe"],
                        "token" : "10",
                        "optionOne" : "socks",
                        "optionTwo" : "shoes",
                        "optionThree" : "tiffin",
                        "optionFour" : "bottle"
                        },

                "11" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_I_HearThunder.mp3",
                        "name" : "I hear Thunder",
                        "que" : "What is cloudy today?",
                        "ans" : ["sky"],
                        "token" : "11",
                        "optionOne" : "river",
                        "optionTwo" : "sea",
                        "optionThree" : "sky",
                        "optionFour" : "road"
                        },
        
                "12" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Santa_Finger_Family.mp3",
                        "name" : "Santa Finger Family",
                        "que" : "X",
                        "ans" : ["X"],
                        "token" : "12",
                        "optionOne" : "X",
                        "optionTwo" : "X",
                        "optionThree" : "X",
                        "optionFour" : "X"
                        },
        

                "13" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Row_your_boat.mp3",
                        "name" : "Row Row Your boat",
                        "que" : "where are they rowing the boat",
                        "ans" : ["stream"],
                        "token" : "13",
                        "optionOne" : "ocean",
                        "optionTwo" : "cloud",
                        "optionThree" : "road",
                        "optionFour" : "stream"
                        },
        


                "14" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Opposites_Song.mp3",
                        "name" : "The opposites song",
                        "que" : "What is the opposite of hot?",
                        "ans" : ["cold"],
                        "token" : "14",
                        "optionOne" : "near",
                        "optionTwo" : "day",
                        "optionThree" : "tall",
                        "optionFour" : "cold"
                        },
        
                "15" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/number-song.mp3",
                        "name" : "Number Song 1 to 10",
                        "que" : "What Come After Number nine ",
                        "ans" : ["ten", "10", 10],
                        "token" : "15",
                        "optionOne" : "one",
                        "optionTwo" : "four",
                        "optionThree" : "two",
                        "optionFour" : "ten"
                        },
        
                "16" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/OneTwoBuckleMyShoe.mp3",
                        "name" : "One Two Buckle My Shoes",
                        "que" : "We Have Count Till how Many Number",
                        "ans" : ["twenty" , "20" , 20],
                        "token" : "16",
                        "optionOne" : "two",
                        "optionTwo" : "nine",
                        "optionThree" : "thirty",
                        "optionFour" : "twenty"
                        },
        
                "17" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/IHearThunder.mp3",
                        "name" : "I Hear Thunder",
                        "que" : "what sound  we can hear",
                        "ans" : ["thunder"],
                        "token" : "17",
                        "optionOne" : "lightning",
                        "optionTwo" : "thunder",
                        "optionThree" : "wet",
                        "optionFour" : "cold"
                        },



                "18" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/YankeeDoodle.mp3",
                        "name" : "Yankee Doodle",
                        "que" : "where did yankee doodle go",
                        "ans" : ["town"],
                        "token" : "18",
                        "optionOne" : "town",
                        "optionTwo" : "market",
                        "optionThree" : "home",
                        "optionFour" : "village"
                        },
        



                "19" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Friendship-Song.mp3",
                        "name" : "Friendship song",
                        "que" : "who is bob Favourite friends ",
                        "ans" : ["all of us", "all of you" , "us"],
                        "token" : "19",
                        "optionOne" : "parents",
                        "optionTwo" : "neighbours",
                        "optionThree" : "relative",
                        "optionFour" : "all of you"
                        },
        


                "25" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Friendship-Song.mp3",
                        "name" : "Friendship song",
                        "que" : "Friendship song is all about who",
                        "ans" : ["friend" , "firends"],
                        "token" : "25",
                        "optionOne" : "friends",
                        "optionTwo" : "parents",
                        "optionThree" : "brother",
                        "optionFour" : "sister"
                        },
        
                "21" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Five_little+duckss.mp3",
                        "name" : "Five Little Ducks ",
                        "que" : "what activities 5 ducks Were Doing ",
                        "ans" : ["swimming"],
                        "token" : "21",
                        "optionOne" : "running",
                        "optionTwo" : "swimming",
                        "optionThree" : "playing",
                        "optionFour" : "jumping"
                        },
        
                "22" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Cobbler.mp3",
                        "name" : "Bob Cobblers",
                        "que" : "Who mend  the shoes",
                        "ans" : ["Cobblers" , "Cobbler"],
                        "token" : "22",
                        "optionOne" : "carpenter",
                        "optionTwo" : "cobblers",
                        "optionThree" : "teacher",
                        "optionFour" : "mechanic"
                        },
        
        
                "23" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Tiskat.mp3",
                        "name" : "Bob Tiskat",
                        "que" : "which color Basket Was it",
                        "ans" : ["Green and Yellow", "green yellow" , "yellow and green" , "yellow green"],
                        "token" : "23",
                        "optionOne" : "green and yellow",
                        "optionTwo" : "blue",
                        "optionThree" : "white",
                        "optionFour" : "orange"
                        },

                "24" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/MaryContrary.mp3",
                        "name" : "Mary Contrary",
                        "que" : "What is Made Of Chocolate brick",
                        "ans" : ["mary home"],
                        "token" : "24",
                        "optionOne" : "garden",
                        "optionTwo" : "flower",
                        "optionThree" : "farm",
                        "optionFour" : "mary home"
                        },
        
                "20" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/PussyCat.mp3",
                        "name" : "Pussy Cat",
                        "que" : "what does pussy cat love to do",
                        "ans" : ["travel the world"],
                        "token" : "20",
                        "optionOne" : "travel the world",
                        "optionTwo" : "reading",
                        "optionThree" : "writing",
                        "optionFour" : "singing"
                        },
        
                "26" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Bob_Opposites_Song.mp3",
                        "name" : "Opposite song",
                        "que" : "what is the opposite of night",
                        "ans" : ["day"],
                        "token" : "26",
                        "optionOne" : "day",
                        "optionTwo" : "morning",
                        "optionThree" : "afternoon",
                        "optionFour" : "evening"
                        },
        
                "27" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/DaysoftheWeek.mp3",
                        "name" : "Day Of The Weeks",
                        "que" : "Which day comes after monday",
                        "ans" : ["tuesday"],
                        "token" : "27",
                        "optionOne" : "tuesday",
                        "optionTwo" : "friday",
                        "optionThree" : "sunday",
                        "optionFour" : "wednesday"
                        },
        
                "28" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/We_Go.mp3",
                        "name" : "We go",
                        "que" : "What does the bob cross through",
                        "ans" : ["dessert"],
                        "token" : "28",
                        "optionOne" : "dessert",
                        "optionTwo" : "sea",
                        "optionThree" : "road",
                        "optionFour" : "sky"
                        },
        
                "29" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Incy_Wincy_Spider.mp3",
                        "name" : "Incy Wincy Spider",
                        "que" : "Who went up the water spout",
                        "ans" : ["Incy Wincy Spider"],
                        "token" : "29",
                        "optionOne" : "Incy Wincy Spider",
                        "optionTwo" : "ant",
                        "optionThree" : "monkey",
                        "optionFour" : "elephant"
                        },
        
                "30" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Humpty_Dumpty.mp3",
                        "name" : "Humpty Dumpty",
                        "que" : "Who had a great fall",
                        "ans" : ["Humpty Dumpty"],
                        "token" : "30",
                        "optionOne" : "Humpty Dumpty",
                        "optionTwo" : "king",
                        "optionThree" : "horses",
                        "optionFour" : "spider"
                        },
        
                "31" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/Wheels_On_The_Bus.mp3",
                        "name" : "the wheels on the bus",
                        "que" : "what goes up and down in the bus",
                        "ans" : ["window"],
                        "token" : "31",
                        "optionOne" : "window",
                        "optionTwo" : "wheel",
                        "optionThree" : "horn",
                        "optionFour" : "wiper"
                        },
        

                "32" : { "url" : "https://s3.ap-south-1.amazonaws.com/bobthetrainapp/alexa-english/DaysoftheWeek.mp3",
                        "name" : "Day Of The Weeks",
                        "que" : "which day is a rest day to take a lots of sleep",
                        "ans" : ["sunday"],
                        "token" : "32",
                        "optionOne" : "sunday",
                        "optionTwo" : "tuesday",
                        "optionThree" : "monday",
                        "optionFour" : "friday"
                        },
        
                }


@assist.action('Default Welcome Intent')
def hello_world():
    google_data = request
    my_context = context_manager.get('testContext', 'param1')
    speech = """
<speak>
<audio src="https://s3.amazonaws.com/bobthetraincanatech/Hi+Kids+I_m+Bob.mp3">
    <desc>Bob the train intro sound</desc>
    Hi Kids, I am Bob
  </audio>
<break time="1000ms"/>
Say play all, to play all the songs, or , say the name of the song you want to play.
</speak>
                """
    return ask(speech)





@assist.action('playTrack')
def hello_world():
    google_data = request

    track = google_data["result"]["parameters"]["songsNames"]
    track = track.strip().lower()
    if track.strip() in tracksList:
        for index in range(1, tracksLength + 1):
                data = tracksData[str(index)]
                if data["name"].lower() == track:
                        
                        trackIndex = str(index)
                        break
                else:
                        trackIndex = "99"
                        continue
    if trackIndex == "99":
            speech = """
<speak>
Sorry, I could not find a track by that name. Say , play all to play all the songs, or , say, the name of the song you want to play.
</speak>
                """
    else:               

            my_context = context_manager.get('testContext', 'param1')
            context_manager.add("playstart")
            context_manager.set('playstart', 'currentTrack', trackIndex)
            speech = """
        <speak>
        Playing """ + tracksData[trackIndex]["name"] + """ . 
        <break time="1000ms"/>
        <audio src=" """ + tracksData[trackIndex]["url"] + """ ">
            <desc>""" + tracksData[trackIndex]["name"] + """</desc>
            Sorry, there is some problem
          </audio>
        <break time="1000ms"/>
        Would you like to play a quiz now?
        </speak>
                        """
    return ask(speech)



@assist.action('playAll')
def hello_world():
    google_data = request
    my_context = context_manager.get('testContext', 'param1')
    context_manager.add("playstart")
    context_manager.set('playstart', 'currentTrack', "1")
    speech = """
<speak>
Playing """ + tracksData["1"]["name"] + """ . 
<break time="1000ms"/>
<audio src=" """ + tracksData["1"]["url"] + """ ">
    <desc>""" + tracksData["1"]["name"] + """</desc>
    Sorry, there is some problem
  </audio>
<break time="1000ms"/>
Would you like to play a quiz now?
</speak>
                """
    return ask(speech)



@assist.action('playTrack-yes')
def hello_world():
    google_data = request
    contextsList = google_data["result"]["contexts"]
    for context in contextsList:
        if context["name"] == "playstart":
                currentTrack = context["parameters"]["currentTrack"]
                break
        else:
                currentTrack = "1"
                continue
    my_context = context_manager.get('playstart', 'currentTrack')
    context_manager.add("playstart")
    context_manager.set('playstart', 'currentTrack', currentTrack)
    if tracksData[currentTrack]["que"] == "X":
            google_data = request
            contextsList = google_data["result"]["contexts"]
            for context in contextsList:
                if context["name"] == "playstart":
                        currentTrack = context["parameters"]["currentTrack"]
                        break
                else:
                        currentTrack = "1"
                        continue 

            speech = """
        <speak>
        <break time="1000ms"/>
        There is no question for this song. Say, play all to play all the songs, or , say , the name of the song you want to play.
        </speak>
                        """
            return ask(speech)


    else:
            speech = """
        <speak>
        Ok, so here is your question,
         """ + tracksData[currentTrack]["que"] +  """ . Your options are,  """ + tracksData[currentTrack]["optionOne"] +  """ ,
        """ + tracksData[currentTrack]["optionTwo"] +  """ ,
        """ + tracksData[currentTrack]["optionThree"] +  """ , or , 
        """ + tracksData[currentTrack]["optionFour"] +  """ .
        </speak>
                        """
            return ask(speech)



@assist.action('playTrack-yes-custom')
def hello_world():
    google_data = request
    contextsList = google_data["result"]["contexts"]
    for context in contextsList:
        if context["name"] == "playstart":
                currentTrack = context["parameters"]["currentTrack"]
                break
        else:
                currentTrack = "1"
                continue
    answerByUser = google_data["result"]["parameters"]["any1"]

    answer = tracksData[currentTrack]["ans"][0]
    if answerByUser == "default answer":
        sOut = "There was some problem in fetching the answer. "
    elif answerByUser == answer:
        sOut = """
<audio src="https://s3.amazonaws.com/bobthetraincanatech/CHILDREN-cheering+VE+2.mp3"><desc></desc></audio>
<audio src="https://s3.amazonaws.com/bobthetraincanatech/Claping+5Sec.mp3"><desc></desc></audio>
Yes, """ + answer + """ is the correct answer.
"""
    else:
        sOut = """
<audio src="https://s3.amazonaws.com/bobthetraincanatech/sfx_1.wav"><desc></desc></audio>
<audio src="https://s3.amazonaws.com/bobthetraincanatech/sfx_2.wav"><desc></desc></audio>
Oops, the correct answer is, """ + answer
    my_context = context_manager.get('playstart', 'currentTrack')
    if currentTrack == "32":
        newTrack = "1"
    else:
        newTrack = str(int(currentTrack) + 1)
   
 
    context_manager.add("playstart")
    context_manager.set('playstart', 'currentTrack', newTrack)
    speech = """
<speak>
""" + sOut + """

Say, play all, to play all the songs, or , say the name of the song you want to play.
</speak>
                """
    return ask(speech)









@assist.action('playTrack-custom')
def hello_world():
    google_data = request
    contextsList = google_data["result"]["contexts"]
    for context in contextsList:
        if context["name"] == "playstart":
                currentTrack = context["parameters"]["currentTrack"]
                answerByUser = context["parameters"]["any.original"]
                break
        else:
                currentTrack = "1"
                answerByUser = "default answer"
                continue 

   
 
    context_manager.add("playstart")
    context_manager.set('playstart', 'currentTrack', currentTrack)
    speech = """
<speak>
Sorry, I could not understand that.
<break time="1000ms"/>
Now Playing """ + tracksData[currentTrack]["name"] + """ . 
<break time="1000ms"/>
<audio src=" """ + tracksData[currentTrack]["url"] + """ ">
    <desc>""" + tracksData[currentTrack]["name"] + """</desc>
    Sorry, there is some problem
  </audio>
<break time="1000ms"/>
Would you like to play a quiz now?

</speak>
                """
    return ask(speech)







@assist.action('playAll-yes')
def hello_world():
    google_data = request
    contextsList = google_data["result"]["contexts"]
    for context in contextsList:
        if context["name"] == "playstart":
                currentTrack = context["parameters"]["currentTrack"]
                break
        else:
                currentTrack = "1"
                continue
    my_context = context_manager.get('playstart', 'currentTrack')
    context_manager.add("playstart")
    context_manager.set('playstart', 'currentTrack', currentTrack)
    if tracksData[currentTrack]["que"] == "X":
            google_data = request
            contextsList = google_data["result"]["contexts"]
            for context in contextsList:
                if context["name"] == "playstart":
                        currentTrack = context["parameters"]["currentTrack"]
                        break
                else:
                        currentTrack = "1"
                        continue 

            if currentTrack == "32":
                newTrack = "1"
            else:
                newTrack = str(int(currentTrack) + 1)
           
         
            context_manager.add("playstart")
            context_manager.set('playstart', 'currentTrack', newTrack)
            speech = """
        <speak>
        There is no question for this song. Now Playing """ + tracksData[newTrack]["name"] + """ . 
        <break time="1000ms"/>
        <audio src=" """ + tracksData[newTrack]["url"] + """ ">
            <desc>""" + tracksData[newTrack]["name"] + """</desc>
            Sorry, there is some problem
          </audio>
        <break time="1000ms"/>
        Would you like to play a quiz now?

        </speak>
                        """
            return ask(speech)
    else:
            speech = """
        <speak>
        Ok, so here is your question,
         """ + tracksData[currentTrack]["que"] +  """. Your options are, """ + tracksData[currentTrack]["optionOne"] +  """ ,
        """ + tracksData[currentTrack]["optionTwo"] +  """ ,
        """ + tracksData[currentTrack]["optionThree"] +  """ , or , 
        """ + tracksData[currentTrack]["optionFour"] +  """ .
        </speak>
                        """
            return ask(speech)



@assist.action('playAll-custom')
def hello_world():
    google_data = request
    contextsList = google_data["result"]["contexts"]
    for context in contextsList:
        if context["name"] == "playstart":
                currentTrack = context["parameters"]["currentTrack"]
                answerByUser = context["parameters"]["any.original"]
                break
        else:
                currentTrack = "1"
                answerByUser = "default answer"
                continue 

   
 
    context_manager.add("playstart")
    context_manager.set('playstart', 'currentTrack', currentTrack)
    speech = """
<speak>
Sorry, I could not understand that
<break time="1000ms"/>
Now Playing """ + tracksData[currentTrack]["name"] + """ . 
<break time="1000ms"/>
<audio src=" """ + tracksData[currentTrack]["url"] + """ ">
    <desc>""" + tracksData[currentTrack]["name"] + """</desc>
    Sorry, there is some problem
  </audio>
<break time="1000ms"/>
Would you like to play a quiz now?

</speak>
                """
    return ask(speech)





@assist.action('playAll-yes-custom')
def hello_world():
    google_data = request
    contextsList = google_data["result"]["contexts"]
    for context in contextsList:
        if context["name"] == "playstart":
                currentTrack = context["parameters"]["currentTrack"]
                answerByUser = context["parameters"]["any.original"]
                break
        else:
                currentTrack = "1"
                answerByUser = "default answer"
                continue 

    answer = tracksData[currentTrack]["ans"][0]
    if answerByUser == "default answer":
        sOut = "There was some problem in fetching the answer"
 
    elif answerByUser == answer:
        sOut = """
<audio src="https://s3.amazonaws.com/bobthetraincanatech/CHILDREN-cheering+VE+2.mp3"><desc></desc></audio>
<audio src="https://s3.amazonaws.com/bobthetraincanatech/Claping+5Sec.mp3"><desc></desc></audio>
Yes, """ + answer + """ is the correct answer.
"""
    else:
        sOut = """
<audio src="https://s3.amazonaws.com/bobthetraincanatech/sfx_1.wav"><desc></desc></audio>
<audio src="https://s3.amazonaws.com/bobthetraincanatech/sfx_2.wav"><desc></desc></audio>
Oops, the correct answer is, """ + answer
    my_context = context_manager.get('playstart', 'currentTrack')
    if currentTrack == "32":
        newTrack = "1"
    else:
        newTrack = str(int(currentTrack) + 1)
   
 
    context_manager.add("playstart")
    context_manager.set('playstart', 'currentTrack', newTrack)
    speech = """
<speak>
""" + sOut + """

<break time="1000ms"/>
. Now Playing """ + tracksData[newTrack]["name"] + """ . 
<break time="1000ms"/>
<audio src=" """ + tracksData[newTrack]["url"] + """ ">
    <desc>""" + tracksData[newTrack]["name"] + """</desc>
    Sorry, there is some problem
  </audio>
<break time="1000ms"/>
Would you like to play a quiz now?

</speak>
                """
    return ask(speech)






@assist.action('playAll-no')
def hello_world():

    google_data = request
    contextsList = google_data["result"]["contexts"]
    for context in contextsList:
        if context["name"] == "playstart":
                currentTrack = context["parameters"]["currentTrack"]
                break
        else:
                currentTrack = "1"
                continue 

    if currentTrack == "32":
        newTrack = "1"
    else:
        newTrack = str(int(currentTrack) + 1)
   
 
    context_manager.add("playstart")
    context_manager.set('playstart', 'currentTrack', newTrack)
    speech = """
<speak>
Now Playing """ + tracksData[newTrack]["name"] + """ . 
<break time="1000ms"/>
<audio src=" """ + tracksData[newTrack]["url"] + """ ">
    <desc>""" + tracksData[newTrack]["name"] + """</desc>
    Sorry, there is some problem
  </audio>
<break time="1000ms"/>
Would you like to play a quiz now?

</speak>
                """
    return ask(speech)


@assist.action('playTrack-no')
def hello_world():

    google_data = request
    contextsList = google_data["result"]["contexts"]
    for context in contextsList:
        if context["name"] == "playstart":
                currentTrack = context["parameters"]["currentTrack"]
                break
        else:
                currentTrack = "1"
                continue 

    speech = """
<speak>
<break time="1000ms"/>
Say, play all to play all the songs, or , say , the name of the song you want to play.
</speak>
                """
    return ask(speech)

if __name__ == '__main__':
    app.run(debug=True)
