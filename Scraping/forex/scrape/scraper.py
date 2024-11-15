import requests
import re
from bs4 import BeautifulSoup
from csv_handler import CSVHandler
from s3_uploader import S3Uploader

class ForexScraper:
    def __init__(self):
        ##
        # STEP 1:
        # 	Initialize necessary instance variables
        #
        """CODE BLOCK STARTS"""


        """CODE BLOCK ENDS"""

    def run(self):
        try:
            ##
            # STEP 2:
            #   Send a get request to the landing page
            #   Fetch the base URL
            #
            """CODE BLOCK STARTS"""



            # print('Successfully fetched the landing page!')
            """CODE BLOCK ENDS"""

            ##
            # STEP 3:
            #   Make a call to parse_links method and go forward to define it
            #
            #   NOTE: Ensure to call close_and_upload_csv_handler
            # 
            """CODE BLOCK STARTS"""


            """CODE BLOCK ENDS"""
        except requests.exceptions.RequestException as e:
            print(f'Error fetching the landing page: {e}')

    def parse_links(self, html_content):
        try:
            ##
            # STEP 4:
            #   1. Look for buttons with text `View Rates`
            #   2. Loop into those links and extract the value of href attribute
            #   3. Append href with base URL
            #   4. Extract date from the full URL (will discuss why? later)
            #   5. Make a call to handle_month_transition method (We'll come back to this part later; 
            #                                                     follow on to step 6 of this section for now)
            #   6. Navigate to these full URLs (fetch_rates_page)
            # 

            """CODE BLOCK STARTS"""


            """CODE BLOCK ENDS"""
        except Exception as e:
            print(f'Error parsing links: {e}')

    def handle_month_transition(self, date):
        """Check if the month has changed and handle file closing and opening accordingly"""
        ##
        # STEP 7
        #   1. Extract new month('YYYY-MM') from the date
        #   2. Initialize first month if the current month is not available
        #   3. Check if the current month equal to the new month. If the month has changed:
        #       a. Close the current csv file and upload to s3 using close_and_upload_csv_handler
        #       b. Set the current month equal to the extracted new month
        #
        """CODE BLOCK STARTS"""
        new_month = date[:7]  # Extract 'YYYY-MM' from the date

        if self.current_month is None:
            self.current_month = new_month  # First month initialization
        elif self.current_month != new_month:
            # If the month has changed, close and upload the previous month's file
            print(f"Transitioning to new month: {new_month}, closing previous month: {self.current_month}")
            self.close_and_upload_csv_handler()
            self.current_month = new_month  # Update the current month to the new month
        """CODE BLOCK ENDS"""

    def close_and_upload_csv_handler(self):
        """Close the current CSV handler and upload the file to S3 if open."""
        if self.csv_handler:
            self.csv_handler.close(self.s3_uploader)
            self.csv_handler = None  # Reset the handler after uploading

    # def fetch_rates_page(self, full_url, date):
    #     try:
            ##
            # STEP 5: (Similar to step 1)
            #   1. Fetch rates page by a sending a get request
            #   2. Make a call to extract_data method for data extraction
            #
            # """CODE BLOCK STARTS"""


			# """CODE BLOCK ENDS"""

        # except requests.exceptions.RequestException as e:
        #     print(f'Error fetching the View Rates page at {full_url}: {e}')

    # def extract_data(self, html_content, date):
    #     try:
            ##
            # STEP 6:
            #   1. Locate and find the table tag
            #   2. Extract data from the table and write to a csv file using the csv handler
            #
            # Side Note: 
			# 	Snippet for data extraction from each table row: 
			# 		row_data = [col.text.strip() for i, col in enumerate(columns) if i != 1]
			#				OR
            #		row_data = []
			#		for i, col in enumerate(columns):
			#		 	if i != 1:
			#		 		row_data.append(col.text.strip())
            #
			# """CODE BLOCK STARTS"""


			# """CODE BLOCK ENDS"""
        # except Exception as e:
        #     print(f'Error extracting data: {e}')
