from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
  
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Al heard about question and answer webapp so he decide to visit it
    self.browser.get('http://localhost:8000')

    # He notice the page title and header say Question
    self.assertIn('Question', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Question', header_text)

    # He see a box below with text that say Enter your own question
    inputbox = self.browser.find_element_by_id('id_new_question')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own question'
    )
    # He types in "Is it raining today?"
    inputbox.send_keys('Is it raining today?')

    # He hit enter, the page update
    inputbox.send_keys(Keys.ENTER)

    import time
    time.sleep(10)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(
        any(row.text == '1:Is it raining today?' for row in rows)
    )
    # To be continue
    self.fail('Finish test')


if __name__ == '__main__':
  unittest.main(warnings='ignore')
