# Import the required libraries
from connect_bdd import connect_bdd
from datetime import timedelta

def get_next_birthday(server_name, date_today):
    # Get all name and birthday dates from a server name
    try:
        mydb = connect_bdd()
        mycursor = mydb.cursor()
        birthday_dict = {}
        stop = False
        i = 1
        mycursor.execute(f"select m.member_name, m.member_birthday_date from members m inner join servers s on m.server_id = s.server_id where s.server_name = '{server_name}'")

        for x in mycursor:
            birthday_dict[x[0]] = x[1]

    except Exception as e:
        print(f"Error: {e}")
    
    # Get the next birthday for the server name list
    try:
        while not stop :
            # Secure infinit loop
            if i > 366:
                stop = True

            next_day = date_today + timedelta(days=i)
            date_formatted = next_day.strftime("%d/%m")

            for key, value in birthday_dict.items():
                if value == date_formatted:
                    return key, value
            i += 1
    except:
        name, date = "error"
        return name, date