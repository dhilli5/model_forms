from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
    
    
class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name','url']   
        #exclude=['url']
        widgets={'name':forms.PasswordInput,'url':forms.Textarea,"email":forms.PasswordInput}    
        #abels={"topic_name":'TN'}
        #help_texts={"name":'name must be Uppercase,Lowercase,Special_Character,numbers '}
        
        
class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
        #fields=['name','author']
        #exclude=['author']
        widgets={'name':forms.PasswordInput}
       # labels={"author":'AUTHOR'}
        help_texts={"date":"must should contains the lowercase,uppercase,numbers"}