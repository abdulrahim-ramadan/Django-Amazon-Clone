from celery import shared_task
import time

@shared_task
def send_emails():   
    for x in range(40):
        time.sleep(1)
        print(x)

