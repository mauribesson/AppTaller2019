import pyrebase


config = {
            "apiKey": "AIzaSyBHoVNC2ji7XihvnD22q9SysNl9OGlDapc",
            "authDomain": "apptaller2019.firebaseapp.com",
            "databaseURL": "https://apptaller2019.firebaseio.com",
            "projectId": "apptaller2019",
            "storageBucket": "apptaller2019.appspot.com",
            "messagingSenderId": "171601985099",
            "appId": "1:171601985099:web:fcba3f334a55c6bc6997ce"
        }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
