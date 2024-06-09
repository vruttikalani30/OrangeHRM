from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

default_wait = 30
selenium = None


class SeleniumHelpers:

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    # Wait Helpers

    # Wait until element is invisible
    def wait_Till_Element_Is_Visible(self, by_locator):
        return WebDriverWait(self.driver, default_wait).until(EC.visibility_of_element_located(by_locator))

    def wait_Till_Element_Is_Visible(self, by_locator, waitDurationInSeconds):
        return WebDriverWait(self.driver, waitDurationInSeconds).until(EC.visibility_of_element_located(by_locator))

    def wait_InCase_Element_Visible(self, by_locator, duration):
        wait = WebDriverWait(self.driver, duration)
        try:
            return wait.until(EC.visibility_of_element_located(by_locator))
        except Exception as e:
            return None

    # Wait until element is not invisible
    def wait_Till_Element_Is_Not_Visible(self, by_locator):
        WebDriverWait(self.driver, default_wait).until(EC.invisibility_of_element_located(by_locator))

    def wait_Till_Element_Is_Not_Visible(self, by_locator, waitDurationInSeconds):
        WebDriverWait(self.driver, waitDurationInSeconds).until(EC.invisibility_of_element_located(by_locator))

    # Wait until element is Click-able
    def wait_Till_Element_Is_Clickable(self, by_locator):
        wait = WebDriverWait(self.driver, default_wait)
        return wait.until(EC.element_to_be_clickable(by_locator))

    def wait_InCase_Element_Clickable(self, by_locator, duration):
        wait = WebDriverWait(self.driver, duration)
        try:
            return wait.until(EC.element_to_be_clickable(by_locator))
        except Exception as e:
            return None

    # Wait until element is Present
    def wait_Till_Element_Is_Present(self, by_locator):
        wait = WebDriverWait(self.driver, default_wait)
        return wait.until(EC.presence_of_element_located(by_locator))

    def wait_InCase_Element_Present(self, by_locator, duration):
        wait = WebDriverWait(self.driver, duration)
        try:
            return wait.until(EC.presence_of_element_located(by_locator))
        except Exception as e:
            return None

    # Wait till frame is available for switching
    def wait_Till_frame_ToBe_Available_And_SwitchToIt(self, by_locator):
        WebDriverWait(self.driver, default_wait).until(EC.frame_to_be_available_and_switch_to_it(by_locator))

    # Wait till element not attached to DOM
    def wait_Till_Element_Not_Attached_To_DOM(self, by_locator):
        WebDriverWait(self.driver, default_wait).until(EC.staleness_of(by_locator))

    # Waiting before performing next action
    def hard_wait(self, duration):
        time.sleep(duration * 1000)

    # Elements

    # Enter text to input field
    def enter_Text(self, by_locator, text):
        return self.wait_Till_Element_Is_Clickable(by_locator).send_keys(text)

    # Double click and enter text to input field
    def fill_Field_After_Double_Click(self, by_locator, text):
        self.wait_Till_Element_Is_Clickable(by_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(by_locator)
        actions.double_click()
        actions.send_keys(text)
        actions.perform()

    # Get Text from Field
    def get_Text(self, by_locator):
        Text = self.wait_Till_Element_Is_Visible(by_locator).text
        return Text

    # Click On Element
    def click_On(self, by_locator):
        self.wait_Till_Element_Is_Clickable(by_locator).click()

    # To determine whether WebElement has given Attribute or not
    def isElement_Attribute_Present(self, by_locator, attributeName):
        return self.wait_InCase_Element_Present(by_locator, default_wait).get_attribute(attributeName) is not None

    #  To get Element attribute value
    def getElement_Attribute_Value(self, by_locator, attributeName):

        if self.isElement_Attribute_Present(by_locator, attributeName):
            return self.wait_InCase_Element_Present(by_locator, default_wait).getattr(attributeName)
        else:
            return "Attribute" + attributeName + " not found"

    # Method verify whether element is present on screen
    def isElementPresent(self, by_locator):
        if self.wait_InCase_Element_Present(by_locator, default_wait) is not None:
            return self.wait_InCase_Element_Present(by_locator, default_wait).is_displayed()
        else:
            return False

    # Navigation
    def navigate_To_Page(self, url):
        self.driver.get(url)

    def refresh_Page(self):
        self.driver.refresh()

    def back_To_Page(self):
        self.driver.back()

    def forward_To_Page(self):
        self.driver.forward()

    # Alert
    def wait_Till_Alert_Present(self):
        WebDriverWait(self.driver, default_wait).until(EC.alert_is_present)

    def dismiss_Alert(self):
        self.driver.switch_to.alert.dismiss()

    def accept_Alert(self):
        self.driver.switch_to.alert.accept()

    # Switch to alert
    def switch_To_Alert(self):
        self.driver.switch_to_alert()

    def getText_From_Alert(self):
        return self.driver.switch_to.text

    # DropDown
    def select_Drop_down_Value_ByText(self, by_locator, text):
        select = Select(by_locator)
        select.select_by_visible_text(text)

    def getSelected_Drop_down_Value(self, by_locator):
        return Select(by_locator).first_selected_option.text.strip()

    def select_Drop_down_Value_ByIndex(self, by_locator, index):
        select = Select(by_locator)
        select.select_by_index(index)
        return Select(by_locator).first_selected_option.text.strip()

    def get_All_Drop_down_Values(self, by_locator):
        select = Select(by_locator)
        return select.all_selected_options.text.strip()

    # Action Event
    def focus_On_Element(self, by_locator):
        self.wait_Till_Element_Is_Clickable(by_locator)
        ActionChains(self.driver).move_to_element(by_locator).click().perform()
        # actions = ActionChains(self.driver)
        # actions.move_to_element(by_locator).click().perform()

    def double_ClickOn_Element(self, by_locator):
        self.wait_Till_Element_Is_Clickable(by_locator)
        ActionChains(self.driver).double_click(by_locator).perform()
        # actions = ActionChains(self.driver)
        # actions.double_click(by_locator).perform()

    def double_ClickOn_Element_WithOffset(self, by_locator_x, by_locator_y):
        self.wait_Till_Element_Is_Clickable(by_locator_x)
        self.wait_Till_Element_Is_Clickable(by_locator_y)
        ActionChains(self.driver).move_by_offset(by_locator_x, by_locator_y).double_click().perform()
        # actions = ActionChains(self.driver)
        # actions.move_by_offset(by_locator_x, by_locator_y).double_click().perform()

    def single_ClickOn_Element(self, by_locator):
        self.wait_Till_Element_Is_Clickable(by_locator)
        ActionChains(self.driver).move_to_element(by_locator).click().perform()
        # actions = ActionChains(self.driver)
        # actions.move_to_element(by_locator).click().perform()

    def single_ClickOn_Element_WithOffset(self, by_locator_x, by_locator_y):
        self.wait_Till_Element_Is_Clickable(by_locator_x)
        self.wait_Till_Element_Is_Clickable(by_locator_y)
        ActionChains(self.driver).move_by_offset(by_locator_x, by_locator_y).click().perform()
        # actions = ActionChains(self.driver)
        # actions.move_by_offset(by_locator_x, by_locator_y).click().perform()

    def drag_And_Drop(self, by_drag, by_drop):
        self.wait_Till_Element_Is_Clickable(by_drag)
        self.wait_Till_Element_Is_Clickable(by_drop)
        ActionChains(self.driver).click_and_hold(by_drag).move_to_element(by_drop).release(by_drag).perform()
        # actions = ActionChains(self.driver)
        # actions.click_and_hold(by_drag).perform()
        # self.hard_wait(30)
        # actions.move_to_element(by_drop).perform()
        # self.hard_wait(30)
        # actions.release(by_drag).perform()
        # self.hard_wait(30)

    # Page scrolls
    def page_Scroll_InView(self, by_locator):
        return self.driver.execute_script("arguments[0].scrollIntoView();", by_locator)

    # Browser's Tab handler
    def get_WindowHandle(self):
        return self.driver.getWindowHandle

    def switch_To_Window(self, windowHandle):
        self.driver.switch_to.window(windowHandle)

    # iFrames
    def switch_To_Iframe(self, iframe_Id):
        self.driver.switch_to.frame(iframe_Id)

    def switch_To_Iframe(self, iframe_Index):
        self.driver.switch_to.frame(iframe_Index)

    def swtich_ToMain_Iframe(self):
        self.driver.switch_to.default_content()
