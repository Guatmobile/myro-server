#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import random
import json
import urlparse
import time
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
        make_request(data)
        self.response.write(json.dumps(randList))
        code = Code(columns = randList)
        c_key = code.put()

    def make_request(data):
        json_data = {
            "collapse_key" : "msg",
            "data" : data
            "registration_ids": ['1'],
        }

        url = 'https://android.googleapis.com/gcm/send'
        myKey = "AIzaSyAD9SQqeWGcrSprGEkrjgbeTgEmVbloVFg"
        data = json.dumps(json_data)
        headers = {'Content-Type': 'application/json', 'Authorization': 'key=%s' % myKey}
        req = urllib2.Request(url, data, headers)
        f = urllib2.urlopen(req)
        response = json.loads(f.read())

        ''' self.response.out.write(json.dumps(response,sort_keys=True, indent=2) ) '''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


