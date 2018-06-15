from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time

class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_quiz(self):
    # Al heard about question and answer webapp so he decide to visit it
    self.browser.get(self.live_server_url)

    # He notice the page title and header say Question
    self.assertIn('Question', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Question', header_text)

    # He see a box below with text that say Enter your own question
    inputbox = self.browser.find_element_by_id('id_question')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own question'
    )

    # He types in "Is Waffle square pancake?"
    inputbox.send_keys('Is Waffle square pancake?')

    # He tick Yes for the answer
    answer = self.browser.find_element_by_id('id_yes_answer')
    answer.click()

    # He hit enter, the page update
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)

    # He see a box below with text that say Enter your own question
    inputbox = self.browser.find_element_by_id('id_question')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own question'
    )

    # He types in "Is Pancake triangle waffle?"
    inputbox.send_keys('Is Pancake triangle waffle?')

    # He tick No for the answer
    answer = self.browser.find_element_by_id('id_no_answer')
    answer.click()

    # He hit enter, the page update
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)

    # He see a box below with text that say Enter your own question
    inputbox = self.browser.find_element_by_id('id_question')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own question'
    )

    # He types in "Is waking up earlier hard?"
    inputbox.send_keys('Is waking up earlier hard?')

    # He tick Yes for the answer
    answer = self.browser.find_element_by_id('id_yes_answer')
    answer.click()

    # He hit enter, the page update
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)

    # He click on Start Quiz! to begin doing quiz
    start_quiz = self.browser.find_element_by_tag_name('a')
    start_quiz.click()

    # He see that the title change to Start! with Start Quiz as header
    self.assertIn('Start!', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Start Quiz', header_text)

    # He see the word Begin above quiz
    header_text = self.browser.find_element_by_tag_name('h2').text
    self.assertIn('Begin', header_text)

    # He see the first question and answer yes
    question = self.browser.find_element_by_id('q1').text
    self.assertIn('1. Is Waffle square pancake?', question)
    answer = self.browser.find_element_by_id('y1')
    answer.click()

    # He click Answer and see that he is corrected
    commit = self.browser.find_element_by_id('a1')
    commit.click()
    check = self.browser.find_element_by_id('c1').text
    self.assertIn('Correct', check)

    # He see the second question and answer no
    question = self.browser.find_element_by_id('q2').text
    self.assertIn('2. Is Pancake triangle waffle?', question)
    answer = self.browser.find_element_by_id('n2')
    answer.click()

    # He click Answer and see that he is correct
    commit = self.browser.find_element_by_id('a2')
    commit.click()
    check = self.browser.find_element_by_id('c2').text
    self.assertIn('Correct', check)

    # He see the third question and answer no
    question = self.browser.find_element_by_id('q3').text
    self.assertIn('3. Is waking up earlier hard?', question)
    answer = self.browser.find_element_by_id('n3')
    answer.click()

    # He click Answer and see that he is incorrect
    commit = self.browser.find_element_by_id('a3')
    commit.click()
    check = self.browser.find_element_by_id('i3').text
    self.assertIn('Incorrect', check)

    # He click on Add question to add quiz
    add_quiz = self.browser.find_element_by_tag_name('a')
    add_quiz.click()

    # He see a box below with text that say Enter your own question
    inputbox = self.browser.find_element_by_id('id_question')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own question'
    )

    # He types in "Is it raining today?"
    inputbox.send_keys('Is it raining today?')

    # He tick Yes for the answer
    answer = self.browser.find_element_by_id('id_yes_answer')
    answer.click()

    # He hit enter, the page update
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)

    # He click on Start Quiz! to begin doing quiz
    start_quiz = self.browser.find_element_by_tag_name('a')
    start_quiz.click()

    # He see the question that he add then answer yes
    question = self.browser.find_element_by_id('q4').text
    self.assertIn('4. Is it raining today?', question)
    answer = self.browser.find_element_by_id('y4')
    answer.click()

    # He click Answer and see that he is correct
    commit = self.browser.find_element_by_id('a4')
    commit.click()
    check = self.browser.find_element_by_id('c4').text
    self.assertIn('Correct', check)

    time.sleep(3)

    # After complete the quiz he close the computer and go to sleep
