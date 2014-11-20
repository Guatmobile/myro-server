import webapp2
import random
import json
import urlparse
import time
import urllib2
from google.appengine.ext import db

class Code(db.Model):
    columns = db.ListProperty(long, required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #check url
        url = self.request.url
        parsed = urlparse.urlparse(url)
        element = str(urlparse.parse_qs(parsed.query)['key'])

        db_items = Code.all()
        for item in db_items:
            item.delete()

        if(element != "['6969']"):
            return;

        randList = [random.randint(0,1) for i in range(9)]
        randList[0] = 1
        randList[8] = 1

        self.make_request(randList)
        self.response.write(json.dumps(randList))

        code = Code(columns = randList)
        c_key = code.put()

    def make_request(self, randList):
        json_data = {
            "collapse_key" : "msg",
            "data" : {
                "random_list": randList,
                "identifier": 0
            },
            "registration_ids": ['APA91bGnfiwRXsiRUy8mXC-lIasZmWvme6sC3NthuxYv1gIUyASHZT_nXt3xmXZa4emveDhUHq1l-hxrEmJ4qf0TEZujf_LxWV3IcMgkYherEhL8KygIh3kmtKwzvBUN5gZSWkRL3jfVoi45bH2p4wG8LIEAhfi7mTdTt7QUYz_t8TS4IgvMb8E']
        }

        url = 'https://android.googleapis.com/gcm/send'
        myKey = "AIzaSyAD9SQqeWGcrSprGEkrjgbeTgEmVbloVFg"
        data = json.dumps(json_data)
        headers = {'Content-Type': 'application/json', 'Authorization': 'key=%s' % myKey}
        req = urllib2.Request(url, data, headers)
        f = urllib2.urlopen(req)
        response = json.loads(f.read())
        # self.response.out.write(json.dumps(response,sort_keys=True, indent=2) )

class CheckHandler(webapp2.RequestHandler):
    def get(self):
        #check url
        url = self.request.url
        parsed = urlparse.urlparse(url)
        check = str(urlparse.parse_qs(parsed.query)['check'])
        self.response.write(check)
        self.make_request(check)

    def make_request(self, check):
        json_data = {
            "collapse_key" : "msg",
            "data" : {
                "correct_code": check,
                "identifier": 1
            },
            "registration_ids": ['APA91bGnfiwRXsiRUy8mXC-lIasZmWvme6sC3NthuxYv1gIUyASHZT_nXt3xmXZa4emveDhUHq1l-hxrEmJ4qf0TEZujf_LxWV3IcMgkYherEhL8KygIh3kmtKwzvBUN5gZSWkRL3jfVoi45bH2p4wG8LIEAhfi7mTdTt7QUYz_t8TS4IgvMb8E']
        }
        url = 'https://android.googleapis.com/gcm/send'
        myKey = "AIzaSyAD9SQqeWGcrSprGEkrjgbeTgEmVbloVFg"
        data = json.dumps(json_data)
        headers = {'Content-Type': 'application/json', 'Authorization': 'key=%s' % myKey}
        req = urllib2.Request(url, data, headers)
        f = urllib2.urlopen(req)
        response = json.loads(f.read())
        # self.response.out.write(json.dumps(response,sort_keys=True, indent=2) )

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/2', CheckHandler)
], debug=True)

