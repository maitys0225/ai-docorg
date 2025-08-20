import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('maity.siddhartha@gmail.com', 'your_app_password')
mail.select('inbox')

result, data = mail.search(None, 'ALL')
mail_ids = data[0].split()

for mail_id in mail_ids:
    result, msg_data = mail.fetch(mail_id, '(RFC822)')
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)
    subject = msg['subject']
    body = msg.get_payload(decode=True)
    print(subject, body)

mail.logout()