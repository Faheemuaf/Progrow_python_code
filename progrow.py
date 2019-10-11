from selenium import webdriver
from selenium.common import exceptions
import pandas as pd 
# path of the driver in which it is installed.
browser = webdriver.Chrome('/home/faheem/Documents/workspace/scrapping/chromedriver_linux64/chromedriver')
browser.get('https://progrow.co.uk/shop/')
beach_balls = browser.find_elements_by_css_selector('li.o-Flex_Gutters.c-Feed_Item')
#print(type(beach_balls))
Name = []
Price = []
i = 1
while i < 104:
    try:
        beach_balls = browser.find_elements_by_css_selector('li.o-Flex_Gutters.c-Feed_Item')
        for ball in beach_balls:
           Name.append(ball.find_element_by_css_selector('h3.o-M15.c-Products_Title.c-Products_Title-lg a').text)
           Price.append(ball.find_element_by_css_selector('span.o-M25.c-Products_Price').text)

        browser.find_elements_by_css_selector('c-Btn.c-Pagination_Link')
        i += 1
    except exceptions.StaleElementReferenceException:
         pass
df = pd.DataFrame(list(zip(Name, Price)), columns=['Product Name', 'Product Price'])
beach_balls_data = df.to_csv('Progrow_data.csv', index=False)