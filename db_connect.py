import mysql.connector
from pprint import pprint
from db_dispender import DbDispenser

class DbQueries:

    meetup_list = []
    meetups_after = []
    user_list_introduction = []

    def __init__(self):
        self.db = DbDispenser("localhost", "root", "1234", "meetup_db", "mysql_scripts\\")


    def get_name(self):
        name = input("Kerem adja meg a nevet: ")
        sentence = "SELECT meetups.Id, meetups.StartTime, meetups.Location, meetups.Topic, meetups.Description, meetups.Support \
        FROM meetups INNER JOIN meetupregistrations ON  meetups.id = meetupregistrations.MeetupsId \
        INNER JOIN Users ON Users.Id = meetupregistrations.UsersId WHERE Users.Real_name LIKE '%s'" % name
        pprint(self.db.select(sentence))
        return

    def get_meetups_after(self):
        print(self.db.select("SELECT * FROM meetups WHERE StartTime > '2015/11/27'"))

    def get_user_introducion(self):
        print(self.db.select("SELECT * FROM users WHERE Introduction is not NULL "))

q = DbQueries()
q.get_meetups_after()
print("-" * 20)
q.get_user_introducion()
print("-" * 20)
q.get_name()
