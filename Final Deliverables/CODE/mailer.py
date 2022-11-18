from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from bodyHTMLRender import getHTMLBody

def sendMailThroughSendGrid(body,reciever):
    message = Mail(
        from_email='khariharan066@gmail.com',
        to_emails=reciever,
        subject='Hee Hoo, News Update!!!',
        html_content=body)
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
