import os 
from dotenv import load_dotenv

load_dotenv()


postgrest = {
    "host":os.getenv("DB_HOST"),
    "port":os.getenv("DB_PORT"),
    "dbname":os.getenv("DB_NAME"),
    "user":os.getenv("DB_USER"),
    "password":os.getenv("DB_PASSWORD")
} 

email = {
    "MAIL_USERNAME":os.getenv("MAIL_USERNAME"),
    "MAIL_PASSWORD":os.getenv("MAIL_PASSWORD"),
    "MAIL_FROM":os.getenv("MAIL_FROM"),
    "MAIL_PORT":os.getenv("MAIL_PORT"),
    "MAIL_SERVER":os.getenv("MAIL_SERVER"),
}

geminis = {
  "API_KEYS_GEMINIS":os.getenv("API_KEYS_GEMINIS")
}