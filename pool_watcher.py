from twilio.rest import Client
from datetime import datetime
from retrying import retry
from config import Config
from halo import Halo
import requests
import time
import os

# setup variables
config = Config().get()
account_sid = config.get('twilio', 'account_sid')
auth_token = config.get('twilio', 'auth_token')
client = Client(account_sid, auth_token)
done = False


def send_sms(body):
    client.messages.create(
        body=body,
        from_=config.get('twilio', 'from'),
        to=config.get('twilio', 'to')
    )


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


@retry
def get_hashrate():
    response = requests.get(config.get('nanopool', 'url'))
    hashrate = response.json()["data"]
    return hashrate


def animate(current_hashrate):
    with Halo(text=datetime.now().strftime('%Y-%m-%d %H:%M:%S') +
                   ' - hashing at ' + str(current_hashrate) + ' mh/s ', spinner='circle'):
        time.sleep(300)  # Wait 2 minute


def wait_drop():
    # hashrate loop
    current_hashrate = get_hashrate()
    while current_hashrate != 0:
        animate(current_hashrate)
        current_hashrate = get_hashrate()

    # if hashrate is 0 send sms and emal
    send_sms('The rig stopped working!')
    send_email(user=config.get('gmail', 'user'),
               pwd=config.get('gmail', 'pwd'),
               recipient=config.get('gmail', 'recipient'),
               subject=config.get('gmail', 'subject'),
               body='Current hashrate is 0 Mh/s... Operator has been notified.')


def wait_return():
    # hashrate loop
    current_hashrate = get_hashrate()
    while current_hashrate == 0:
        print('Waiting for mining to resume...')
        current_hashrate = get_hashrate()

    # if hashrate is 0 send sms and emal
    send_sms('The rig is hashing again!')
    send_email(user=config.get('gmail', 'user'),
               pwd=config.get('gmail', 'pwd'),
               recipient=config.get('gmail', 'recipient'),
               subject=config.get('gmail', 'subject'),
               body='The rig is working again!')


def main():
    os.system('clear')

    while 1:
        wait_drop()
        wait_return()


if __name__ == '__main__':
    main()
