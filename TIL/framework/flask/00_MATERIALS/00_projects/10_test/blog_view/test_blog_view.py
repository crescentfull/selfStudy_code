from db_model.test_db_model import test_db
import os

def test_blog():
    print(os.path.dirname(os.path.realpath(__file__)) )
    print (test_db())