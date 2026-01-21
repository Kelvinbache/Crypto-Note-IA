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

    async def tables(self):        
        try:
            conn = self.connection()
            with conn.cursor() as cur:
             cur.execute("""
                    SELECT EXISTS ( 
                    SELECT 1 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name IN ('users', 'chat', 'test')
                    );
                    """)
            
             consult = cur.fetchone() 
             
             if consult[0]:
                print("the table already exists")         
             else:   
                 cur.execute("""
                 CREATE TABLE IF NOT EXISTS test (
                 id_test SERIAL PRIMARY KEY,
                 user_id int UNIQUE,
                 chat_id int UNIQUE,
                 status bool DEFAULT false);
                """) 
                
                 cur.execute("""
                   CREATE TABLE IF NOT EXISTS users (
                    id_user SERIAL PRIMARY KEY,
                    name_user varchar(255),
                    email_user varchar(255) UNIQUE,
                    password varchar(255),
                    credits int DEFAULT 3);
                """)     
                 
                 cur.execute("""
                  CREATE TABLE IF NOT EXISTS chat (
                  id_chat SERIAL PRIMARY KEY,
                  chat text);
    
                """)
                 
                 cur.execute("""
                       ALTER TABLE users 
                       ADD CONSTRAINT fk_user_test 
                       FOREIGN KEY (id_user) REFERENCES test (user_id);""") 
        
                 cur.execute("""
                            ALTER TABLE chat 
                            ADD CONSTRAINT fk_chat_test 
                            FOREIGN KEY (id_chat) REFERENCES test (chat_id);""")
                
            conn.commit()

        except Exception as err:           
            conn.rollback()
            print(f"this is {err}")

   
    async def ini_db(self):
        try:
            await self.tables()

            if self.conn is None:
                return self.conn
            else:
                return self.conn
            
        except Exception as e:
            print(f"this is error ini_db: {e}")
 
db = Postgrest_db()