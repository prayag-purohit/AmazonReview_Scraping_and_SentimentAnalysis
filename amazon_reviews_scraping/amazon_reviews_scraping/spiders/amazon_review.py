import scrapy
import time 

import scrapy

class AmazonReviewsSpider(scrapy.Spider):
    name = 'amazon_reviews'
    allowed_domains = ['amazon.ca']
    
    # List of 10 product URLs to crawl
    start_urls = [
        'https://www.amazon.ca/dp/B0DZ7L4M9C?th=1',  
        'https://www.amazon.ca/dp/B08J4JRRCT?th=1',  
        'https://www.amazon.ca/dp/B0BY13SMZW?th=1',  
        'https://www.amazon.ca/dp/B082PM6T1J?th=1',  
        'https://www.amazon.ca/dp/B07FTPX71F?th=1',
        'https://www.amazon.ca/dp/B0CQN248PX?th=1',  
    ]

    def parse(self, response):
        # Extract reviews from the current product page
        reviews = response.css('[data-hook="review"]')
        
        for review in reviews:
            time.sleep(5) #Sleep for 3 seconds between requests to avoid being blocked
            yield {
                'username': review.css('.a-profile-name::text').get(default='').strip(),
                'rating': review.css('.review-rating .a-icon-alt::text').get(default='').strip(),
                'review_title': review.css('[data-hook="review-title"] span::text').get(default='').strip(),
                'review_text': ' '.join(review.css('[data-hook="review-body"] span::text').getall()).strip(),
                'review_date': review.css('[data-hook="review-date"]::text').get(default='').strip(),
                'product_url': response.url  # Add the product URL to each review
            }