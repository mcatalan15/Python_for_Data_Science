from datetime import datetime 

current_time = datetime.now()

start_date = datetime(1970, 1, 1, 0, 0, 0) # 1 of January of 1970 same as the Example

delta = current_time - start_date

total_secs = delta.total_seconds()

print(f"Seconds since January 1, 1970: {total_secs:,.4f} or {total_secs:e} in scientific notation")

format_date = current_time.strftime("%b %d %Y")

print(format_date)
