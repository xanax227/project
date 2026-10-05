seconds = int(input())
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s).")