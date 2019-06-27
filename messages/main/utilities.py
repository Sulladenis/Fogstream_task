from django.contrib.auth.models import User

def post_save_dispacher(sender, **kwargs):
    if kwargs['created']:
        admin = User.objects.get(username='admin')
        obj_msg = kwargs['instance']
        subject = obj_msg
        body = obj_msg.text
        email = obj_msg.email
        admin.email_user(subject, body)
        print('Сообщение {} созданно'.format(kwargs['instance']))