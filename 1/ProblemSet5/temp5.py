# import feedparser
# import string
# import time
# import threading
# from project_util import translate_html
# from mtTkinter import *
# from datetime import datetime
# import pytz



# class NewsStory(object):
    # def __init__(self,guid, title,description,link,pudate):
    #     self.guid=str(guid)
    #     self.title=str(title)
    #     self.description=str(descritpion)
    #     self.link=str(link)
    #     self.pubdate=datetime.datetime(pubdate)
        
    # def get_guid(self):
    #     return self.guid
    # def get_title(self):
    #    return self.title
    # def get_description(self):
    #     return self.description
    # def get_link(self):
    #     return self.link
    # def get_pubdate(self):
    #     return self.pubdate

# c=NewsStory(4, 'red sox', 'failed everything', 'no link', 25)
# print(c.get_title())

class Story(object):
    def __init__(self,id,link,text):
        self.id=int(id)
        self.link=str(link)
        self.text=str(text)
    def get_text(self):
        return self.text

#FIRE
text=['The purple cow is soft and cuddly.','purple@#$%cow','The farmer owns a really PURPLE cow.','Purple!!! Cow!!!','purple@#$%cow','Did you see a purple cow?']
# NOT Fire
# text=['Purple cows are cool!','The purple blob over there is a cow.','How now brown cow.','Cow!!! Purple!!!','purplecowpurplecowpurplecow']
c=Story(25, 'http', text)
print(c.get_text())

class trigger(object):
    def __init__(self,story,trigger):
        self.story=str(story)
        self.trigger=str(trigger)
    
    def get_story_trigger(self):
        return self.story    
    
    def rise_flag(self):
        
        if self.trigger in self.story:
            return self.story
        else:
            return False   
        
    def set_trigger(self,trigger):
        self.trigger=trigger
        
    def get_trigger(self):
        return self.trigger

x=trigger(c.get_text(),'purple cow')
print(x.get_story_trigger())
print(x.get_trigger())
print(x.rise_flag())






























        