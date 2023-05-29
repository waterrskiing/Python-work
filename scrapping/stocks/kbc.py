import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText

# Define the URL you want to scrape
url = 'https://www.kinhbaccity.vn/news/vi/kbc-shareholder-relations/announcements'

# Define the email addresses involved in the sending process
to_address = 'phamthanhtung.epu91@gmail.com'
from_address = 'mr.overnight.a2@gmail.com'
password = 'exkcnarjcsgqwyey'

# Define the email subject
subject = 'New post on KBC-QHCD!'

# Define the interval (in hours) at which you want to scan the website
interval = 24


# Define the function that checks for new posts and sends the email
def check_for_new_post():
    # Send a GET request to the website and get the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    # Find date of latest update
    latest_update = soup.find_all('dd', {"class": "create"})
    latest_date = latest_update[0].get_text().replace('\n', '')

    # Check if any of the dates are new since the last time we checked
    new_links = []
    with open('links.txt', 'r') as f:
        old_dates = f.read().splitlines()
        if latest_date not in old_dates:
            new_links.append(latest_date)
    # If there are new links, send an email
    if new_links:
        print(new_links)
        msg = MIMEText(f'Hello from BOT! New post at {url}')
        send_email(subject, msg)
        # Write the new links to the links.txt file
        with open('links.txt', 'w') as f:
            f.write('\n'.join(new_links))


def send_email(subject, content):
    content['Subject'] = subject
    content['From'] = from_address
    content['To'] = to_address
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_address, password)
        smtp.sendmail(from_address, to_address, content.as_string())


# Keep checking for new posts at the specified interval
while True:
    check_for_new_post()
    time.sleep(interval * 3600)
