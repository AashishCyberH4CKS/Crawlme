import requests
import re
import time
import threading
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse
from collections import deque
import os
from datetime import datetime
from bs4 import BeautifulSoup
import sys
from time import sleep

# Initialize color codes for terminal
class Colors:
    GOLD = '\033[38;5;214m'
    ORANGE = '\033[38;5;208m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

def animate_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = f"""{Colors.GOLD}
    ░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░██╗  ███╗░░░███╗███████╗
    ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░╚█║  ████╗░████║██╔════╝
    ██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░░╚╝  ██╔████╔██║█████╗░░
    ██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░░░░  ██║╚██╔╝██║██╔══╝░░
    ╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗░░░  ██║░╚═╝░██║███████╗
    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝░░░  ╚═╝░░░░░╚═╝╚══════╝
    {Colors.END}"""
    
    print(banner)
    
    # Animated creator text
    creator_text = f"{Colors.GOLD}{Colors.BOLD}           Created By AashishCyberH4CKS | Version 1.0 {Colors.END}🔥👨‍💻🔒"
    animate_text(creator_text, 0.05)
    
    print(f"\n{Colors.ORANGE}{'='*70}{Colors.END}")
    print(f"{Colors.RED}🚀 WELCOME TO THE ULTIMATE WEB CRAWLER TOOL {Colors.GREEN}⚡{Colors.END}")
    print(f"{Colors.RED}🔐 For Educational & Ethical Use Only {Colors.GREEN}✅{Colors.END}")
    print(f"{Colors.ORANGE}{'='*70}{Colors.END}\n")

class EducationalWebCrawler:
    def __init__(self):
        self.visited_urls = set()
        self.to_crawl = deque()
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.phone_pattern = r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{2,4}[-.\s]?\d{3,5}\b'
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'EducationalWebCrawler/1.0 (Educational Research; +http://example.com/bot.html)'
        })
        self.delay = 1  # Default delay between requests
        self.max_threads = 5
        self.found_emails = set()
        self.found_phones = set()
        self.found_links = set()
        self.found_external_links = set()
        self.domain = ""
        self.robots_parser = None
        self.crawl_count = 0
        
    def is_allowed_by_robots(self, url):
        try:
            return self.robots_parser.can_fetch(self.session.headers['User-Agent'], url)
        except:
            return False
            
    def get_robots_txt(self, base_url):
        robots_url = urljoin(base_url, '/robots.txt')
        self.robots_parser = RobotFileParser()
        try:
            self.robots_parser.set_url(robots_url)
            self.robots_parser.read()
            crawl_delay = self.robots_parser.crawl_delay(self.session.headers['User-Agent'])
            if crawl_delay:
                self.delay = max(self.delay, crawl_delay)
            print(f"{Colors.GREEN}✅ robots.txt found and parsed{Colors.END}")
        except:
            print(f"{Colors.YELLOW}⚠️ No robots.txt found or couldn't be parsed. Proceeding with default settings.{Colors.END}")
            
    def extract_emails(self, text):
        return re.findall(self.email_pattern, text)
        
    def extract_phones(self, text):
        return re.findall(self.phone_pattern, text)
        
    def extract_links(self, soup, base_url):
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(base_url, href)
            links.add(full_url)
        return links
        
    def is_same_domain(self, url):
        return urlparse(url).netloc == self.domain
        
    def crawl_page(self, url):
        if url in self.visited_urls:
            return
            
        if not self.is_allowed_by_robots(url):
            print(f"{Colors.YELLOW}🚫 Blocked by robots.txt: {url}{Colors.END}")
            return
            
        try:
            time.sleep(self.delay)  # Respectful crawling
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Add to visited URLs
            self.visited_urls.add(url)
            
            # Parse the content
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = soup.get_text()
            
            # Extract data
            emails = self.extract_emails(text_content)
            phones = self.extract_phones(text_content)
            links = self.extract_links(soup, url)
            
            # Update found data
            self.found_emails.update(emails)
            self.found_phones.update(phones)
            self.found_links.update(links)
            
            # Add new links to the queue if they're from the same domain
            for link in links:
                if link not in self.visited_urls and link not in self.to_crawl:
                    if self.is_same_domain(link):
                        self.to_crawl.append(link)
                    else:
                        self.found_external_links.add(link)
                        
            print(f"{Colors.CYAN}🌐 Crawled: {url} {Colors.GREEN}| Found: {len(emails)} emails, {len(phones)} phones, {len(links)} links{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}❌ Error crawling {url}: {str(e)}{Colors.END}")
            
    def start_crawling(self, start_url, max_pages=50):
        print(f"\n{Colors.GREEN}🚀 Starting crawl of {start_url}{Colors.END}")
        print(f"{Colors.YELLOW}⏳ This may take a while depending on the site size...{Colors.END}\n")
        
        # Reset state for new crawl
        self.visited_urls.clear()
        self.to_crawl.clear()
        self.found_emails.clear()
        self.found_phones.clear()
        self.found_links.clear()
        self.found_external_links.clear()
        
        # Set domain and get robots.txt
        parsed_url = urlparse(start_url)
        self.domain = parsed_url.netloc
        self.get_robots_txt(start_url)
        
        # Add start URL to the queue
        self.to_crawl.append(start_url)
        
        # Start crawling with multiple threads
        threads = []
        pages_crawled = 0
        
        # Simple progress indicator (replacing tqdm)
        print(f"{Colors.PURPLE}[{Colors.END}", end="", flush=True)
        
        while self.to_crawl and pages_crawled < max_pages:
            # Start new threads if we have URLs to crawl and thread limit not reached
            while self.to_crawl and len(threads) < self.max_threads and pages_crawled < max_pages:
                url = self.to_crawl.popleft()
                thread = threading.Thread(target=self.crawl_page, args=(url,))
                thread.start()
                threads.append(thread)
                pages_crawled += 1
                
                # Update progress indicator
                if pages_crawled % 5 == 0:
                    print(f"{Colors.PURPLE}▓{Colors.END}", end="", flush=True)
                    
            # Remove finished threads
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)
                    
            time.sleep(0.1)
            
        # Wait for all threads to finish
        for thread in threads:
            thread.join()
            
        print(f"{Colors.PURPLE}]{Colors.END}")
                
        return self.generate_report()
        
    def generate_report(self):
        self.crawl_count += 1
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"crawl_report_{self.crawl_count}_{timestamp}.txt"
        
        report = {
            "crawl_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_pages_crawled": len(self.visited_urls),
            "emails_found": list(self.found_emails),
            "phones_found": list(self.found_phones),
            "internal_links_found": list(self.found_links),
            "external_links_found": list(self.found_external_links),
            "crawled_urls": list(self.visited_urls)
        }
        
        # Save report to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("           WEB CRAWLER REPORT - EDUCATIONAL USE ONLY\n")
            f.write("="*60 + "\n")
            f.write(f"Crawl Date: {report['crawl_date']}\n")
            f.write(f"Total Pages Crawled: {report['total_pages_crawled']}\n")
            f.write(f"Emails Found: {len(report['emails_found'])}\n")
            f.write(f"Phone Numbers Found: {len(report['phones_found'])}\n")
            f.write(f"Internal Links Found: {len(report['internal_links_found'])}\n")
            f.write(f"External Links Found: {len(report['external_links_found'])}\n")
            f.write("="*60 + "\n\n")
            
            f.write("EMAILS FOUND:\n")
            f.write("-"*50 + "\n")
            for email in report['emails_found']:
                f.write(f"{email}\n")
                
            f.write("\nPHONE NUMBERS FOUND:\n")
            f.write("-"*50 + "\n")
            for phone in report['phones_found']:
                f.write(f"{phone}\n")
                
            f.write("\nINTERNAL LINKS FOUND:\n")
            f.write("-"*50 + "\n")
            for link in report['internal_links_found']:
                f.write(f"{link}\n")
                
            f.write("\nEXTERNAL LINKS FOUND:\n")
            f.write("-"*50 + "\n")
            for link in report['external_links_found']:
                f.write(f"{link}\n")
                
            f.write("\nCRAWLED URLs:\n")
            f.write("-"*50 + "\n")
            for url in report['crawled_urls']:
                f.write(f"{url}\n")
                
        return filename

