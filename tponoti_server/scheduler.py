import scraper
import schedule
from pyfcm import FCMNotification
import time
DATABASE = "db.sqlite3"


conn = schedule.create_connection(DATABASE)
all_tokens = schedule.select_all_tasks(conn)
TOKEN = []
for i in all_tokens:
    TOKEN.append(i[2])
print TOKEN
firebase = open('firebase.txt', 'r')
key = firebase.readline().strip()
FIREBASE_API_KEY = key
print FIREBASE_API_KEY

def get_all_tokens():
    conn = schedule.create_connection(DATABASE)
    all_tokens = schedule.select_all_tasks(conn)
    TOKEN = []
    for i in all_tokens:
        TOKEN.append(i[2])
    return TOKEN


def send_push(tokens):
    push_service = FCMNotification(api_key=FIREBASE_API_KEY)
    notis = []
    try:
        notis = scraper.return_list()
    except:
        return []
    if notis:
        for i in notis:
            message_title = "Update Notification"
            message_body = i
            result = push_service.notify_multiple_devices(registration_ids=tokens, message_title=message_title, message_body=message_body, sound="default")
    else:
        print "Nothing New..."
        pass

if __name__ == "__main__":
    while True:
        print "Getting Tokens....."
        toki = get_all_tokens()
        print "Sending Notifications..."
        send_push(toki)
        time.sleep(120)

