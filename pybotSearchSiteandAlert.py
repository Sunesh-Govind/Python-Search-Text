# Import mechanize to download content from the page
import mechanize

# Import BeautifulSoup to parse the content downloaded
from bs4 import BeautifulSoup

# Import Time for time functions
import time

# Import smtplib to send mail
import smtplib

# True by default
while True:
    # set the url to check,
    url = "https://www.google.com"
    # download the page
    browser = mechanize.Browser()
    browser.open(url)
    # Obtain response from the page
    response = browser.response().read()
    # parse the downloaded content from the page
    soup = BeautifulSoup(response, "lxml")
    #Counter for number of checks
    count = 1
    # if there is no occurrence of the text entered,
    if str(soup).find("English") == -1:
        # wait 60 seconds (change the time(in seconds) as you wish),
        print('Checking - ' + str(count) + 'th Time')
        time.sleep(60)
        count += 1
        # continue with the script
        continue

    # If the word occurs,
    else:
        # create an email message with a message,
        msg = 'Subject: Hey, CHECK the site_name that you wanted to observe!'
        # set the 'from' address,
        fromaddr = 'from@example.com'
        # set the 'to' addresses,
        toaddrs  = ['to1@example.com','to2@example.com','to3@example.com']

        # Setup the email server,
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        # add the from address account login name and password,
        server.login("from@example.com", "password")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

        break