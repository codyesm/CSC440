#!/Users/snnot/Desktop/se_project_env

# -*- coding: utf-8 -*-
import os

from wiki import create_app
"""
import calendar

print(calendar.weekheader(3))
print()

print(calendar.month(2020,4))
"""

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console()

#pickle.dump(credentials, open("token.pkl", "wb"))
#credentials = pickle.load(open("token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)

result = service.calendarList().list().execute()


directory = os.getcwd()
app = create_app(directory)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
