# Proxy Checker

This Python script retrieves a list of proxies from a website and checks their availability. It utilizes multithreading to improve performance.

## Features:
- Scrapes a website to extract a list of proxy IP addresses with ports
- Verifies the availability of proxies by sending HTTP requests
- Uses multithreading for concurrent checking of proxies
- Provides thread-safe access to the list of valid proxies

## Requirements:
- Python 3.x
- requests library (install using pip: `pip install requests`)

## Usage:
1. Clone the repository or download the script.
2. Install the required dependencies (requests library).
3. Run the script using the command: `python proxy_checker.py`

## Description:
The script starts by retrieving the content of a specified website (https://free-proxy-list.net/) to obtain a list of proxy IP addresses with ports. It uses regular expressions to extract the IP addresses and ports from the webpage content.

After obtaining the list of proxies, the script initiates a thread for each proxy to check its availability. Each thread sends an HTTP request to the same website using the corresponding proxy. If the request is successful (HTTP status code 200), the proxy is considered valid and added to the list of valid proxies.

The list of valid proxies is stored in a thread-safe list, ensuring safe access from multiple threads using a lock mechanism.

## Improvements:
1. Consider using a robust HTML parsing library like BeautifulSoup instead of regular expressions for extracting data from webpages.
2. Pass the list of valid proxies as an argument to the check_proxys function instead of using a global variable.
3. Implement additional checks or measures to ensure the reliability and efficiency of proxy availability verification.

## Disclaimer:
This script is for educational and informational purposes only. Usage of proxies should comply with the terms and conditions of the websites being accessed.

## Contributing:
Contributions are welcome! If you have any suggestions, bug reports, or improvements, feel free to submit a pull request or open an issue on GitHub.

## License:
This project is licensed under the MIT License. See the LICENSE file for details.

Author:
Manuel Barros
