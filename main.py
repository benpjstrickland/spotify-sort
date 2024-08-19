from dotenv import load_dotenv
import os 

load_dotenv()

# got this to work for pc + mac
print(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))