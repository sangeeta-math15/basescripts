import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from basescript import BaseScript
from argparse import ArgumentParser

username = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')


class SendEmail(BaseScript):
    """
    create class SendEmail
    """
    def send_mail(self, text='Email Body', subject='Hello world',
                  from_email='Sangeeta Math <sangeeta.1rn18mca30@gmail.com>',
                  to_emails=None):

        print(self.args.to_emails)
        msg = MIMEMultipart('alternative')
        msg['from'] = from_email
        msg['To'] = self.args.to_emails
        msg['Subject'] = subject

        text_part = MIMEText(text, 'plain')
        msg.attach(text_part)

        text_part = MIMEText("<h1> This is working</h1>", 'html')
        msg.attach(text_part)

        msg_str = msg.as_string()
        # login to smpt server
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, self.args.to_emails, msg_str)
        server.quit()

    def define_subcommands(self, subcommands):
        super(SendEmail, self).define_subcommands(subcommands)
        add_cmd = subcommands.add_parser("send_mail", help="send email")
        add_cmd.set_defaults(func=self.send_mail)
        add_cmd.add_argument('--to_emails', type=str, help="mail to add")


if __name__ == '__main__':
    SendEmail().start()
