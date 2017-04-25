# python-Search-Text

To Search a particular text in a webpage and alert by sending a mail

1. Modify the URL of the page that you want to search.
2. Change the text that you want to find in the page.
3. Modify the Time as in what interval you want to check the site for the text.
4. Modify the SMTP settings with your mail address and the receiving mail address.

Run the script by the following command:
```
python pybotSearchSiteandAlert.py
```

Usecase:

Let's assume, you want to a book a movie/show ticket as soon as it is available and open on the site. You can use the above script to alert you via email when the ticket is available by inputting some keyword that would help the script to identify that the booking is open.

You can vary the time interval at which the script should check for the keyword in the site and mention a number of friends in the to-mail list, so that even if you miss the alert, your friends can book.