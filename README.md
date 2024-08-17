# World Language Translator

## Introduction

The **World Language Translator** is a Python-based tool designed for easy language translation and information retrieval. Users can identify languages spoken in specific countries, find countries where a particular language is spoken, and translate text between languages.

## Features

- **Language Lookup by Country**: Find out which languages are spoken in a given country.
- **Country Lookup by Language**: Discover the countries where a specific language is spoken.
- **Text Translation**: Translate phrases from English to a target language.
- **View All Available Countries and Languages**: List all countries and languages stored in the database.

## Installation

### Prerequisites

- Python 3.x
- pip for managing Python packages

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/YourUsername/world-language-translator.git
   cd world-language-translator
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python Interface.py
   ```

## Usage

Upon running the program, follow the menu prompts:

- **Find Languages by Country**: Input a country name to see its languages.
- **Find Countries by Language**: Input a language to see where it is spoken.
- **Translate Text**: Translate text from English to another language.
- **View Lists**: Display all available countries or languages.

### Example

- **Translate "Hello" to Spanish**:
  ```plaintext
  Select an option: 3
  Enter text to translate: Hello
  Enter target language: Spanish
  Translation: Hola
  ```
