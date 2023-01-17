import smtplib
import email.message

#crição do email 

def send_email():
    body_email = ''''
    <p>Olá Cauã,</p>
    <p>Email automatico, tenha um bom dia!</p>
    '''

#Abrir email e enviar    

    msg = email.message.Message()
    msg['Subject'] = 'Teste envio de email com python'
    msg['From'] = 'cauacampos258@gmail.com'
    msg['To'] = 'caua.ciee@sergipegas.com.br'
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
 
