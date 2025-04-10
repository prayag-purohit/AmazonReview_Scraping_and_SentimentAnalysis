import scrapy
import time 

class AmazonReviewsSpider(scrapy.Spider):
    name = 'amazon_reviews'
    allowed_domains = ['amazon.ca']
    start_urls = ['https://www.amazon.ca/dp/B0DZ7L4M9C?th=1']

    def parse(self, response):
        # Select all review elements using data-hook
        reviews = response.css('[data-hook="review"]')
        
        for review in reviews:
            time.sleep(3)  # Sleep for 1 second to avoid overwhelming the server
            yield {
                'username': review.css('.a-profile-name::text').get(default='').strip(),
                'rating': review.css('.review-rating .a-icon-alt::text').get(default='').strip(),
                'review_title': review.css('[data-hook="review-title"] span::text').get(default='').strip(),
                'review_text': ' '.join(review.css('[data-hook="review-body"] span::text').getall()).strip(),
                'review_date': review.css('[data-hook="review-date"]::text').get(default='').strip()
            }