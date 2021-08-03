import smtplib
from fastapi import BackgroundTasks, APIRouter
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi_crudrouter import OrmarCRUDRouter


from repositories.users import Users, CreateUsers, UpdateUsers
from conf.mail import  settings



custom_router = OrmarCRUDRouter(
    schema=Users,
    update_schema=UpdateUsers,
    prefix="/api/v1/applications",

)





def send_message_mail(email,message):
    you = email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "El-Bazaar"
    msg['From'] = settings.mail_username
    msg['To'] = you
    part2 = MIMEText(message, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.mail.ru', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(settings.mail_username, settings.mail_password)
    mail.sendmail(settings.mail_username, email, msg.as_string())
    mail.quit()




@custom_router.post('')
async def create_one(appl: CreateUsers, background_tasks: BackgroundTasks,):
    new_appl = Users(name_user=appl.name_user,
                     phone_user=appl.phone_user, email_user=appl.email_user)
    await new_appl.save()
    style = """
    * {
                margin: 0;
                padding: 0;
                font-size: 100%;
                font-family: 'Avenir Next', "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
                line-height: 1.65; }

                img {
                max-width: 100%;
                margin: 0 auto;
                display: block; }

                body,
                .body-wrap {
                width: 100% !important;
                height: 100%;
                background: #efefef;
                -webkit-font-smoothing: antialiased;
                -webkit-text-size-adjust: none; }

                a {
                color: #71bc37;
                text-decoration: none; }

                .text-center {
                text-align: center; }

                .text-right {
                text-align: right; }

                .text-left {
                text-align: left; }

                .button {
                display: inline-block;
                color: white;
                background: #71bc37;
                border: solid #71bc37;
                border-width: 10px 20px 8px;
                font-weight: bold;
                border-radius: 4px; }

                h1, h2, h3, h4, h5, h6 {
                margin-bottom: 20px;
                line-height: 1.25; }

                h1 {
                font-size: 32px; }

                h2 {
                font-size: 28px; }

                h3 {
                font-size: 24px; }

                h4 {
                font-size: 20px; }

                h5 {
                font-size: 16px; }

                p, ul, ol {
                font-size: 16px;
                font-weight: normal;
                margin-bottom: 20px; }

                .container {
                display: block !important;
                clear: both !important;
                margin: 0 auto !important;
                max-width: 580px !important; }
                .container table {
                    width: 100% !important;
                    border-collapse: collapse; }
                .container .masthead {
                    padding: 80px 0;
                    background: #71bc37;
                    color: white; }
                    .container .masthead h1 {
                    margin: 0 auto !important;
                    max-width: 90%;
                    text-transform: uppercase; }
                .container .content {
                    background: white;
                    padding: 30px 35px; }
                    .container .content.footer {
                    background: none; }
                    .container .content.footer p {
                        margin-bottom: 0;
                        color: #888;
                        text-align: center;
                        font-size: 14px; }
                    .container .content.footer a {
                        color: #888;
                        text-decoration: none;
                        font-weight: bold; }
        """
    html = '''\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width"/>
        <style type="text/css">
        {style}
        </style>
    </head>
    <body>
    <table class="body-wrap">
        <tr>
            <td class="container">
                <table>
                    <tr>
                        <td align="center" class="masthead">
                            <h1>{appl.name_user} <br> Поздравляем!</h1>
                            <p>Вы успешно зарегестрированы!</p>
                        </td>
                    </tr>
                    <tr>
                        <td class="content">
                            <h2>Добро пожаловать в сервис El-Bazaar,</h2>
                            <p>Вы успешно зарегестрировались и вскоре мы с вами свяжемся.</p>
                            <p>Перейти на сайт <a href="https://el-bazaar.kz">El-Bazaar</a>.</p>
                            <p><em>– El-Bazaar</em></p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td class="container">
                <table>
                    <tr>
                        <td class="content footer" align="center">
                            <p>Sent by <a href="https://el-bazaar.kz">El-Bazaar</a>, Казахстан,</p>
                            
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    </body>
    </html>
    '''.format(**locals())
    html2 = '''\
    <p>Новая заявка на сайте </p> 
    <p>Имя пользователя: {appl.name_user} </p>
    <p>Телефон пользователя:{appl.phone_user} </p>
    <p>Email пользователя:{appl.email_user} </p>
    <p>Перейти на сайт <a href="https://el-bazaar.kz">El-Bazaar</a>.</p>
    '''.format(**locals())
    background_tasks.add_task(send_message_mail,appl.email_user,html)
    background_tasks.add_task(send_message_mail,settings.mail_username,html2)
    return new_appl


count_router = APIRouter(
    prefix="/api/v1/appl",
    tags=["appl"],
)

@count_router.get('/')
async def count_all():
    return await Users.objects.count()
