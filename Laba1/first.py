from datetime import date

# Отримати поточну дату
today = date.today()
day_of_week = today.weekday()  # 0 - понеділок, 6 - неділя

# Визначення статусу дня
if day_of_week >= 5:
    status = "Сьогодні вихідний!"
else:
    status = "Сьогодні робочий день."

# Вивід результатів
print(f"Сьогодні: {today.strftime('%A')}, {status}")
