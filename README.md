# Book-Recommendation-System

## Description
This project is a Book Recommendation System built using Python and the Tkinter library. It allows users to search for books, view their details, and display book covers using the Google Books API. The interface provides options to display additional information such as the publication date and average rating of the books.

## Features
- **Search for Books:** Users can search for books using the Google Books API.
- **Display Book Details:** The system fetches and displays book titles, covers, publication dates, and ratings.
- **Interactive UI:** The graphical user interface is created using Tkinter, providing a user-friendly experience.
- **Settings Menu:** Users can choose to display or hide publication dates and ratings.

## Prerequisites
- Python 3.x
- Virtualenv

## Installation

1. **Create a virtual environment:**
   ```sh
   pip install virtualenv
   virtualenv book
2. **Activate the virtual environment:**
   
     **On Windows:**
   
       .\book\Scripts\activate
   
     **On macOS/Linux:**
   
       source book/bin/activate
       
3. **Install required packages:**
   
  pip install pillow
  
  pip install requests

## Dependencies
  - Pillow: 10.3.0
  - Requests: 2.32.2
  - certifi: 2024.2.2
  - charset-normalizer: 3.3.2
  - idna: 3.7
  - urllib3: 2.2.1

## Project Structure
main.py: The main script containing the code for the Book Recommendation System.
images folder: Contains images used in the application (icon, background, logo, etc.).

## Usage
python main.py

