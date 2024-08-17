import requests
from Abrevs import Abrevs
from X2D import X2D
from translate import Translator

class Tree:
    def __init__(self):
        self.abrevs = Abrevs()
        self.data_manager = X2D()
        # Load data from the Excel files
        self.data_manager.load_data('data/countries.xlsx', 'data/languages.xlsx')
        self.endpoint = 'https://libretranslate.com/translate'  # Translation API endpoint

        # Mapping of country codes to full country names
        self.country_codes = {
            'US': 'United States',
            'CA': 'Canada',
            'GB': 'United Kingdom',
            'FR': 'France',
            'DE': 'Germany',
            'IT': 'Italy',
            'ES': 'Spain',
            'RU': 'Russia',
            'CN': 'China',
            'JP': 'Japan',
            'KR': 'South Korea',
            'IN': 'India',
            'BR': 'Brazil',
            'MX': 'Mexico',
            'ZA': 'South Africa',
            'AU': 'Australia',
            'NZ': 'New Zealand',
            'AR': 'Argentina',
            'CL': 'Chile',
            'CO': 'Colombia',
            'SE': 'Sweden',
            'NO': 'Norway',
            'DK': 'Denmark',
            'FI': 'Finland',
            'NL': 'Netherlands',
            'BE': 'Belgium',
            'PT': 'Portugal',
            'GR': 'Greece',
            'PL': 'Poland',
            'HU': 'Hungary',
            'RO': 'Romania',
            'IL': 'Israel',
            'TR': 'Turkey',
            'EG': 'Egypt',
            'SA': 'Saudi Arabia',
            'VN': 'Vietnam',
            'TH': 'Thailand',
            'ID': 'Indonesia',
            'MY': 'Malaysia',
            'SG': 'Singapore',
            'PH': 'Philippines',
            'AE': 'United Arab Emirates',
        }

    def translate(self, text, target_language):
        # Get the language code from the abbreviation class
        lang_code = self.abrevs.get_abbreviation(target_language)
        if not lang_code:
            return "Language not supported"

        # Use the Translator library for translation
        translator = Translator(to_lang=lang_code)
        
        try:
            translation = translator.translate(text)
            return translation
        except Exception as e:
            return f"Error: {str(e)}"

    def find_languages_by_country(self, country_code_or_name):
        # Convert country code to full country name if necessary
        country = self.country_codes.get(country_code_or_name, country_code_or_name)
        languages = self.data_manager.languages_by_country.get(country)
        
        if not languages:
            return f"No languages found for {country}."
        return languages

    def find_countries_by_language(self, language):
        # Get the language code, or use the full language name if not available
        lang_code = self.abrevs.get_abbreviation(language) or language
        countries = self.data_manager.countries_by_language.get(lang_code)

        if not countries:
            countries = self.data_manager.countries_by_language.get(language)

        if not countries:
            return []
        
        return countries
