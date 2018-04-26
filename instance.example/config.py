# instance.example/config.py
import os

SECRET_KEY = os.urandom(24).encode('hex')
