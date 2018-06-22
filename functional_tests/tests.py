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
    # Al ได้ยินว่ามีเว็บตอบคำถามเลยลองเข้าไปดู
    self.browser.get(self.live_server_url)

    # He notice the page title and header say Question
    # เขาเห็นว่าหน้าเว็บมีชื่อว่า Question
    self.assertIn('Question', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Question', header_text)

    # He see a box below with text that say Enter your own question
    # เขาเห็นกล่องตอบคำถามที่เขียน Enter your own question
    inputbox = self.browser.find_element_by_id('id_question')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own question'
    )

    # He types in "Is Waffle square pancake?"
    # เขาพิมพ์ว่า "Is Waffle square pancake?"
    inputbox.send_keys('Is Waffle square pancake?')

    # He tick Yes for the answer
    # เขาให้ข้อนี้มีคำตอบเท่ากับ Yes
    answer = self.browser.find_element_by_id('id_yes_answer')
    answer.click()

    # He hit enter, the page update
    # เขากด enter แล้วหน้าจะทำการบันทึกข้อมูลแล้วรีเฟรช
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)

    # He see a box below with text that say Enter your own question
    # เขาเพิ่มคำถามอีกอัน
    inputbox = self.browser.find_element_by_id('id_question')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own question'
    )

    # He types in "Is Pancake triangle waffle?"
    # คราวนี้ใส่คำถามว่า "Is Pancake triangle waffle?"
    inputbox.send_keys('Is Pancake triangle waffle?')

    # He tick No for the answer
    # เขาให้ข้อนี้ตอบ No
    answer = self.browser.find_element_by_id('id_no_answer')
    answer.click()

    # He hit enter, the page update
    # เขากด enter แล้วหน้าจะทำการบันทึกข้อมูลแล้วรีเฟรช
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)

    # He see a box below with text that say Enter your own question
    # เขาทำการเพิ่มอีกคำถาม
    inputbox = self.browser.find_element_by_id('id_question')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own question'
    )

    # He types in "Is waking up earlier hard?"
    # เขาตั้ง้คำถามนี้ว่า "Is waking up earlier hard?"
    inputbox.send_keys('Is waking up earlier hard?')

    # He tick Yes for the answer
    # เขาให้ข้อนี้ตอบ Yes
    answer = self.browser.find_element_by_id('id_yes_answer')
    answer.click()

    # He hit enter, the page update
    # เขากด enter แล้วหน้าจะทำการบันทึกข้อมูลแล้วรีเฟรช
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)


    # He click on Start Quiz! to begin doing quiz
    # เขาจะเริ่มการทำตอบคำถาม โดยคลิก Start Quiz! เพื่อไปที่หน้าเริ่ม
    start_quiz = self.browser.find_element_by_tag_name('a')
    start_quiz.click()

    # He see that the title change to Start! with Start Quiz as header
    # เขาเห็นชื่อหน้าเว็บว่าเป็น Start! โดยที่มีหัวข้อเขียนว่า Start Quiz
    self.assertIn('Start!', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Start Quiz', header_text)

    # He see the word Begin above quiz
    # เขาเห็นว่าจะมีหัวข้อเขียนว่า Begin ก่อนจะมีการเริ่มตอบคำถาม
    header_text = self.browser.find_element_by_tag_name('h2').text
    self.assertIn('Begin', header_text)

    # He see the first question and answer yes
    # เขาเห็นคำถามแรกแล้วทำการเลือกตอบว่า yes
    question = self.browser.find_element_by_id('q1').text
    self.assertIn('1. Is Waffle square pancake?', question)
    answer = self.browser.find_element_by_id('y1')
    answer.click()

    # He click Answer and see that he is corrected
    # เขากด Answer แล้วเห็นว่าเป็นคำตอบที่ถูกต้อง
    commit = self.browser.find_element_by_id('a1')
    commit.click()
    check = self.browser.find_element_by_id('c1').text
    self.assertIn('Correct', check)

    # He see the second question and answer no
    # เขาเห็นคำถามที่สองแล้วทำการเลือกตอบว่า no
    question = self.browser.find_element_by_id('q2').text
    self.assertIn('2. Is Pancake triangle waffle?', question)
    answer = self.browser.find_element_by_id('n2')
    answer.click()

    # He click Answer and see that he is correct
    # เขากด Answer แล้วเห็นว่าเป็นคำตอบที่ถูกต้อง
    commit = self.browser.find_element_by_id('a2')
    commit.click()
    check = self.browser.find_element_by_id('c2').text
    self.assertIn('Correct', check)

    # He see the third question and answer no
    # เขาเห็นคำถามที่สามแล้วทำการเลือกตอบว่า no
    question = self.browser.find_element_by_id('q3').text
    self.assertIn('3. Is waking up earlier hard?', question)
    answer = self.browser.find_element_by_id('n3')
    answer.click()

    # He click Answer and see that he is incorrect
    # เขากด  Answer แล้วเห็นว่าเป็นคำตอบที่ผิด
    commit = self.browser.find_element_by_id('a3')
    commit.click()
    check = self.browser.find_element_by_id('i3').text
    self.assertIn('Incorrect', check)

    # He click on Add question to add quiz
    # เขากดย้อนกลับไปที่หน้าหลักโดยคลิกที่ Add question
    add_quiz = self.browser.find_element_by_tag_name('a')
    add_quiz.click()

    # He see a box below with text that say Enter your own question
    # เขาทำการพิมพ์ไปที่ช่องเพื่อเพิ่มคำถาม
    inputbox = self.browser.find_element_by_id('id_question')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your own question'
    )

    # He types in "Is it raining today?"
    # เขาทำการเพิ่มคำถามใหม่คือ "Is it raining today?"
    inputbox.send_keys('Is it raining today?')

    # He tick Yes for the answer
    # เขาให้ข้อนี้ตอบ yes
    answer = self.browser.find_element_by_id('id_yes_answer')
    answer.click()

    # He hit enter, the page update
    # เขากด enter แล้วหน้าจะทำการบันทึกข้อมูลแล้วรีเฟรช
    inputbox.send_keys(Keys.ENTER)
    time.sleep(3)

    # He click on Start Quiz! to begin doing quiz
    # เขากดไปที่หน้าตอบคำถามอีกครั้ง โดยคลิกที่ Start Quiz!
    start_quiz = self.browser.find_element_by_tag_name('a')
    start_quiz.click()

    # He see the question that he add then answer yes
    # เขาเจอคำถามที่เพิ่มเข้าไปแล้วทำการตอบ yes
    question = self.browser.find_element_by_id('q4').text
    self.assertIn('4. Is it raining today?', question)
    answer = self.browser.find_element_by_id('y4')
    answer.click()

    # He click Answer and see that he is correct
    # เขาเห็นว่าคำตอบนั้นถูกต้อง
    commit = self.browser.find_element_by_id('a4')
    commit.click()
    check = self.browser.find_element_by_id('c4').text
    self.assertIn('Correct', check)

    time.sleep(3)

    # After complete the quiz he close the computer and go to sleep
    # หลังจากที่ทำเสร็จเขาปิดตอมแล้วไปนอน
