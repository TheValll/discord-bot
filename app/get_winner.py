# Import the required libraries
from connect_bdd import connect_bdd
from exception_condition import exception_condition_sql

def get_winner(server_name):
    try:
        mydb = connect_bdd()
        winner = {}
        mycursor = mydb.cursor()
        mycursor.execute(f"select m.*, s.server_name from members m inner join servers s on m.server_id = s.server_id where s.server_name = '{server_name}' and m.member_name not in ({exception_condition_sql}) order by rand() limit 1")

        for x in mycursor:
            winner = {
                "id_member": x[0],
                "server_id": x[1],
                "member_name": x[2],
                "member_birthday_date": x[3],
                "server_name": x[4]
            }
        
        return winner
    except Exception as e:
        print(f"Error: {e}")