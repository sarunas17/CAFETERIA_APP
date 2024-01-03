from datetime import datetime, timedelta
current_time = datetime.now()

time_format = "%H:%M"
time_slots = ["12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00"]

new_time_slots = [slot.strftime(time_format) for slot in [datetime.strptime(slot, time_format) for slot in time_slots if slot >= current_time.strftime(time_format)]]
print("Available time slots:")
for i, slot in enumerate(new_time_slots, 1):
    print(f"{i}. {slot}")

choice = input("Choose a time slot number: ")

choice_index = int(choice) - 1
chosen_time = datetime.strptime(new_time_slots[choice_index], time_format)
time_till = chosen_time + timedelta(hours=2)

print(f"Your reservation time is from {chosen_time.strftime(time_format)} to {time_till.strftime(time_format)}")

      


    


# datetime_obj1 = datetime.strptime(time1, time_format)
# datetime_obj2 = datetime.strptime(time2, time_format)



# nauji = [slot.replace(":", "") for slot in time_slots if slot >= time_string] 

# print(nauji)

# print("Available Time Slots:")
# for i, slot in enumerate(time_slots, 1):
#     print(f"{i}. {slot}")


# choice = input("Choose a time slot number: ")


# choice_index = int(choice) - 1
# print(time_slots[choice_index])







