
from models import *

def create_tables():
    db.connect()
    db.create_tables([Source, Request, Message])
    db.close()
