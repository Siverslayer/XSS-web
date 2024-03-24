# XSS Vulnerability Scanner Program

This program is written in Python and is used to scan for potential XSS vulnerabilities in web pages.

## How it Works

- The program starts by specifying the starting URL for scanning.
- It gathers all the links from the specified homepage.
- It uses the `requests` library to access each link and fetch its content.
- It utilizes the `BeautifulSoup` library to parse the web page and search for suspicious tags like `<script>` which may indicate XSS vulnerabilities.
- Upon finding a suspicious tag, it displays an alert message.

## How to Use the Program

1. Set the main URL to be scanned in the `start_url` variable.
2. Specify the desired depth for scanning in the `max_depth` variable.
3. Run the program, and it will begin gathering links and searching for vulnerabilities.

## Warning
Ensure that you have proper authorization before scanning any website. Unauthorized scanning may violate terms of service and could be illegal.


## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` library

The program will start scanning the links and display the results.

This Markdown file now includes a warning section highlighted in red to emphasize the importance of proper authorization before scanning any website.


