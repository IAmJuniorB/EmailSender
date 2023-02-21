from email.message import EmailMessage
import ssl, smtplib

class EmailSender():
    def send_an_email(self, email_sender=str, email_password=str, email_receiver=str, subject=str, body=str):
        """
        Sends an email address to a recipient 
        
        Args:
        - email_sender: a string representation of your email address
        - email_password: a string representaion of your password for this email address
        that is given to you by going to myaccount.google.com
        and creating a password specifically for this program
        - email_receiver - a string representation of reipient's email address
        - subject - the subject line of the email you are sending
        - body - the body message of the email you want to send
        
        Returns:
        - an output stating "message sent" if completed succesfully
        
        Raises:
        - ValueError: if the email addresses do not exit
        """
        
        
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            print("Message sent")
    
EM = EmailSender()
    
EM.send_an_email("bonfanti7414@gmail.com",
                 "hezvhavrfpyberdc",
                 "briannap582@gmail.com",
                 "Python Email",
                 """
I sent this from my own program
""")