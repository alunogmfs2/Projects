import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Informações do servidor de e-mail
smtp_host = 'smtp.gmail.com'
smtp_port = 465  # Porta padrão para TLS
smtp_user = 'gabriel.massaro.fraga2011@gmail.com'
smtp_password = 'Gmfs2011'

# Criando a mensagem
mensagem = MIMEMultipart()
mensagem['From'] = smtp_user
mensagem['To'] = 'gabriel.massaro.2conta2011@gmail.com'
mensagem['Subject'] = 'Bem vindo ao seu Jornal Diario'

# Corpo do e-mail
corpo_email = 'Gabriel, você está pronto para o seu Jornal Diario de hoje?'
mensagem.attach(MIMEText(corpo_email, 'plain'))

try:
    # Conectando ao servidor SMTP
    servidor = smtplib.SMTP(smtp_host, smtp_port)
    servidor.starttls()  # Iniciando a conexão segura
    servidor.login(smtp_user, smtp_password)
    texto = mensagem.as_string()
    servidor.sendmail(mensagem['From'], mensagem['To'], texto)
    servidor.quit()
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
