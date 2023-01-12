import smtplib
import email.message

#text highlighter variable
green_highlighter = '\033[1;36;42m'


smtp = 'smtp.office365.com'
port = 587
email_from = '################'
password = '###########!'
email_to = '####################'
subject = 'Teste envio de email com python 3'
body_email = '''
    <p>Olá Cauã,</p>
    <p>Email automatico, tenha um bom dia!</p>
'''

#crição do email 
def send_email(smtp, port, email_from, password, email_to, subject, body_email) :

#Abrir email e enviar    
    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = email_to
    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)
    
    s = smtplib.SMTP(smtp + ':' + str(port))
    s.connect(smtp, port)
    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print (f'{green_highlighter}Sent email!')
    
send_email(smtp, port, email_from, password, email_to, subject, body_email)
