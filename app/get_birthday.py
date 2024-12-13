# Import the required libraries
from connect_bdd import connect_bdd

def get_birthday(date_formatted):
    try:
        mydb = connect_bdd()
        birthdays = []

        mycursor = mydb.cursor()
        mycursor.execute(f"select m.member_name, s.server_name, s.channel_id, m.member_birthday_date from members m inner join servers s on m.server_id = s.server_id where m.member_birthday_date = '{date_formatted}'")

        for x in mycursor:
            birthday = {
                "member_name": x[0],
                "server_name": x[1],
                "channel_id": x[2],
                "member_birthday_date": x[3],
            }
            birthdays.append(birthday)
        
        return birthdays
    except Exception as e:
        print(f"Error: {e}")