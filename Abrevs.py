# Class to map language names to their abbreviations
class Abrevs:
    def __init__(self):
        self.language_map = {
            'English': 'en',
            'Spanish': 'es',
            'French': 'fr',
            'German': 'de',
            'Italian': 'it',
            'Portuguese': 'pt',
            'Russian': 'ru',
            'Chinese': 'zh',
            'Japanese': 'ja',
            'Korean': 'ko',
            'Arabic': 'ar',
            'Hindi': 'hi',
            'Bengali': 'bn',
            'Turkish': 'tr',
            'Dutch': 'nl',
            'Greek': 'el',
            'Swedish': 'sv',
            'Norwegian': 'no',
            'Danish': 'da',
            'Finnish': 'fi',
            'Polish': 'pl',
            'Hungarian': 'hu',
            'Czech': 'cs',
            'Romanian': 'ro',
            'Hebrew': 'he',
            'Vietnamese': 'vi',
            'Thai': 'th',
            'Indonesian': 'id',
            'Malay': 'ms',
        }

    def get_abbreviation(self, language_name):
        return self.language_map.get(language_name, None)
