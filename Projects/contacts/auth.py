import datetime
import threading

from Projects.contacts.queries import get_user_by_email, add_user_query, add_verification_code, get_user_code, \
    update_user_status, update_user_is_login
from Projects.contacts.utils import get_verification_code


def send_verification_code(email: str, code: int):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    sender_email = "sanjarbekwork@gmail.com"
    password = "rasu ofds znzu xund"

    subject = "Verification Code"
    body = f"Your verification code: {code}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
    except Exception as e:
        print(e)


def register():
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Passwords do not match")
        return register()

    if get_user_by_email(email=email):
        print("Email already registered")
        return register()

    if add_user_query(params=(full_name, email, password,)):
        code = get_verification_code(email=email)
        email_thread = threading.Thread(target=send_verification_code, args=(email, code,))
        email_thread.start()
        add_verification_code(email=email, code=code)
        return True
    return False


def activate_email():
    email = input("Enter your email: ")
    code = int(input("Enter your verification code: "))

    user_code = get_user_code(email=email, code=code)
    if user_code:
        current_time = datetime.datetime.now()
        diff = current_time - user_code[-1]
        minute = diff.total_seconds() // 60
        if minute > 20:
            print("Your verification code expired")
            return False

        update_user_status(email=email, status=1)
        print("Your email is verified, you can login now")
        return True
    else:
        print("Your verification code is not valid")
        return False


def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    user = get_user_by_email(email=email)
    if user and user[3] == password:
        if user[-1] == 0:
            print("Please verify your email")
            return activate_email()
        else:
            update_user_is_login(email=email, is_login=1)
            return True
    return False
