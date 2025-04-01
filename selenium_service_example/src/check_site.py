
import time

import boto3 as boto3

from selenium_service_example.src.controller import check_site
import pymssql
import os

# run file, here service is called

SENDER = "me@test.com"
RECIPIENT = "another_man@test.com"
CONFIGURATION_SET = "ConfigSet"
BODY_TEXT = ("Body text")

SUBJECT_STARTED = "Started widgeting"
BODY_HTML_STARTED = """<html>
<head></head>
<body>
  <h1>Client side widget test Started...</h1>
  <p> just body, dont know what to send</p>
</body>
</html>
            """
SUBJECT_FAILED = "FAILED widgeting"
BODY_HTML_FAILED = """<html>
<head></head>
<body>
  <h1>Widget test failed for some reason(</h1>
  <p> just body, dont know what to send</p>
</body>
</html>
            """
# The character encoding for the email.
CHARSET = "UTF-8"



if __name__ == "__main__":
    # aws client, environment variables as credentials
    ses_client = boto3.client('ses',
                             aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                             aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                             region_name=os.getenv("AWS_DEFAULT_REGION")
                             )

    # this module sends notification when service starts, (I should have hidden it to another class or function,
    # but I am lazy and service is small)
    try:
        client = ses_client
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML_STARTED,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT_STARTED,
                },
            },
            Source=SENDER
        )

        print("Started!")

        # next lines are just test data
        # #
        # WIDGET_ID = [
        #     # "e7b55476-952f-4f6b-bd12-08dc00805dd0",
        #     # "f0685c44-e4fa-41ee-bd13-08dc00805dd0",
        #     # "046e65f0-2e64-4ca5-dfa3-08dba3b01c5f",
        #     # "fb62c0a7-a943-41ad-1a33-08dba21da2ef",
        #     # "f981d6eb-c217-479a-bd14-08dc00805dd0",
        #     # "6f3a93c0-2a86-4fb0-65aa-08dbac546120",
        #     # "6a1b6bd1-f096-43d3-65a9-08dbac546120",
        #     # "a890f6b2-71db-4588-65a1-08dbac546120",
        #     # "1e0dfc86-fdbc-499b-b484-08dba6ddbf3d",
        #     # "dd0fa3bb-a430-44f8-b486-08dba6ddbf3d",
        #     "72aa3c60-5bab-4b58-bd37-08dc00805dd0",
        #     # "5ba49879-e5a1-42a1-cb25-08db97f31e55",
        #     # "dd0fa3bb-a430-44f8-b486-08dba6ddbf3d"
        # ]

        # here I start to connect to database, variables are also secured
        # envs
        host = os.getenv("DB_HOST")
        db = os.getenv("DB")
        user = os.getenv("USER")
        password = os.getenv("PASS")

        conn = pymssql.connect(
            server=host,
            user=user,
            password=password,
            database=db,
            as_dict=False
        )

        # SQL query to get test data
        GET_URLS = "SELECT id,WidgetConfigurationId,Url FROM WidgetsHealthCheck"
        cursor = conn.cursor()
        cursor.execute(GET_URLS)

        URL_ROWS = cursor.fetchall()
        # print(URL_ROWS)


        # parse data from query
        URL_ID = [url[0] for url in URL_ROWS]
        WIDGET_ID = [url[1] for url in URL_ROWS]
        URL = [url[2] for url in URL_ROWS]

        # declare empty list to fill it later
        db_report_list = []

        # the test itself
        for i in range(0, len(URL)):
            result = check_site(URL[i], WIDGET_ID[i])
            # print("result -", result[0], ",", result[1], ",", URL[i])

            # biuld the line
            db_report_row = [URL_ID[i], time.strftime('%Y-%m-%d %H:%M:%S'), result[1]]
            print(i, db_report_row)
            # add row to list, tuple format just to fit in the database
            db_report_list.append(tuple(db_report_row))
            # statuses of test subject
            # 0 - widget works as expected
            # 1 - widget doesn't work
            # 2 - can't reach widget
            # 3 - can't reach website
            # 4 - widget works, no spaces available

        print(db_report_list)
        # reporting query, whole batch at one time to save time
        insert_db_reports = "INSERT INTO WidgetsHealthStatus (WidgetHealthCheckId, DateTime, Status) VALUES (%s, %s, %s)"
        cursor.executemany(insert_db_reports, db_report_list)

        conn.commit()
        cursor.close()
        conn.close()

        print("JOB IS DONE")
        print("JOB IS DONE")
        print("JOB IS DONE")

    # aws notification in case if test crashed
    except:
        client = ses_client
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML_FAILED,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT_FAILED,
                },
            },
            Source=SENDER
        )
        print("aboba")

