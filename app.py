import os
from find_work import scrape_work_schedule
from create_event import create_event_final

#if google auth token expiration error, delete the token and run the program again
try: 
    shifts = scrape_work_schedule()
    for shiftKey, shiftValue in shifts.items():
        start = shiftValue[0]
        end = shiftValue[1]
        create_event_final(start,end)
except:
    os.remove("./CREDENTIALS/token.json")
    shifts = scrape_work_schedule()
    for shiftKey, shiftValue in shifts.items():
        start = shiftValue[0]
        end = shiftValue[1]
        create_event_final(start,end)