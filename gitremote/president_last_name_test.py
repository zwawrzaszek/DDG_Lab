import requests
import pytest

url = 'https://api.duckduckgo.com'

response = requests.get(url + "/?q=presidents+of+the+united+states&format=json")
json_data = response.json()

related_topics_dict = json_data['RelatedTopics']

text_from_related_topics = []
for entry in related_topics_dict:
    text_from_related_topics.append(entry['Text'])

big_string = ' '.join(text_from_related_topics)

word_split = big_string.split()

@pytest.mark.parametrize("president_last_name", ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe',
                            'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor',
                            'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson',
                            'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland',
                            'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding',
                            'Coolidge', 'Hoover', 'Truman', 'Eisenhower', 'Kennedy',
                            'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton',
                            'Obama', 'Trump'])

def test_presidents_last_name(president_last_name):
    assert president_last_name in word_split
