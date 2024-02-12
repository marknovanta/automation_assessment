#!/usr/bin/env python3


while True:
    try:
        h_to_automate = int(input("Hours to automate: "))
    except ValueError:
        print("Input an integer number")
        continue
    else:
        break

while True:
    try:
        m_per_week = int(input("Minutes to complete the task per week: "))
    except ValueError:
        print("Input an integer number")
        continue
    else:
        break

h_to_minutes = h_to_automate * 60
weeks = h_to_minutes / m_per_week
divisor = '-' * 21

print(f'{divisor}\n{round(weeks)} weeks to have benefits')

# hours to automate < (minutes to perform a task per week)