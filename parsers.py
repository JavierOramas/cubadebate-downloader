import parsel
from parsel import Selector
from typing import List


def get_other_pages(html: Selector) -> List[str]:

    return html.css('.page::attr(href)').getall()


def get_news_page(html: Selector):
    for div in html.css('#archive > div.generic'):
        a = div.css('.title > a')

        yield {
            'tags': [tag for tag in div.attrib['class'].split(' ') if tag and tag != 'generic' ],
            'title': a.css('::text').get(),
            'link': a.css('::attr(href)').get()
        }


def get_news_info(html: Selector):

    text =  ''.join(html.css('.note_content ::text').getall()).strip()


    return {
        'text': text,
        'images': None,
    }


def get_comments(html: Selector):

    comments = html.css('li.comment')

    ans = []

    for comment in comments:
        ans.append({
            'attrs': [attr for attr in comment.attrib['class'].split(' ') ],
            'head': comment.css('.generic > div > cite > strong::text').get(),
            'text': ''.join(comment.css('.generic > div > p::text').getall()),
            'date': comment.css('.generic > div > .commentmetadata::text').get()
        })

    return ans

