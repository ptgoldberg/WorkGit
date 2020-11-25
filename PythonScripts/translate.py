import boto3

translate = boto3.client(service_name='translate', region_name='us-west-2', use_ssl=True)

languageDict = {'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca', 'Chinese (Simplified)': 'zh', 'Chinese (Traditional)': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dari': 'fa-AF', 'Dutch': 'nl', 'English': 'en', 'Estonian': 'et', 'Farsi (Persian)': 'fa', 'Filipino Tagalog': 'tl', 'Finnish': 'fi', 'French': 'fr', 'French (Canada)': 'fr-CA', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hebrew': 'he', 'Hindi': 'hi', 'Hungarian': 'hu', 'Icelandic': 'is', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kannada': 'kn', 'Kazakh': 'kk', 'Korean': 'ko', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Macedonian': 'mk', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Mongolian': 'mn', 'Norwegian': 'no', 'Persian': 'fa', 'Pashto': 'ps', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru', 'Serbian': 'sr', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali':
'so', 'Spanish': 'es', 'Spanish (Mexico)': 'es-MX', 'Swahili': 'sw', 'Swedish': 'sv', 'Tagalog': 'tl', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy'}

textInput = input('Translate: ')
textInputLang = "en"
textOutputLang = input('Language Output: ')
try: 
    result = translate.translate_text(Text=textInput, 
                SourceLanguageCode=textInputLang, TargetLanguageCode=textOutputLang)
    print('TranslatedText: ' + result.get('TranslatedText'))
    print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
    print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
except: 
    print('There was an error, please try again!')
