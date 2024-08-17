# World Language Translator

## Overview

The **World Language Translator** is a Python application designed to help users translate text between languages, find the languages spoken in specific countries, and identify countries where a particular language is spoken. It features a simple command-line interface that allows easy interaction with the tool.

## Features

- **Translate Text**: Translate text from English into multiple target languages.
- **Languages by Country**: Find out which languages are spoken in a given country.
- **Countries by Language**: Discover the countries where a specific language is spoken.
- **List Available Languages and Countries**: View all supported languages and countries stored in the database.

## Project Structure

- **Abrevs.py**: Handles the mapping of language names to their abbreviations.
- **Interface.py**: The main script for user interaction, providing a menu-driven interface.
- **Tree.py**: Contains the logic for translations and language-country lookups.
- **X2D.py**: Manages the loading of language and country data from Excel files.
- **countries.py**: A dictionary that maps country codes to full country names.

## Installation

### Prerequisites

- **Python 3.x**
- **pip**: For managing Python packages

### Steps to Install

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

Upon running `Interface.py`, you will be presented with a menu where you can:

- **Find Languages by Country**: Input a country name to see its languages.
- **Find Countries by Language**: Input a language to see where it is spoken.
- **Translate Text**: Translate text from English to another language.
- **View All Available Countries**: List all countries in the database.
- **View All Available Languages**: List all languages in the database.

### Example Commands

- **Translate a Phrase**:

  ```plaintext
  Select an option: 3
  Enter text to translate: Hello
  Enter target language: Spanish
  Translation: Hola
  ```

- **Find Languages in Canada**:
  ```plaintext
  Select an option: 1
  Enter country: Canada
  Languages spoken in Canada: English, French
  ```

## Configuration

Ensure that your API keys are set correctly in the `Tree.py` file to enable translation functionality. Also, make sure the `countries.xlsx` and `languages.xlsx` files in the `data/` directory are properly formatted.
