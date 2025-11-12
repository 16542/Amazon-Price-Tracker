# Amazon Price Tracker

A Python-based web scraper that monitors Amazon product prices and sends email notifications when the price drops below a specified threshold.

## Features

- 🔍 Scrapes product prices from Amazon product pages
- 📧 Sends email notifications when price drops below target
- 🔐 Secure credential management using environment variables
- 🌐 Handles Amazon's anti-bot measures with proper headers

## Prerequisites

- Python 3.7 or higher
- A Gmail account (or other SMTP email service)
- An app-specific password for your email account

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Amazon-price-tracker.git
cd Amazon-price-tracker
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. Install required dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root directory with the following variables:
```env
SMTP_SERVER=smtp.gmail.com
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password
RECIPIENT_EMAIL=recipient_email@gmail.com
```

## Configuration

### Setting up Email Notifications

1. **For Gmail users:**
   - Enable 2-factor authentication on your Google account
   - Generate an app-specific password: [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Use this app password in your `.env` file

2. **For other email providers:**
   - Update the `SMTP_SERVER` in your `.env` file
   - Adjust the port number in `main.py` if necessary (default is 587)

### Customizing the Product and Price Threshold

Edit `main.py` to customize:

- **Product URL:** Replace the URL in the `requests.get()` call with your desired Amazon product
- **Price Threshold:** Modify the condition `if(price<=70.99):` to your target price

## Usage

Run the script:
```bash
python main.py
```

The script will:
1. Scrape the current price from the specified Amazon product page
2. Compare it against your target price
3. Send an email notification if the price is below the threshold

### Automating Price Checks

To run the script periodically:

- **Windows:** Use Task Scheduler
- **macOS/Linux:** Use cron jobs
- **Cloud:** Deploy to services like Heroku, AWS Lambda, or PythonAnywhere

Example cron job (checks every hour):
```bash
0 * * * * /path/to/python /path/to/main.py
```

## Dependencies

- `beautifulsoup4` - Web scraping library
- `requests` - HTTP library for making requests
- `python-dotenv` - Environment variable management

## Important Notes

⚠️ **Web Scraping Disclaimer:**
- Web scraping may violate Amazon's Terms of Service
- This project is for educational purposes only
- Use responsibly and at your own risk
- Amazon's HTML structure may change, requiring updates to the scraper

⚠️ **Security:**
- Never commit your `.env` file to version control
- Keep your email credentials secure
- Use app-specific passwords, not your main account password

## Troubleshooting

- **No price found:** Amazon's HTML structure may have changed. Inspect the page and update the class names in `main.py`
- **Email not sending:** Verify your SMTP settings and app password
- **Request blocked:** Amazon may be blocking your requests. Try using different user agents or adding delays between requests

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created by Ahmed Ben Kahla

## Acknowledgments

- Built with Python, BeautifulSoup, and Requests
- Inspired by the need to catch good deals on Amazon
