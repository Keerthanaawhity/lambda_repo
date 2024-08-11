# lambda demo

This python script file contains three WEB UI automated scenarios using selenium

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium and add extensions of python from VS

```bash
pip install selenium
```

## Imports

```bash
# To control web browser
from selenium import webdriver

#For XPATH and element locator
from selenium.webdriver.common.by import By

#To make the driver wait to appear elements in DOM
from selenium.webdriver.support.ui import WebDriverWait

# Pre-defined conditions
from selenium.webdriver.support import expected_conditions as EC

#For simulating actions on web page 
from selenium.webdriver.common.action_chains import ActionChains

# To run different scenarios as separate unit tests
import unittest

```

## Description

Three different scenarios were run in unit test, The test cases will run based on the alphabetical order of the test case name.

scenario 1 [test_inputform]: Verify the error note on empty fields and success note after filling text fields.

scenario 2 [test_simpleFormDemo]: verify whether the entered text message is the same as the reflected message on clicking get text.

scenario 3 [test_slider]: verify the value in the text box is same as the offset value of the slider after performing action 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
