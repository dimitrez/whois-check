import pythonwhois
import datetime
from email.mime.text import MIMEText
from subprocess import Popen, PIPE


def check_domain(domain):

    q = pythonwhois.get_whois(domain)
    domainExpirationDate = q['expiration_date'][0]
    currentDate = datetime.datetime.now()
    leftSeconds = domainExpirationDate - currentDate

    return int(leftSeconds.days)

def check_time(leftDays,domain):
    d = 30 -leftDays
    if d == 0:
        return d
    elif d == 20:
        return d
    elif d == 10:
        return d
    elif d == 5:
        return d
    elif d == 1:
        return d
    else:
        return 255

def send_notify(domain, leftDays):
    mailFrom = 'domaincontro@demi4.com'
    mailTo = 'admi@demi4.com'

    msg = MIMEText("please check and prolong domain %s " % domain)
    msg["From"] = "domainControl@demi4.com"
    msg["To"] = "admin@demi4.com"
    msg["Subject"] = "Warning - need prolong domain %s" % domain
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())

def readDomainList(File):
    f = open(File)
    d = f.read().lower().split('\n')
    for i in d:
        leftDays = check_domain(i)
        if check_time(leftDays,i) != 255:
            send_notify(i, leftDays)

readDomainList('domains.txt')