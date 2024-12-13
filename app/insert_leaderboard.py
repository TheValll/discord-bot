# Import the required libraries
from connect_bdd import connect_bdd
from space_time import SpaceTime

def insert_leaderboard(winner, points, percentage, real_date):
    try:
        mydb = connect_bdd()
        mycursor = mydb.cursor()
        real_date = SpaceTime.get_date_sql_format(real_date)
        mycursor.execute(f"insert into leaderboard (id_member, points, bonus, date_obtention) value ({winner["id_member"]}, {points}, {percentage}, '{real_date}');")
        mydb.commit()
        return
    except Exception as e:
        print(f"Error: {e}")
