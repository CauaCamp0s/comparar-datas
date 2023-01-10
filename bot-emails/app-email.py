#import smtplib
#from email.message import EmailMessage
#from senha import senha 
#
##Abrir email
#email_address = 'cauacampos258@gmail.com'
#email_password = senha
#
##Criar email
#msg = EmailMessage()
#msg['Subject'] = 'Email teste envio de email com python'
#msg['From'] = 'cauacampos258@gmail.com'
#msg['To'] = 'cauafps04@gmail.com'
#msg.set_content('O email foi enviado com sucesso, enviado com python')
#
##enviar email
#with smtplib.SMTP_SSL('smtp.gmail.com: 587') as smtp:
#    smtp.login(email_address, email_password)
#    smtp.send_message(msg)



import smtplib
import email.message

def send_email():
    body_email = ''''
    <p>Olá Cauã,</p>
    <p>Email automatico, tenha um bom dia!</p>
    '''
    
    msg = email.message.Message()
    msg['Subject'] = 'Teste envio de email com python'
    msg['From'] = 'cauacampos258@gmail.com'
    msg['To'] = 'cauafps04@gmail.com'
    senha = 'akvcqskunyxhkpuz'
    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)
    
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.connect('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login(msg['From'], senha)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print ('Sent email')
    
send_email()

