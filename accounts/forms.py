from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        #this use the default UserCreationForm and add extra
        fields = UserCreationForm.Meta.fields + ('age','email')
        # or use this trick but then we have to control or add our own field
        # fields = (
        #     "username",
        #     "email",
        #     "age",
        #     ) 
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields