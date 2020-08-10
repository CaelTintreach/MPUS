import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Projects, UserStories

test_project_name = "Test Project"
test_userstory_name = "Test Story"
test_userstory_desc = "Test Desc"

class TestBase(LiveServerTestCase):

	def create_app(self): #Set environmental variables
		app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
		app.config['SECRET_KEY'] = getenv('SKEY')
		return app

	def setUp(self): #Setup the test driver
		print("--------------------------NEXT-TEST----------------------------------------------")
		chrome_options = Options()
		chrome_options.binary_location = "/usr/bin/chromium-browser"
		chrome_options.add_argument("--headless")
		self.driver = webdriver.Chrome(executable_path="/home/cliffordmckinney1997/chromedriver", chrome_options=chrome_options)
		self.driver.get("http://localhost:5000")
		db.session.commit()
		db.drop_all()
		db.create_all()

	def tearDown(self): #Remove the test driver once it is completed
		self.driver.quit()
		print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

	def test_server_is_up_and_running(self): #Test the server is currently running
		response = urlopen("http://localhost:5000")
		self.assertEqual(response.code, 200)

class TestProjectView(TestBase): #This function will test to ensure the button for projects view is working

	def test_projectview(self):
		self.driver.find_element_by_xpath("/html/body/div/a[3]").click()
		time.sleep(1)

		assert url_for('viewprojects') in self.driver.current_url

	if __name__ == '__main__':
		unittest.main(port=5000)

class TestUserStoryView(TestBase): #This function will test to ensure the button for user stories view is working

	def test_userstoryview(self):
		self.driver.find_element_by_xpath("/html/body/div/a[5]").click()
		time.sleep(1)

		assert url_for('viewuserstories') in self.driver.current_url		

	if __name__ == '__main__':
		unittest.main(port=5000)

class TestAllButtons(TestBase): #This function will test all the buttons in the navbar to ensure functionality

	def test_allbuttons(self):
		self.driver.find_element_by_xpath("/html/body/div/a[1]").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("/html/body/div/a[2]").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("/html/body/div/a[3]").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("/html/body/div/a[4]").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("/html/body/div/a[5]").click()
		time.sleep(1)
		assert url_for('viewuserstories') in self.driver.current_url

	if __name__ == '__main__':
		unittest.main(port=5000)

class TestAddProject(TestBase): #Test function for testing 

	def test_addproject(self):
		self.driver.find_element_by_xpath("/html/body/div/a[2]").click()
		self.driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/input").send_keys(test_project_name)
		self.driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/input").click()
		assert url_for('viewprojects') in self.driver.current_url

	if __name__ == '__main__':
		unittest.main(port=5000)