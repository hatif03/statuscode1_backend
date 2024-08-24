import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase
cred = credentials.Certificate("statuscode.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'statuscode1-c411d.appspot.com'
})


def get_image_url(image_name):
    bucket = storage.bucket()
    blob = bucket.blob(image_name)
    url = blob.generate_signed_url(expiration=3600)  # URL expires in 1 hour
    return url

