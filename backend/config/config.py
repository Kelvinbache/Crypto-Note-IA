import os 
from dotenv import load_dotenv

load_dotenv()


postgrest = {
    "DB_HOST":os.getenv("DB_HOST"),
    "DB_PORT":os.getenv("DB_PORT"),
    "DB_NAME":os.getenv("DB_NAME"),
    "DB_USER":os.getenv("DB_USER"),
    "DB_PASSWORD":os.getenv("DB_PASSWORD")
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