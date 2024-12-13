# Import the required libraries
from connect_bdd import connect_bdd

def get_server_id(server_name):
    try:
        mydb = connect_bdd()
        channel_id = None
        mycursor = mydb.cursor()
        mycursor.execute(f"select channel_id from servers where server_name = '{server_name}'")

        for x in mycursor:
            channel_id = x[0]
        
        return channel_id
    except Exception as e:
        print(f"Error: {e}")