
# sends an email to intended recipient from a given email account with the option of sending an email to the sender as well
def send_email(from_email, to, email_content, subject='Hi', cc=None, email_format='text', logger=logger):
    '''
    :from_email - str
    :to - list
    :email_content - text or html
    :cc - list
    :email_format - text or html
    '''
    
    logger.debug('Entering with parameters:[from_email:%s, to:%s, subject:%s ]' % (from_email, to, subject))
    
    email_content = MIMEText(email_content, email_format)
    
    msg = MIMEMultipart('alternative')

    if cc:
        rcpt = cc + to
        msg['Cc'] = ','.join(cc)
        logger.info("Email/fax sent a cc to:%s" % (cc))
    else:
        rcpt = to

    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ','.join(to)

    msg.attach(email_content)
    logger.debug('Establishing a connection to the email server')
    server = smtplib.SMTP(settings.EMAIL_SERVER)
    logger.debug('Established a connection to the email server')
    logger.debug('Attempting to send an email')
    server.sendmail(from_email, rcpt, msg.as_string())
    logger.info('Email attempt was made')
    logger.debug('Leaving')
    return True
