# Import the required libraries
from connect_bdd import connect_bdd
from space_time import SpaceTime
from exception_condition import exception_condition_sql

def get_leaderboard(real_date, server_name):
    try:
        mydb = connect_bdd()
        mycursor = mydb.cursor()
        leaderboard = {}
        real_date = SpaceTime.get_date_sql_format(real_date)
        mycursor.execute(f"select m.member_name, floor(coalesce(sum((l.points * l.bonus / 100) + l.points), 0)) as total from members m left join leaderboard l on m.id_member = l.id_member and year(l.date_obtention) = year('{real_date}') and month(l.date_obtention) = month('{real_date}') inner join servers s on m.server_id = s.server_id where s.server_name = '{server_name}' and m.member_name not in ({exception_condition_sql}) group by m.member_name order by total desc;")

        for x in mycursor:
            leaderboard[x[0]] = x[1]

        return leaderboard
    except Exception as e:
        print(f"Error: {e}")