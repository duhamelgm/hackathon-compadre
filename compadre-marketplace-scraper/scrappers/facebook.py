from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

def main(city: str, query: str):
  # TODO - Add more cities to the dictionary.
  cities = {
      'New York': 'nyc',
      'Los Angeles': 'la',
      'Las Vegas': 'vegas',
      'Chicago': 'chicago',
      'Montréal': 'montreal'
  }
  # If the city is in the cities dictionary...
  if city in cities:
      # Get the city location id from the cities dictionary.
      city = cities[city]
  # If the city is not in the cities dictionary...
  else:
      # Exit the script if the city is not in the cities dictionary.
      # Capitalize only the first letter of the city.
      city = city.capitalize()
      # Raise an HTTPException.
      raise HTTPException (404, f'{city} is not a city we are currently supporting on the Facebook Marketplace. Please reach out to us to add this city in our directory.')
      # TODO - Try and find a way to get city location ids from Facebook if the city is not in the cities dictionary.
      
  # Define the URL to scrape.
  marketplace_url = f'https://www.facebook.com/marketplace/{city}/search/?query={query}'
  initial_url = "https://www.facebook.com/login/device-based/regular/login/"
  # Get listings of particular item in a particular city for a particular price.
  # Initialize the session using Playwright.
  with sync_playwright() as p:
      # Open a new browser page.
      browser = p.chromium.launch(headless=True)
      page = browser.new_page()
      # Navigate to the URL.
      page.goto(initial_url)
      # Wait for the page to load.
      time.sleep(2)
      try:
          email_input = page.wait_for_selector('input[name="email"]').fill('YOUREMAIL')
          password_input = page.wait_for_selector('input[name="pass"]').fill('YOURPASSWORD')
          #password_input = page.wait_for_selector('input[name="pass"]').fill('Compadre2024!')
          time.sleep(2)
          login_button = page.wait_for_selector('button[name="login"]').click()
          time.sleep(2)
          page.goto(marketplace_url)
      except:
          page.goto(marketplace_url)
      # Wait for the page to load.
      time.sleep(2)
      # Infinite scroll to the bottom of the page until the loop breaks.
      #for _ in range(5):
      #      page.keyboard.press('End')
      #      time.sleep(2)
      html = page.content()
      soup = BeautifulSoup(html, 'html.parser')
      parsed = []
      listings = soup.find_all('div', class_='x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e x1iorvi4 xjkvuk6 xnpuxes x291uyu x1uepa24')
      print('listings find:'+str(len(listings)))
      for listing in listings:
          try:
            image = None
            if listing.find('img', class_='xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3'):
                image = listing.find('img', class_='xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3')['src']
            # Get the item title from span.
            title=None
            if listing.find('span', 'x1lliihq x6ikm8r x10wlt62 x1n2onr6'):
                title = listing.find('span', 'x1lliihq x6ikm8r x10wlt62 x1n2onr6').text
            # Get the item price.
            price = "0"
            if listing.find('span', 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u'):
                price = listing.find('span', 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u').text
              # Get the item URL.
            post_url = None
            if listing.find('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1sur9pj xkrqix3 x1lku1pv'):
                post_url = listing.find('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1sur9pj xkrqix3 x1lku1pv')['href']

              #post_url = listing.find('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1sur9pj xkrqix3 x1s688f x1lku1pv')
              #post_url = listing.find('a', class_='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1lku1pv')['href']
              #print('post_url: '+post_url)       
              
              # Get the item location.
              #location = listing.find('span', 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa xo1l8bm xi81zsa').text
              #location = listing.find('span', 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84').text
              #print('location: '+location)       

              # Append the parsed data to the list.
            parsed.append({
                'image': image,
                'title': title,
                'price': price,
                'post_url': post_url,
                'location': city
            })
          except:
              pass
      # Close the browser.
      browser.close()
      # Return the parsed data as a JSON.
      result = []
      for item in parsed:
          result.append({
              'source': 'marketplace',
              'price': item['price'],
              'location': item['location'],
              'title': item['title'],
              'image': item['image'],
              'link': item['post_url']
          })
      return result[:10]