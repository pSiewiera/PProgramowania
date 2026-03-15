
import unittest
from selenium import webdriver
from selenium . webdriver . common . by import By
import time
class TestCase ( unittest . TestCase ):
    def setUp ( self ):
        self . driver = webdriver . Edge ()

    def tearDown ( self ) :
        self . driver . close ()

class InputTesting ( TestCase ):
    BLOG_URL = " https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrVS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNSy0v1k9JTUsszSlRsgYAa16bfc1a21dc0e1c7f0e7a3aab272ef62ddf4eee&locale=pl"
    INPUT_NAME = "username"

    def test_input_value ( self ):
        self . driver . get ( self . BLOG_URL )
        try :
            login_box = self . driver . find_element ( by = By . NAME , value = self . INPUT_NAME )
            button = self . driver . find_element ( by = By . ID , value = "clearForm" )
        except Exception :
            self . fail (" Login input not found !")
        login_box . send_keys ("your_username")
        inputValue = login_box . get_attribute ("value")
        self . assertEqual ("your_username", inputValue )
        button. click ()
        inputValue = login_box . get_attribute ("value")
        self . assertEqual ("",inputValue)
        
unittest.main(argv=['first-arg-is-ignored'], exit=False)
if __name__ == '__main__':
    unittest.main()

    #test