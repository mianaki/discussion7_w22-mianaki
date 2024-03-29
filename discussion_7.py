from bs4 import BeautifulSoup
import requests
import unittest

# Task 2: Get the URL that links to webpage of universities with Olympic medal wins
# search for the url in the University of Michgian wikipedia page (in the third pargraph of the intro)
# HINT: You will have to add https://en.wikipedia.org to the URL retrieved using BeautifulSoup
def getLink(soup):
    tag = soup.find('a', title='List of American universities with Olympic medals')
    info = tag.get('href')
    return("https://en.wikipedia.org" + info)
    

# Task 3: Get the details from the box titled "College/school founding". Get all the college/school names and the year they were
# founded and organize the same into key-value pairs.
def getFoundingInfo(soup):
    table = soup.find('table', class_='toccolours')
    all_rows = table.find_all('tr')
    dict_schools = {}
    for row in all_rows[1:]:
        row_cell = row.find_all('td')
        school_name = row_cell[0].text.strip()
        year = row_cell[1].text.strip()
        dict_schools[school_name]= year
    return dict_schools

def main():
    # Task 1: Create a BeautifulSoup object and name it soup. Refer to discussion slides or lecture slides to complete this

    #### YOUR CODE HERE####
    url = 'https://en.wikipedia.org/wiki/University_of_Michigan'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    #Call the functions getLink(soup) and getFoundingInfo(soup) on your soup object.
    getLink(soup)
    getFoundingInfo(soup)

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        # Task1 continues: Create a BeautifulSoup object and name it soup
        #### YOUR CODE HERE####
        pass

    def test_link_nobel_laureates(self):
        self.assertEqual(getLink(self.soup), 'https://en.wikipedia.org/wiki/List_of_American_universities_with_Olympic_medals')

    def test_founding_info(self):
        self.assertEqual(getFoundingInfo(self.soup), {'Literature, Science, andthe Arts': '1841',
                                                            'Medicine':'1850',
                                                            'Engineering': '1854', 
                                                            'Law': '1859',
                                                            'Dentistry': '1875', 
                                                            'Pharmacy': '1876', 
                                                            'Music, Theatre &Dance': '1880', 
                                                            'Nursing': '1893', 
                                                            'Architecture &Urban Planning': '1906', 
                                                            'Graduate Studies': '1912', 
                                                            'Government': '1914', 'Education': 
                                                            '1921', 'Business': '1924', 
                                                            'Environment andSustainability': '1927', 
                                                            'Public Health': '1941', 
                                                            'Social Work': '1951', 
                                                            'Information': '1969', 
                                                            'Art & Design': '1974', 
                                                            'Kinesiology': '1984'})

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
