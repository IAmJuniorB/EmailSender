# Email Sender Program

This program sends an email to a recipient using Gmail's SMTP server.

## Requirements

To use this program, you need to have a Gmail account and create an app password for this program. Here are the steps to create an app password:

1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords?).
2. Select the app you want to generate the app password for.
3. Follow the on-screen instructions to generate the app password.
4. Copy the generated app password and use it as the `email_password` argument when running the program.

## Usage

To use the program, call the `send_an_email` method of the `EmailSender` class with the following arguments:

- `email_sender`: a string representation of your email address.
- `email_password`: a string representation of the app password you generated for this program.
- `email_receiver`: a string representation of the recipient's email address.
- `subject`: the subject line of the email you are sending.
- `body`: the body message of the email you want to send.

The `send_an_email` method returns "Message sent" if the email was sent successfully.

### Example

```python
EM = EmailSender()
    
EM.send_an_email("whoever@gmail.com",
                 "ThIsIsMyPaSsWoRd",
                 "WhoeverThisIs@gmail.com",
                 "Subject",
                 """
Body message
""")
