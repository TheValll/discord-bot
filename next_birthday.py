from datetime import timedelta

def next_birthday(dict, date_today):
    
    stop = False
    i = 1

    try:
        while not stop :

            if i > 365:
                stop = True
                
            next_day = date_today + timedelta(days=i)
            date_formatted = next_day.strftime("%d/%m")

            for key, value in dict.items():
                if value == date_formatted:
                    return key, value
            i += 1
    except:
        name, date = "error"
        return name, date