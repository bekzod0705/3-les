from modeltranslation.translator import translator, TranslationOptions
from polls.models import TeacherModel

class TeacherTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('uz',)
translator.register(TeacherModel, TeacherTranslationOptions)