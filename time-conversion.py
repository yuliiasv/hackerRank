__author__ = 'jullyt'


# !/bin/python3

def time_conversion(time):
    if time[-2:] == 'PM' and time[:2] != '12':
        hours = int(time[:2]) + 12
        return str(hours) + time[2:-2]
    else:
        if time[:2] == '12':
            return '00' + time[2:-2]
    return time[:-2]

# def timeConversion(time):
#     if time[-2:] == 'PM':
#         if time[:2] != '12':
#             hours = int(time[:2]) + 12
#             return str(hours) + time[2:-2]
#     else:
#         if time[:2] == '12':
#             return '00' + time[2:-2]
#     return time[:-2]

s = input().strip()
result = time_conversion(s)
print(result)
