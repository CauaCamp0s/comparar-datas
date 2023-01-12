import smtplib
import email.message

#text highlighter variable
green_highlighter = '\033[1;36;42m'

#crição do email 
def send_email():
    body_email = ''''
    <p>Olá Cauã,</p>
    <p>Email automatico, tenha um bom dia!</p>
    '''

#Abrir email e enviar    
    msg = email.message.Message()
    msg['Subject'] = 'Teste envio de email com python'
    msg['From'] = '################'
    msg['To'] = '#########@gmail.com'
    senha = '#############'
    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)
    
    s = smtplib.SMTP('smtp.office365.com:587')
    s.connect('smtp.office365.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login(msg['From'], senha)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print (f'{green_highlighter}Sent email!')
    
send_email()

