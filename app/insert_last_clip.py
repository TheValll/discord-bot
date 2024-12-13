# Import the required libraries
from connect_bdd import connect_bdd
from space_time import SpaceTime

def insert_last_clip(id_clip, real_date):
    try:
        mydb = connect_bdd()
        mycursor = mydb.cursor()
        real_date = SpaceTime.get_date_sql_format(real_date)
        mycursor.execute(f"insert into last_clips (id_clip, date_upload) value ({id_clip},'{real_date}');")
        mydb.commit()
        return
    except Exception as e:
        print(f"Error: {e}")
