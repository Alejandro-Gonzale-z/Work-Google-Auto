# Work-Google-Auto
A python script that scrapes my Urban Air work schedule from Optim8.com and then integrates with Google Calendar. I used selenium to access the scheduling site, then used beautiful soup to parse the html data. I used Google Calendar's Python Quickstart guide to create the events according to the data. 

# Token Expiration
Google Auth Tokens tend to expire within a 7-14 day period. When the Tokens expire, running app.py or calendar_api.py will result in an error that states "Token has been expired or revoked", at this point you must delete the token.json file and run the code again. You will then be asked to sign into google and the program will create a new token.json file. 

# Chrome Updates
Google Chrome automates updates and does not give users a choice of whether to downgrade or not. This results in chromedriver versions becoming outdated. If errors occur regarding the chromedriver version visit https://googlechromelabs.github.io/chrome-for-testing/#stable to download the latest version of chromedriver. 

# Installation
To install the dependencies run the following command: pip install -r requirements.txt

