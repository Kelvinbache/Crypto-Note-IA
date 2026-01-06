from config.config import postgrest
import psycopg

class Postgrest_db():
    def __init__(self):
        self.conn = None

    def connection(self):
        try:
         
         self.conn = psycopg.connect(**postgrest)
         return self.conn 
        
        except Exception as err:
            print(f"this is: {err}") 

    def exit_table(self):        
        try:
            conn = self.connection()
            with conn.cursor() as cur:
             cur.execute("""
                    SELECT EXISTS ( 
                    SELECT 1 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name IN ('users', 'chat', 'login', 'user_test')
                    );
                    """)
            
             consult = cur.fetchone() 

             self.controller(consult[0])
    
        except Exception as err:           
            print(f"this is {err}")

    def create_table(self): 
        conn = self.connection()
        
        try:
            with conn.cursor() as cur:    
             cur.execute("""
               CREATE TABLE "users" (
               "id_user" int PRIMARY KEY,
               "name_user" varchar(255),
               "email_user" varchar(255) UNIQUE,
               "password" varchar(255),
               "credits" int DEFAULT 3);
            """)     
             
             cur.execute("""
              CREATE TABLE "chat" (
              "id_chat" int PRIMARY KEY,
              "chat" text);

            """)
             
             cur.execute("""
             CREATE TABLE "test" (
             "id_test" int PRIMARY KEY,
             "user_id" int,
             "chat_id" int,
             "status" bool DEFAULT false);
            """) 
            
            return conn    

        except Exception:
           conn.rollback()

    def controller(status:bool, self):
       if(not status):     
          print("the table already exists")
       else:
          self.create_table()
 
db = Postgrest_db()