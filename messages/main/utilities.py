from django.contrib.auth.models import User
import json
from urllib.request import urlopen


def post_save_dispacher(sender, **kwargs):
    """This function sends an email with message text and api data"""
    if kwargs['created']:
        admin = User.objects.get(username='admin')
        obj_msg = kwargs['instance']
        email = obj_msg.email
        body = "Вам отправленно сообщение:\n" + obj_msg.text + "\n\nДанные пользователя:\n" + get_user_data(email)
        try:
            admin.email_user(obj_msg, body)
            obj_msg.sent_email = True
            obj_msg.save()
        except:
            print("Письмо не отправленно")

def get_user_data(email):
    """This function receives data from api"""
    url = "http://jsonplaceholder.typicode.com/users?email="
    user_data = ""
    try:
        with urlopen(url+email) as response:
            source = response.read()
    except:
        return "Информация не доступна"
    try:
        data = json.loads(source)
        for key in data[0].keys():
            if type(data[0][key]) == dict:
                user_data = user_data + "{}:\n".format(key) 
                for k in data[0][key].keys():
                    user_data = user_data + "    {}: {} \n".format(k, data[0][key][k])            
            else:
                user_data = user_data + "{}: {} \n".format(key, data[0][key])
    except:
        user_data = "Пользователя нет в БД"
    return user_data





 


