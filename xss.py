import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = []
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and href.startswith('http'):
                    links.append(href)
            return links
        else:
            print("فشل في الوصول إلى الصفحة: ", url)
            return []
    except Exception as e:
        print("حدث خطأ: ", e)
        return []

def scan_for_xss(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            xss_found = False
            for tag in soup.find_all():
                if 'script' in tag.name:
                    print("تم العثور على علامة <script> مشبوهة في: ", url)
                    xss_found = True
            if not xss_found:
                print("لم يتم العثور على ثغرات XSS في: ", url)
        else:
            print("فشل في الوصول إلى الصفحة: ", url)
    except Exception as e:
        print("حدث خطأ: ", e)

start_url = "https://example.com"

max_depth = 2

scanned_links = set()

def crawl_and_scan(url, depth):
    if depth > max_depth:
        return
    if url in scanned_links:
        return
    print("جاري فحص: ", url)
    scanned_links.add(url)
    links = get_all_links(url)
    for link in links:
        absolute_url = urljoin(url, link)
        crawl_and_scan(absolute_url, depth + 1)
        scan_for_xss(absolute_url)

crawl_and_scan(start_url, 0)
