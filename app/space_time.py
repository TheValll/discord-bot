# Import the required libraries
from datetime import datetime, timedelta

class SpaceTime:
  
  # Get the current date
  @staticmethod
  def get_today():
    date_today = datetime.now()
    # Add an offset cause gcp config
    real_date = date_today + timedelta(hours=1)
    date_formatted = real_date.strftime("%d/%m")
    current_hour = real_date.hour
    current_minute = real_date.minute

    return date_today, real_date, date_formatted, current_hour, current_minute
  
  @staticmethod
  def get_date_sql_format(real_date):
    return real_date.strftime("%Y-%m-%d")