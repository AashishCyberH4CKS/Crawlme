<img width="1094" height="686" alt="image" src="https://github.com/user-attachments/assets/02524998-28c1-4ba5-a698-0879b6c059f7" />


# 🕷️ Web Crawler Tool

A powerful, **ethical web crawler tool** designed for educational purposes to extract emails, phone numbers, and links from websites.

![Python](https://img.shields.io/badge/Python-3.6%252B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Purpose](https://img.shields.io/badge/Purpose-Educational%2520Only-yellow)

---

## 🌟 Features

- **Email Extraction**: Automatically finds and extracts email addresses  
- **Phone Number Detection**: Identifies various phone number formats  
- **Link Discovery**: Collects both internal and external links  
- **Robots.txt Compliance**: Respects website crawling policies  
- **Multi-threaded Crawling**: Efficient parallel processing  
- **Ethical Design**: Built with respectful crawling delays and proper user-agent identification  
- **Detailed Reports**: Generates comprehensive text reports with timestamps  
- **Hacker-themed UI**: Beautiful golden banner with animations and emojis  

---

## 🚀 Quick Start

### Installation

Clone or download the repository, then install the required dependencies:

```bash
**pip install -r requirements.txt

Usage

Run the crawler:

python web_crawler.py

Enter the target website URL when prompted:

💻 Enter the website/URL you want to crawl (or 'quit' to exit): https://example.com

---

##  📋 Requirements

    Python 3.6+
    Required packages:

        requests==2.31.0
        beautifulsoup4==4.12.2
        lxml==4.9.3
        urllib3==2.0.4

##   🛠️ How It Works

    URL Processing – The crawler starts with a seed URL and processes pages systematically
    Content Analysis – Each page is analyzed for emails, phone numbers, and links
    Respectful Crawling – Implements delays between requests and follows robots.txt rules
    Data Extraction – Uses regex patterns to identify contact information
    Report Generation – Creates detailed timestamped reports in text format

##   📊 Output

The tool generates comprehensive reports with:
    Crawl date and time
    Number of pages crawled
    All discovered email addresses
    All discovered phone numbers
    Internal and external links
    Complete list of crawled URLs
Sample output filename:
crawl_report_1_20231025_143022.txt

 ##  ⚠️ Important Notes

    This tool is for educational purposes only

    Always obtain proper authorization before crawling any website

    Respect website terms of service and robots.txt directives

    Implement crawling delays to avoid overwhelming servers

    The creator is not responsible for misuse of this tool

🔧 Technical Details
Core Components

    URL Frontier/Scheduler – Manages the queue of URLs to crawl

    HTTP Client – Handles web requests with proper headers and timeouts

    HTML Parser – Extracts content using BeautifulSoup

    Data Extractors – Regex patterns for emails and phone numbers

    Deduplication – Ensures URLs are not processed multiple times

Ethical Features

    Respects robots.txt directives

    Configurable delay between requests

    Proper user-agent identification

    Rate limiting to prevent server overload

📝 License

This project is licensed under the MIT License – see the LICENSE

file for details.
👨‍💻 Creator

AashishCyberH4CKS – Security Researcher & Developer
🆘 Support

If you encounter any issues or have questions:**

    Check that all dependencies are properly installed

    Ensure you're using a supported Python version (3.6+)

    Verify that the target website is accessible and allows crawling


    ⚡ Remember: With great power comes great responsibility. Always use this tool ethically and legally. 🛡️
