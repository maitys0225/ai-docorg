#!/usr/bin/env python3

"""
ChromeDriver Setup Script
-------------------------
This script downloads and initializes ChromeDriver using webdriver-manager.
Run this script from within your virtual environment to ensure ChromeDriver
is properly set up for your Selenium automation.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import platform
import sys

def setup_chrome_driver():
    print("Setting up ChromeDriver...")
    
    # Use webdriver_manager to download the appropriate ChromeDriver version
    # Set cache_valid_range to 1 to ensure we get a fresh driver
    driver_manager = ChromeDriverManager(cache_valid_range=1)
    driver_path = driver_manager.install()
    
    # Check if running on Apple Silicon Mac
    is_apple_silicon = platform.system() == "Darwin" and platform.machine() == "arm64"
    
    if is_apple_silicon:
        print("Detected Apple Silicon Mac (arm64)")
        # On Apple Silicon, we need to make sure we're using the arm64 version
        # Find the actual chromedriver executable (not the NOTICES file)
        base_path = os.path.dirname(driver_path)
        
        # Look for the correct chromedriver executable
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file == "chromedriver" or file == "chromedriver.exe":
                    driver_path = os.path.join(root, file)
                    # Make sure the file is executable
                    os.chmod(driver_path, 0o755)
                    print(f"Using arm64 ChromeDriver at: {driver_path}")
    
    # Print the final driver path we're using
    print(f"ChromeDriver path: {driver_path}")
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
    
    try:
        # Initialize the driver with the downloaded ChromeDriver
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Test the driver by visiting a website
        print("Testing ChromeDriver with a sample website...")
        driver.get("https://www.google.com")
        print(f"Page title: {driver.title}")
        
        # Close the driver
        driver.quit()
        print("ChromeDriver setup completed successfully!")
        return driver_path
    except Exception as e:
        print(f"Error setting up ChromeDriver: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure Google Chrome is installed on your system")
        print("2. Try manually downloading ChromeDriver from: https://chromedriver.chromium.org/downloads")
        print("3. Ensure the ChromeDriver version matches your Chrome version")
        print(f"4. Your system: {platform.system()} {platform.machine()}, Python {sys.version}")
        return None

if __name__ == "__main__":
    driver_path = setup_chrome_driver()
    if driver_path:
        print("\nYou can now use ChromeDriver in your Selenium scripts.")
        print(f"Driver location: {driver_path}")
        print("\nExample usage:")
        print("from selenium import webdriver")
        print("from selenium.webdriver.chrome.service import Service")
        print(f"service = Service('{driver_path}')")
        print("driver = webdriver.Chrome(service=service)")
        print("driver.get('https://example.com')")
    else:
        print("\nSetup failed. Please see the troubleshooting tips above.") 