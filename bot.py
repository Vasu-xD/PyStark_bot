from pystark import Stark
from database.users_sql import Users


bot = Stark()
Users.__table__.create(checkfirst=True)

if __name__ == "__main__":
    bot.activate()
