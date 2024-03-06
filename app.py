from find_work import scrape_work_schedule
from create_event import create_event_final

shifts = scrape_work_schedule()
for shiftKey, shiftValue in shifts.items():
    start = shiftValue[0]
    end = shiftValue[1]
    create_event_final(start,end)
