from exchangelib import Credentials, Account, Configuration,DELEGATE,Message,Mailbox
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# bypass the SSL verification
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

# username & password
username = input("请输入邮件名称，格式参考：CCIC-NET\\800016256")
password = input("请输入密码，区分大小写")
credentials = Credentials(username, password)
# server address
config = Configuration(server='mail.ccic-net.com.cn', credentials=credentials)
print("config is completed")

myAccount = Account(primary_smtp_address='mengxh@ccic-net.com.cn',  config=config, autodiscover=False, access_type=DELEGATE)
print("account is connected")


# Create an Email

newMail = Message(
    account=myAccount,
    subject='Email sending test by using Python',
    body='This email is sent from MXH by using Python',
    to_recipients=[


        Mailbox(email_address='mengxh@ccic-net.com.cn'),

        Mailbox(email_address='liguangpshx@ccic-net.com.cn')
    ]

        # ,
    # cc_recipients=['carl@example.com', 'denice@example.com'],  # Simple strings work, too
    # bcc_recipients=[
    #     Mailbox(email_address='erik@example.com'),
    #     'felicity@example.com',
    # ],  # Or a mix of both
)
# can't fount it from sent-mail-box
# newMail.send()

# can be found in the sent-mail-box
newMail.send_and_save()
