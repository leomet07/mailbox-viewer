import pyrebase

config = {
    "apiKey": "AIzaSyAjM9zJgZTtQahKkbt2sNyw4DBU74BFWOs",
    "authDomain": "mailbox-alarm.firebaseapp.com",
    "databaseURL": "https://mailbox-alarm.firebaseio.com",
    "projectId": "mailbox-alarm",
    "storageBucket": "mailbox-alarm.appspot.com",
    "messagingSenderId": "718325752978",
    "appId": "1:718325752978:web:bf60ffc63b6e26b259724b",
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()


def put_img(filename, storagename):

    path_on_cloud = "images/" + str(storagename)
    path_local = str(filename)
    storage.child(path_on_cloud).put(path_local)
