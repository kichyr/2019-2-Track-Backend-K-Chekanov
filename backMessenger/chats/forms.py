from django import forms
from users.models import User
from chats.models import Chat
from users.models import Member

class PostNewChatForm(forms.Form):
    topic = forms.CharField(max_length=30)

    def clean_text(self):
        users_logins = self.cleaned_data['users_logins']
        for user_login in users_logins:
            if len(User.objects.filter(login=user_login)) == 0:
                return 'login ${user_login} do not exist'
        return self.changed_data['user_logins']
    
    def save(self):
        createNewChat(self.changed_data['topic'], self.changed_data['user_logins'])



def createNewChat(topic, users_logins):
    """
    create new chat with topic
    attach to this chat list of users given by users_logins
    """
    group_chat_flag = False
    if len(users_logins) > 2:
        group_chat_flag = True

    chat = Chat.objects.create(topic=topic, is_group_chat=group_chat_flag)
    chat.save()
    for user_login in users_logins:
        user = User.objects.filter(login=user_login)[0]
        Member.objects.create(chat=chat, user=user).save()