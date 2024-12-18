from django.core.mail import EmailMessage

def send_assignment_email():
    subject = "Python (Selenium) Assignment - Saandeep CS"
    body = "git repo link: https://github.com/saandeepcs/selenium_proj.git"
    from_email = "saandeepcs010@gmail.com" 
    to_email = ["tech@themedius.ai"]
    cc_email = ["hr@themedius.ai"]

    email = EmailMessage(subject, body, from_email, to_email, cc=cc_email)
    email.send()

    print("Email sent successfully!")
