from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class TextVerify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.lambdatest.com/selenium-playground/")
        
    def test_simpleFormDemo(self):
        
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Simple Form Demo']"))).click()
        print(self.driver.title)
        EnteredText = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-message']")))
        EnteredText.clear()
        IPtext = "Welcome to Lambda Test"
        EnteredText.send_keys(IPtext)
        
        button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, "showInput")))
        button.click()
        
        DisplayedText = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//p[@id='message']")))
        OPtext = DisplayedText.text
 
        self.assertEqual(IPtext, OPtext, "Input text and output text mismatch")
        self.driver.back()
    
    def test_slider(self):
        
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Drag & Drop Sliders']"))).click()
        Slider = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@value='15']")))

        x_offset = 95

        actions = ActionChains(self.driver)
        actions.click_and_hold(Slider).move_by_offset(188, 0).perform()
        After = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//output[@id='rangeSuccess']"))).text

        self.assertEqual(x_offset, int(After), "Slider is mismatched")
        self.driver.back()
        
    def test_inputform(self):
        
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Input Form Submit']"))).click()
        
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Submit']"))).click()
        Errormessage = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).get_attribute("validationMessage")
        ActualErrorMessage = "Please fill out this field."
        self.assertEqual(ActualErrorMessage, Errormessage, "Fields are not empty")
        
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).send_keys("Ruby")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputEmail4']"))).send_keys("xxx@gmail.com")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputPassword4']"))).send_keys("XXyyzz@12345")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='company']"))).send_keys("XYZ")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='websitename']"))).send_keys("xyz.com")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='country']"))).click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//option[@value='US']"))).click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputCity']"))).send_keys("Seattle")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputAddress1']"))).send_keys("X street")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputAddress2']"))).send_keys("Y Plot")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputState']"))).send_keys("LA")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputZip']"))).send_keys("889966")
        
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Submit']"))).click()
        
        success_message = "Thanks for contacting us, we will get back to you shortly."
        AftersubmitText = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='success-msg hidden']"))).text
        
        self.assertEqual(success_message, AftersubmitText, "Form not submitted")
        self.driver.back()

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()