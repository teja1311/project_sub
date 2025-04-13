
from selenium.webdriver.common.by import By
from utils import locators
import pytest

@pytest.mark.parametrize("input_text, expected_result", [
    ("abcabcbb", "3"),
    ("bbbbb", "1"),
    ("", "0"),
    ("abcdef", "6"),
    ("a", "1"),
    ("abc123abc", "6"),
    ("pwwkew", "3"),
    ("abc@#a", "5"),
    ("abc abc", "4")
])

def test_longest_substring(setup_driver, input_text, expected_result):
    driver = setup_driver

    driver.get(locators.HOME_URL)

    driver.find_element(By.ID, locators.INPUT_BOX_ID).send_keys(input_text)

    driver.find_element(By.ID, locators.SUBMIT_BUTTON_ID).click()

    result_text = driver.find_element(By.ID, locators.RESULT_TEXT_ID).text

    assert result_text == expected_result