def main():
    display_banner()
    
    crawler = EducationalWebCrawler()
    
    while True:
        url = input(f"{Colors.BLUE}{Colors.BOLD}💻 Enter the website/URL you want to crawl (or 'quit' to exit): {Colors.END}").strip()
        
        if url.lower() == 'quit':
            print(f"\n{Colors.GREEN}👋 Thanks for using the Web Crawler Tool! Happy ethical hacking! {Colors.END}🚀\n")
            break
            
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        try:
            print(f"\n{Colors.YELLOW}⚡ Crawling in progress... Please wait.{Colors.END}")
            start_time = time.time()
            
            report_file = crawler.start_crawling(url, max_pages=100)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            print(f"\n{Colors.GREEN}✅ Crawling completed in {elapsed_time:.2f} seconds!{Colors.END}")
            print(f"{Colors.GREEN}📄 Report saved to: {report_file}{Colors.END}")
            
            # Display summary
            print(f"\n{Colors.PURPLE}{Colors.BOLD}📊 CRAWL SUMMARY:{Colors.END}")
            print(f"{Colors.CYAN}📝 Pages crawled: {len(crawler.visited_urls)}{Colors.END}")
            print(f"{Colors.CYAN}📧 Emails found: {len(crawler.found_emails)}{Colors.END}")
            print(f"{Colors.CYAN}📞 Phone numbers found: {len(crawler.found_phones)}{Colors.END}")
            print(f"{Colors.CYAN}🔗 Internal links found: {len(crawler.found_links)}{Colors.END}")
            print(f"{Colors.CYAN}🌐 External links found: {len(crawler.found_external_links)}{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {str(e)}{Colors.END}")
            
        print(f"\n{Colors.ORANGE}{'='*70}{Colors.END}\n")

if __name__ == "__main__":
    main()