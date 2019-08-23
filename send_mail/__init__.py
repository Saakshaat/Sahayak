import getpass
import smtplib
from talk import talk


def send_mail(self):
    from get_command import get_command
    username = input("What is your Google Email address?\t")
    print('Enter Password:\t')
    password = getpass.getpass()
    print(password)
    name = input('What is your name?')
    try:
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(username, password)
        recep = []
        not_done = True
        while not_done:
            recep.append(input("Enter Recipient's Email Address: \t"))
            sat = input("Done?")
            if sat == 'y':
                not_done = False
        sure = 'yes'
        while sure == 'yes':
            talk('What is the subject?')
            subject = get_command()
            talk('What should I tell them?')
            message = get_command()
            content = """Subject: {}\n\n{}\n\nRegards,\n{}""".format(subject.capitalize(),
                                                                     message.capitalize(),
                                                                     name.capitalize())  # The subject goes as the email subject if there are 2 blank
            # lines between it and the email content
            print(content)
            talk('Should I send this?')
            sure = get_command()
            if 'yes' in sure.lower() or 'yeah' in sure.lower() or 'yep' in sure.lower():
                server.sendmail(username, recep, content)
                talk('Sent Mail')
                break
            else:
                # repeat send_mail() from asking for the subject
                talk('What would you like to send instead?')
                continue
        server.quit()
    except ConnectionError:
        talk('Could\'nt connect to server because of {}'.format(ConnectionError))
