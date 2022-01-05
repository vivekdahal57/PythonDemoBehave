import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    __TIMEOUT = 30

    class __BasePage:
        def __init__(self, web_driver):
            self.driver = web_driver

        def __str__(self):
            return repr(self) + self.driver

    _web_driver = None

    def __init__(self, web_driver):
        super(BasePage, self).__init__()
        if not BasePage._web_driver:
            BasePage._web_driver = BasePage.__BasePage(web_driver)
        else:
            BasePage._web_driver.driver = web_driver

    def __getattr__(self, web_driver):
        return getattr(self._web_driver, web_driver)

    def open(self, url):
        # This method will type the given url in the browser
        self._web_driver.driver.set_page_load_timeout(30)
        self._web_driver.driver.maximize_window()
        self._web_driver.driver.get(url)

    def open_new_tab_and_switch_to_it(self):
        self._web_driver.driver.execute_script("window.open('', '_blank');")
        time.sleep(2)
        handles = self._web_driver.driver.window_handles
        size = len(handles)
        self._web_driver.driver.switch_to.window(handles[size - 1])

    def close_current_tab_and_switch_to_old(self):
        handles = self._web_driver.driver.window_handles
        size = len(handles)
        if size > 1:
            self._web_driver.driver.close()
            self._web_driver.driver.switch_to.window(handles[size - 2])
        time.sleep(2)

    def get_current_url(self):
        return self._web_driver.driver.current_url

    def action(self):
        return ActionChains(self._web_driver.driver)

    def find_element_by_xpath(self, xpath):
        # This method finds the element using xpath and return the element
        _web_driver_wait = WebDriverWait(self._web_driver.driver, BasePage.__TIMEOUT)
        return _web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def element_list_by_xpath(self, xpath):
        # This method find all the elements using xpath and return the elements
        _web_driver_wait = WebDriverWait(self._web_driver.driver, BasePage.__TIMEOUT)
        return _web_driver_wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))

    def find_element_by_id(self, identity):
        # This method finds the element using id and return the element
        _web_driver_wait = WebDriverWait(self._web_driver.driver, BasePage.__TIMEOUT)
        return _web_driver_wait.until(EC.visibility_of_element_located((By.ID, identity)))

    def find_element_by_name(self, name):
        # This method finds the element using name and return the element
        _web_driver_wait = WebDriverWait(self._web_driver.driver, BasePage.__TIMEOUT)
        return _web_driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_element(self, element, timeout=__TIMEOUT):
        # This method wait for the element and return the element
        _web_driver_wait = WebDriverWait(self._web_driver.driver, timeout)
        return _web_driver_wait.until(EC.visibility_of_element_located(element))

    def find_elements(self, element, timeout=__TIMEOUT):
        # This method wait for the element and return the element
        _web_driver_wait = WebDriverWait(self._web_driver.driver, timeout)
        return _web_driver_wait.until(EC.visibility_of_all_elements_located(element))

    def get_text(self, element, timeout=__TIMEOUT):
        # This method get text from the element and return the text
        elm = self.find_element(element, timeout)
        return elm.text

    def wait_until_element_disappear(self, element, timeout=__TIMEOUT):
        _web_driver_wait = WebDriverWait(self._web_driver.driver, timeout)
        return _web_driver_wait.until(EC.invisibility_of_element_located(element))

    def verify_text(self, element, text, timeout=__TIMEOUT):
        # This method get text from the element and verify it
        assert text in self.get_text(element, timeout), 'Element {} not found'.format(element)

    def click_element(self, element, timeout=__TIMEOUT):
        # This method clicks on the element provided by the user.
        # It first find the element, wait till its loaded and then click it.
        elm = self.find_element(element, timeout)
        elm.click()

    def reload_page(self):
        # It reloads the page
        self._web_driver.driver.refresh()

    def close_browser(self):
        # It closes the browser
        self._web_driver.driver.close()

    def send_value(self, element, value):
        # It types the value send by the user in the provided element.
        # It first find the element, wait till its loaded, clears it if
        # Enter or Return is not send and finally type the value.
        elm = self.find_element(element)
        if value != Keys.ENTER and value != Keys.RETURN:
            elm.clear()
        elm.send_keys(value)

    def upload_file(self, file_name):
        self._web_driver.driver.execute_script(
            "document.querySelector(arguments[0]).setAttribute('style','display:inline');", "input[type='file']")
        self._web_driver.driver.find_element_by_xpath("//input[@type='file']").send_keys(file_name)

    def zoom_browser(self, value):
        # This methods sets the zoom ratio with the provided value
        self._web_driver.driver.execute_script('document.body.style.zoom=\'' + str(value / 100) + '\'')

    def change_height(self, element, l_value=0):
        if l_value > 0:
            self._web_driver.driver.execute_script("arguments[0].setAttribute('style','height:" + str(l_value) + "px')",
                                                   element)

    def drag_from_drop_to(self, source_element, destination_element):
        # This method drag element from source to destination
        # (sometimes it might not work so scroll down to element first and then drag drop)
        self.action().drag_and_drop(self.find_element(source_element),
                                    self.find_element(destination_element)).perform()

    def drag_from_drop_to_js(self, source_element, destination_element):
        # ActionChains(self._web_driver.driver).click_and_hold(self.find_element(source_element)).move_to_element(self.find_element(destination_element)).release(self.find_element(destination_element)).perform()
        self._web_driver.driver.execute_script(
            "function createEvent(typeOfEvent) {\n" + "var event =document.createEvent(\"CustomEvent\");\n"
            + "event.initCustomEvent(typeOfEvent,true, true, null);\n" + "event.dataTransfer = {\n" + "data: {},\n"
            + "setData: function (key, value) {\n" + "this.data[key] = value;\n" + "},\n"
            + "getData: function (key) {\n" + "return this.data[key];\n" + "}\n" + "};\n" + "return event;\n"
            + "}\n" + "\n" + "function dispatchEvent(element, event,transferData) {\n"
            + "if (transferData !== undefined) {\n" + "event.dataTransfer = transferData;\n" + "}\n"
            + "if (element.dispatchEvent) {\n" + "element.dispatchEvent(event);\n"
            + "} else if (element.fireEvent) {\n" + "element.fireEvent(\"on\" + event.type, event);\n" + "}\n"
            + "}\n" + "\n" + "function simulateHTML5DragAndDrop(element, destination) {\n"
            + "var dragStartEvent =createEvent('dragstart');\n" + "dispatchEvent(element, dragStartEvent);\n"
            + "var dropEvent = createEvent('drop');\n"
            + "dispatchEvent(destination, dropEvent,dragStartEvent.dataTransfer);\n"
            + "var dragEndEvent = createEvent('dragend');\n"
            + "dispatchEvent(element, dragEndEvent,dropEvent.dataTransfer);\n" + "}\n" + "\n"
            + "var source = arguments[0];\n" + "var destination = arguments[1];\n"
            + "simulateHTML5DragAndDrop(source,destination);", self.find_element(source_element),
            self.find_element(destination_element))

    def scroll_to(self, element):
        self.action().move_to_element(self.find_element(element)).perform()

    def double_click_element(self, element):
        self.action().double_click(self.find_element(element)).perform()

    def select_value_from_options(self, element, value):
        select = Select(self.find_element(element))
        select.select_by_visible_text(value)

    def select_value_by_partial_text_options(self, element_id, value):
        # “In the basket are %s and %s” % (x,y)
        xpath = "//select[@id='%s']/option[contains(text(), '%s')]" % (str(element_id), str(value))
        elem = self.find_element((By.XPATH, xpath))
        elem.click()

    def does_element_exist(self, element):
        try:
            self.find_element(element, 2)
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True
