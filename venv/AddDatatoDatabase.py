import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os 
from firebase_admin import credentials, firestore, initialize_app 

data = os.path.abspath(os.path.dirname(__file__)) + '\\smarttttt-94151-firebase-adminsdk-v5sfa-9fbface78c.json'
cred = credentials.Certificate(data)
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://smarttttt-94151-default-rtdb.europe-west1.firebasedatabase.app/"
})


print("hhh")
ref = db.reference('Students')
data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    print(key,value)
    ref.child(key).set(value)









