# Forex Data and Gold Silver Price Scraper

This project is a Forex data and gold-silver price scraper designed to extract currency exchange rates and precious metal prices from specified websites. It organizes the data into monthly CSV files and uploads them to an AWS S3 bucket. By processing and uploading each month's data separately, the scraper provides an efficient solution for collecting, organizing, and storing data for visualization and analytics.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Details](#project-details)

## Project Overview

The Scraper performs the following tasks:

1. Scrapes currency exchange rates and gold silver prices from specified websites.
2. Parses the data and organizes it into CSV files by month.
3. Uploads the CSV files to an AWS S3 bucket, one for each month after the data for that month is processed.

## Project Structure

```plaintext
Scraping/
├── .main.py
├── forex_scraper.py
├── gold_silver_scraper.py
├── utils/
│   ├── csv_handler.py
│   └── s3_uploader.py
├── forex/
│   └── (generated CSV files)
├── gold_silver/
│   └── (generated CSV files)
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

Before running this project, make sure you have the following:

- **Python 3.8+**: Ensure Python is installed on your system. If you're using WSL on Windows, use the following commands:
    ```bash
    sudo apt update
    sudo apt install python3
    ```
- **AWS account**: An AWS account with an S3 bucket to upload the data files (We'll provide at the venue).
- **pip**: Ensure that `pip` (Python package manager) is installed. You can install it using:
    ```bash
    sudo apt install python3-pip
    ```

## Installation

Follow these steps to install and set up the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DataHubVeriskNepal/Data_to_Insights_Workshop_Template_2024.git
    ```

2. **Set up virtual environment**:
    - If `venv` is not installed (Not necessary with recent python versions):
      ```bash
      sudo apt install python3-venv
      ```
    - Create and activate the virtual environment:
      ```bash
      cd Scraping
      python -m venv venv (Or python3 -m venv venv)
      source venv/bin/activate   # Linux/Mac
      venv\Scripts\activate      # Windows
      ```

3. **Install required dependencies**:
    ```bash
    cd Scraping
    pip install -r requirements.txt
    ```

## Setup

Before running the scraper, follow these setup steps:

1. **Configure AWS credentials**:
    - Create an AWS account if you don’t have one.
    - Set up an S3 bucket where the CSV files will be uploaded.

2. **Create a `.env` file**:
    - In the project root, create a `.env` file:
      ```bash
      touch .env
      ```
    - Add your AWS credentials and S3 bucket name to the `.env` file:
      ```env
      AWS_ACCESS_KEY_ID=your-access-key
      AWS_SECRET_ACCESS_KEY=your-secret-key
      S3_BUCKET_NAME=your-bucket-name
      ```

## Usage

Once the setup and development is complete, you can run the scraper as follows:

1. **Run the script**:
    ```bash
    python main.py
    ```

2. **Expected behavior**:
    - The scraper will download forex data and gold silver prices from the respective websites.
    - It will save each month’s data in a separate CSV file under the `forex/` and `gold_silver` directories.
    - Each CSV file will be uploaded to the specified S3 bucket after its data is fully written.

## Configuration

The project is configured using environment variables stored in the `.env` file:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
- `S3_BUCKET_NAME`: The name of the S3 bucket where CSV files will be uploaded.

To set these variables, make sure your `.env` file is properly configured.

## Project Details

### Scraper Functionality

- **Web Scraping**: The project uses `requests` and `BeautifulSoup` to scrape forex exchange rates from a website.
- **Data Extraction**: The scraped data is parsed into a structured format and stored as CSV files. The files are named by month and stored locally in the `forex/` directory.
- **AWS S3 Integration**: Using `boto3`, the project uploads each monthly CSV file to an S3 bucket after it finishes processing that month’s data.
