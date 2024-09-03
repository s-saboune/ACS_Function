import azure.functions as func
from azure.communication.email import EmailClient
import logging
import os

connection_string = os.getenv("ACS_CONNECTION_STR")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "DoNotReplyICT@a4539235-5e66-4ad5-8fcb-b4bbf56b4d87.azurecomm.net",
            "recipients":  {
                "to": [{"address": "s.saboune@ict.com.qa" }],
            },
            "content": {
                "subject": "Test Email",
                "plainText": "Hello world via email.",
            }
        }

        poller = client.begin_send(message)
        result = poller.result()

        return func.HttpResponse(
             "Emails have been successfuly sent.",
             status_code=200
        )

    except Exception as ex:
        logging.error("Exception has been raised: %s", ex)
        return func.HttpResponse(
             "An Exception has been raised during email sending.",
             status_code=400
        )
