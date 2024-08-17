from Tree import Tree

def main():
    tree = Tree()
    
    # Welcome Message
    print("\n" + "="*50)
    print(" WELCOME TO THE WORLD LANGUAGE TRANSLATOR")
    print("="*50 + "\n")
    
    while True:
        print("\n" + "-"*50)
        print(" MAIN MENU")
        print("-"*50)
        print("1: Find languages spoken in a country")
        print("2: Find countries where a language is spoken")
        print("3: Translate text")
        print("4: List all available countries")
        print("5: List all available languages")
        print("6: Exit")
        print("-"*50)
        
        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            country = input("Enter country (e.g., United States): ").strip()
            languages = tree.find_languages_by_country(country)
            if languages:
                print(f"\nLanguages spoken in {country}: {', '.join(languages)}")
            else:
                print(f"\nNo languages found for {country}.")
        elif choice == '2':
            language = input("Enter language (e.g., English): ").strip()
            countries = tree.find_countries_by_language(language)
            if countries:
                print(f"\nCountries where {language} is spoken: {', '.join(countries)}")
            else:
                print(f"\nNo countries found where {language} is spoken.")
        elif choice == '3':
            text = input("Enter text to translate (e.g., Hello): ").strip()
            language = input("Enter target language (e.g., Spanish): ").strip()
            translation = tree.translate(text, language)
            print(f"\nTranslation: {translation}")
        elif choice == '4':
            print("\nAvailable countries:")
            for country in tree.data_manager.languages_by_country.keys():
                print(f" - {country}")
        elif choice == '5':
            print("\nAvailable languages:")
            for language in tree.data_manager.countries_by_language.keys():
                print(f" - {language}")
        elif choice == '6':
            print("\nThank you for using the World Language Translator. Goodbye!")
            break
        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()
