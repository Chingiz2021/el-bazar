from fastapi import BackgroundTasks, APIRouter

from fastapi_crudrouter import OrmarCRUDRouter

from repositories.users import Users, CreateUsers, UpdateUsers
from fastapi_mail import  MessageSchema
from conf.mail import fm, settings


custom_router = OrmarCRUDRouter(
        schema=Users,
        update_schema=UpdateUsers,
        prefix="applications",
    )

html = """
<p>Hi this test mail, thanks for using Fastapi-mail</p> 
"""

html2 = """
<p>Hi this test mail, thanks for using Fastapi-mail</p> 
"""



@custom_router.post('')
async def create_one(appl:CreateUsers,background_tasks: BackgroundTasks,):
    new_appl = Users(name_user=appl.name_user,phone_user=appl.phone_user,email_user=appl.email_user)
    await new_appl.save()

    html2 = """
    <p>Новая заявка</p> 
    """
    message = MessageSchema(
    subject="El-Bazaar",
    recipients=[appl.email_user], 
    body=html,
    subtype="html"
    ) 

    message2 = MessageSchema(
    subject="El-Bazaar",
    recipients=[settings.mail_username], 
    body=html2,
    subtype="html"
    ) 
    background_tasks.add_task(fm.send_message,message)
    background_tasks.add_task(fm.send_message,message2)
    return new_appl

count_router = APIRouter()


@count_router.get('/appl')
async def count_all():
    return await Users.objects.count()