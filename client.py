from StringIO import StringIO
from mock import Mock
import gmail_client
import requests
import email


REQUEST_COFFEE_API = 'http://127.0.0.1:5000/api/request-coffee'


def wrapper_message_from_filename(file_path):

    with open(file_path, 'r') as f:
        raw_message = email.message_from_file(f)
        parsed_email = gmail_client.message.ParsedEmail(raw_message)
        message = Mock()
        message.to = raw_message['to']
        message.fr = raw_message['from']
        message.subject = raw_message['subject']
        message.body = parsed_email.txt
        message.html = parsed_email.html
        message.attachments = parsed_email.attachments
        return message


def main(path):
    message = wrapper_message_from_filename(path)
    a = message.attachments[0]
    requests.post(REQUEST_COFFEE_API,
                  data={'location_email': message.to,
                        'user_email': message.fr},
                  files={a.name: StringIO(a.content)})


if __name__ == '__main__':

    test_path = 'data/user-email.txt'
    main(test_path)
