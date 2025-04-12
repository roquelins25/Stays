# Stays API Integration

This project provides an integration with the Stays platform API to export reservation data.

## Project Structure
```
Stays/
├── src/
│   └── reservations.py    # Main script for API integration
├── .env                   # Environment variables (not tracked in git)
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore rules
```

## Features
- Fetches reservation data from Stays platform
- Uses environment variables for secure authentication
- Exports data for specific date ranges
- Returns data in JSON format

## Prerequisites
- Python 3.x
- Virtual environment (recommended)

## Installation

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # For Windows PowerShell
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root
2. Add your authentication credentials:
   ```
   loginsenha=your_base64_encoded_credentials
   ```

## Usage

The script exports reservation data for a specified date range. By default, it fetches data from December 10, 2024, to December 12, 2024.

To run the script:
```bash
python src/reservations.py
```

## Dependencies
- requests==2.32.3
- python-dotenv==1.1.0
- certifi==2025.1.31
- charset-normalizer==3.4.1
- idna==3.10
- urllib3==2.4.0

## Security Notes
- Never commit your `.env` file
- Keep your authentication credentials secure
- Use environment variables for sensitive data

## API Documentation
The script uses the Stays API endpoint:
- Base URL: https://lit.stays.com.br
- Endpoint: /external/v1/booking/reservations-export
- Method: POST
- Authentication: Basic Auth
