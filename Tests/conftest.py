import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Config.config import TestData
from Pages.LoginPage import LoginPage


@pytest.fixture(params=["chrome"],scope="session", autouse= True)
def init_driver(request):
    global web_driver
    if request.param=="chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.maximize_window()
        web_driver.implicitly_wait(5)
        web_driver.get(TestData.Base_Url)
        login = LoginPage(web_driver)
        login.do_login(TestData.Username, TestData.Password)
        session = request.node
        for item in session.items:
            cls = item.getparent(pytest.Class)
            setattr(cls.obj, "driver", web_driver)
    # if request.param=="edge":
    #     web_driver= webdriver.Edge(EdgeChromiumDriverManager().install())
    #     web_driver.maximize_window()
    # request.cls.driver= web_driver
    yield
    web_driver.quit()

def capture_screenshot(name):
    web_driver.get_screenshot_as_file(name)
    # S = lambda X: web_driver.execute_script("return document.body.parentNode.scroll" + X)
    # web_driver.set_window_size(S("Width"), S("Height"))
    # web_driver.find_element(By.TAG_NAME, 'body').screenshot(name)

def pytest_html_report_title(report):
    report.title="Automation Report"

@pytest.hookimpl(hookwrapper= True)
def pytest_runtest_makereport(item ,call):
    pytest_html=item.config.pluginmanager.getplugin('html')
    outcome=yield
    report=outcome.get_result()
    extra=getattr(report,'extra',[])
    if report.when=='call' or report.when=='setup':
        xfail=hasattr(report,'waxfail')
        if(report.skipped and xfail) or (report.failed and not xfail):
            filename=report.nodeid.replace(":","_")+".png"
            capture_screenshot(filename)
            if(filename):
                html='<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                     'onclick="window.open(this.src)" align="right"/></div>'%filename
                extra.append(pytest_html.extras.html(html))
        report.extra=extra