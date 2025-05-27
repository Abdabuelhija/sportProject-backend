from dotenv import load_dotenv
import os
from pathlib import Path

MONGO_URL = os.getenv('MONGO_URL')
MONGO_DBNAME = os.getenv('MONGO_DBNAME')
SECRET_KEY=os.getenv('SECRET_KEY')

CLOUDINARY_NAME=os.getenv('CLOUDINARY_NAME')
CLOUDINARY_API_KEY=os.getenv('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET=os.getenv('CLOUDINARY_API_SECRET')

EMAIL_SENDER=os.getenv('EMAIL_SENDER')
EMAIL_SENDER_PASS=os.getenv('EMAIL_SENDER_PASS')
EMAIL_SERVICE=os.getenv('EMAIL_SERVICE')

ORIGIN=os.getenv('ORIGIN')

PORT=os.getenv('PORT')