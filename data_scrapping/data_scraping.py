# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# def scrape_amazon_bags(url):
#     # Headers bohat zaroori hain, warna Amazon block kar dega
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
#         'Accept-Language': 'en-US, en;q=0.5'
#     }

#     print("Scraping shuru ho rahi hai...")
#     response = requests.get(url, headers=headers)
    
#     if response.status_code != 200:
#         print(f"Error: Amazon ne block kar diya ya page nahi mila. Code: {response.status_code}")
#         return

#     soup = BeautifulSoup(response.content, 'html.parser')
#     products = []

#     # Amazon ke product cards ko dhoondna
#     items = soup.find_all('div', {'data-component-type': 's-search-result'})

#     for item in items:
#         name = item.find('h2').text.strip() if item.find('h2') else "N/A"
        
#         # Price nikalne ke liye
#         price_whole = item.find('span', 'a-price-whole')
#         price_fraction = item.find('span', 'a-price-fraction')
#         price = f"{price_whole.text}{price_fraction.text}" if price_whole else "N/A"
        
#         # Ratings
#         rating = item.find('span', 'a-icon-alt').text if item.find('span', 'a-icon-alt') else "N/A"

#         products.append({
#             'Product Name': name,
#             'Price': price,
#             'Rating': rating
#         })

#     # Data ko Excel/CSV mein save karna
#     df = pd.DataFrame(products)
#     df.to_csv('bagsmart_data.csv', index=False)
#     print(f"Done! {len(products)} products save ho gaye 'bagsmart_data.csv' mein.")

# # Aapka URL
# target_url = "https://www.amazon.com/s?k=bagsmart&page=3"
# scrape_amazon_bags(target_url)



import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_amazon_detailed(search_query, pages=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    
    all_products = []

    for page in range(1, pages + 1):
        print(f"Page {page} nikal raha hai...")
        url = f"https://www.amazon.com/s?k={search_query}&page={page}"
        
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Page {page} par masla aaya!")
            break
            
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in items:
            # 1. Name
            name = item.find('h2').text.strip() if item.find('h2') else "N/A"
            
            # 2. Price
            price = "N/A"
            price_box = item.find('span', 'a-offscreen')
            if price_box:
                price = price_box.text

            # 3. Rating
            rating = item.find('span', 'a-icon-alt').text.split(' ')[0] if item.find('span', 'a-icon-alt') else "0"

            # 4. Reviews Count
            reviews = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text if item.find('span', {'class': 'a-size-base', 'dir': 'auto'}) else "0"

            # 5. Delivery info (Analysis ke liye kaam aata hai)
            delivery = item.find('span', 'a-color-base').text if item.find('span', 'a-color-base') else "N/A"

            all_products.append({
                'Product Name': name,
                'Price': price,
                'Rating': rating,
                'Total Reviews': reviews,
                'Delivery': delivery,
                'Page': page
            })
        
        # Amazon ko gussa na aaye isliye thoda break
        time.sleep(2)

    df = pd.DataFrame(all_products)
    df.to_csv('amazon_analysis_ready.csv', index=False)
    print(f"Mubarak ho! {len(all_products)} lines ka data save ho gaya.")

# Run karein
scrape_amazon_detailed('bagsmart', pages=3)