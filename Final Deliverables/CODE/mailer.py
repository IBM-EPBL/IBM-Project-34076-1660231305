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
        key = "SG."+"sIO"+"wV5YZ"+"Qruer0f4ZUT_n"+"w.ZJ3XN8"+"5WSbuvo"+"3dNSpZy8"+"Oag9cewK9"+"E1aAO8J1s-BK4"
        sg = SendGridAPIClient(key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

sendMailThroughSendGrid("Hi","santymurugan8@gmail.com")