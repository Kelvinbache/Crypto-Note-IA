from fastapi_mail import ConnectionConfig , FastMail, MessageSchema, MessageType
from config.config import email

class Email():
    def __init__(self, config:dict):

        self.mail_username=config.get("MAIL_USERNAME"),
        self.mail_password=config.get("MAIL_PASSWORD"),
        self.mail_from=config.get("MAIL_FROM"),
        self.mail_port=config.get("MAIL_PORT"),
        self.mail_server=config.get("MAIL_SERVER")

    def connection(self):
        try:
            config_connection = ConnectionConfig(
                MAIL_USERNAME = self.mail_username,
                MAIL_PASSWORD = self.mail_password,
                MAIL_FROM = self.mail_from,
                MAIL_PORT = self.mail_port,
                MAIL_SERVER = self.mail_server,
                MAIL_STARTTLS = True,
                MAIL_SSL_TLS = False,
                USE_CREDENTIALS = True,
                VALIDATE_CERTS = True,
            )

            return config_connection

        except Exception as err:
            return f" this is err: {err}"


    async def create_emai(self):
        html = """<p>Thanks for using Fastapi-mail</p> """
        try:
            message = MessageSchema(
                    subject="Confirmación de Cuenta",
                    recipients=[self.mail_username],
                    body=html,
                    subtype=MessageType.html
            )

            fm = FastMail(self.connection())
        
            await fm.send_message(message=message)
        
            return "ok"
        
        except Exception as err:
            return f"this is error:{err}"

scheme_email = Email(email)                