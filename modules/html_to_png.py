"""
Convert a Plotly HTML file to a static PNG using headless Chrome.
"""

import os
from selenium import webdriver


def html_to_png(html_path, png_path, width=1500, height=800):
    """
    Convert a Plotly HTML file to a static PNG using headless Chrome.

    Parameters:
        html_path (str): Path to the input HTML file.
        png_path (str): Path to the output PNG file.
        width (int): Browser width in pixels.
        height (int): Browser height in pixels.
    """
    # Make sure the output folder exists
    os.makedirs(os.path.dirname(png_path), exist_ok=True)  
    # Set up headless Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--hide-scrollbars")
    # Set window size
    options.add_argument(f"--window-size={width},{height}")
    driver = webdriver.Chrome(options=options)

    # Open the HTML file
    driver.get(f"file://{os.path.abspath(html_path)}")

    # Take screenshot
    driver.save_screenshot(png_path)
    driver.quit()
    print(f"Saved PNG to {png_path}")
