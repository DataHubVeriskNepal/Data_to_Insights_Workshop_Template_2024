from dotenv import load_dotenv
from forex_scraper import ForexScraper

def main():
    # Load environment variables
    load_dotenv()

    # Initialize a ForexScraper instance and call the run method
    scraper = ForexScraper()
    scraper.run()

if __name__ == '__main__':
    main()