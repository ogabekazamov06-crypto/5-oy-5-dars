# import asyncio
#
# async  def generate_number():
#     for i in range(1,11):
#         print(i)
#         await asyncio.sleep(i)
#
#
# async  def messsage():
#     print("Asinxron ishladi")
#
# async def main():
#     task1 = generate_number()
#     task2 = messsage()
#
#     await asyncio.gather(task1,task2)
#
# asyncio.run(main())



import  requests
from pprint import pprint

from datetime import datetime

city_name = 'Fergana'
API_key = 'b01e7608c07f15c54ff9d9b64d478705'

parametrs = {
    'q':city_name,
    'appid':API_key,
    'units':'metric'
}
req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?', params=parametrs)
try:
    data = req.json()
    pprint(data)
    temp = data['main']['temp']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    timezone = data['timezone']
    sunsise = datetime.utcfromtimestamp(sunrise+timezone)
    sunset = datetime.utcfromtimestamp(sunset+timezone)
    print(sunrise, sunset)
except Exception as e:
    print(e)