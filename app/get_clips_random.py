# Import the required libraries
from connect_bdd import connect_bdd
from insert_last_clip import insert_last_clip

def get_clips_random(real_date):
    try:
        mydb = connect_bdd()
        clip = {}
        mycursor = mydb.cursor()
        mycursor.execute(f"select id_clip, url from clips where id_clip not in (select id_clip from last_clips) order by rand() limit 1")

        for x in mycursor:
            clip["id_clip"] = x[0]
            clip["url"] = x[1]
        
        if not clip:
            message = "No clips available"
        else:
            insert_last_clip(clip["id_clip"], real_date)
            message = clip["url"]

        return message
    except Exception as e:
        print(f"Error: {e}")