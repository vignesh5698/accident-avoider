from firebase import Firebase
import geocoder

from datetime import datetime

now = datetime.now()

config = {
  "apiKey": "AIzaSyD4EwJFr8MTh0lIQmlMMVn2H365WOV08es",
  "authDomain": "demo1-e68cf.firebaseapp.com",
  "databaseURL": "https://demo1-e68cf.firebaseio.com",
  "storageBucket": "demo1-e68cf.appspot.com"
}

def write_to_firebase(driver_name):
  location = geocoder.ip('me').city
  firebase = Firebase(config)
  db = firebase.database()
  current_time = now.strftime("%Y-%m-%d %H:%M:%S")
  data = {"location": location}
  res = db.child("sleep_list").child(driver_name).child(current_time).set(data)
  print(res)
