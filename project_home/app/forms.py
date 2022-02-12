from django import forms
class loginsform(forms.Form):
    wd_user =  forms.TextInput(attrs={ "class": "input1", "rows": 1, "placeholder": "username" })
    wd_pass = forms.PasswordInput(attrs={ "class": "input1", "rows": 1, "placeholder": "password"})
    username = forms.CharField( label="", widget = wd_user)
    passwd = forms.CharField(label="", widget = wd_pass,max_length=12)
    
    def clean_passwd(self, *args, **kwargs):
        passwd = self.cleaned_data.get("passwd")
        if (len(passwd) < 8 ):
            raise forms.ValidationError("length must be greater than 8")
        return passwd
   