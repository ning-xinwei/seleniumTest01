from appium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 弹窗事件

class AndroidTests(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {}  # 定义了一个字典
        desired_caps['platformName'] = 'Android'  # 平台名称
        desired_caps['platformVersion'] = '5.1'  # 平台版本，手机或平板的系统版本
        desired_caps['deviceName'] = 'Android Emulator'  # 设备名称，默认写Android Emulator模拟器
        desired_caps['noReset'] = 'True'  # 不重置APP
        # desired_caps['fullReset'] = 'True'  # 重置APP，。每一次跑完脚本，会把APP卸载掉
        # desired_caps['app'] = 'E:/idm下载/zuiyou518.apk'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'  # 包名
        desired_caps['appActivity'] = '.ui.base.SplashActivity'  # 指定activity名，获取初始页面的activity
        desired_caps['unicodeKeyboard'] = 'True'  # 会默认安装一个Appium自带的输入法，可以输入中文
        desired_caps['resetKeyboard'] = 'True'    # 重置输入法为Appium的输入法
        desired_caps['automationName'] = 'Uiautomator2'  # 需要它来处理toast，第二代uiautomator
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)  # 127.0.0.1和local
        # host代表本机  4723是端口号  wdWebDriver的缩写  hub主节点


    def tearDown(self) -> None:
        pass

    def test_toast(self):
        time.sleep(3)
        try:
            # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass

        self.driver.implicitly_wait(60)
        # 点击我的
        '''
        self.driver.find_element_by_xpath("//*[@text='我的']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@text='立即登录/注册']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@text='密码登录']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@text='请输入手机号']").send_keys("15127409611")
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/code_edit").send_keys("a123456")
        time.sleep(3)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@text='最右']").click()
        '''
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/holder_flow_rmdv").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.EditText").send_keys("123")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@text='发送']").click()
        time.sleep(3)
        toast_loc = ("xpath",".//*[contains(@text,'评论发送成功')]")
        ele = WebDriverWait(self.driver,20,0.1).until(EC.presence_of_element_located(toast_loc))
        print(ele.text)
        time.sleep(3)
        self.driver.keyevent(4)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

# APP自动化
# 我们之前做的APP已经基本稳定了，基本上三周、一个月一个迭代，所以我们之前做自动化的策略，把对应的所有P0级case，还有核心的一些p1级case实现自动化，
# 我们这一块做的核心的回归自动化测试，对之前老版本功能的回归验证，所以我们之前这块的用例都有，拿到用例，然后把对应P0和p1级case逐个去过一遍，加个执
# 行方式，分析哪些用例要去实现自动化，能实现自动化的就标自动，如果不能就标手工，此时把要实现自动化的用例梳理出来了，我们有对应的框架，框架会分为case
# 层、public层、report层和runner，case层用来放自动化用例，在case层中又分web和APP，web放web的自动化用例，APP放APP的自动化用例，在APP下又分
# 多个py文件，一个py文件对应一个模块的自动化用例，一个py文件就是一个类，这个类继承unittest.TestCase，有setUp、test方法和tearDown，setUp做
# 一些初始化，tearDown做一些截图、清理、释放的，每个test方法和手工用例是一一对应的。在做自动化的过程中，有很多公用的业务流程，如果在test方法中都去
# 写的话，如果业务流程变化，要修改每个test方法，维护量太大，在public下封装了一个公用的类，这个类中会有一些公用的不同的方法，这些业务方法辅助我们调用
# 如果业务流程有变，只需要修改这个公用的方法就好，不需要再去修改每个case，减少维护量，report把我们的一些报告放进去，report中放了一个HTMLtestrunner
# 用来给我们生成HTML报告的，最终还有一个runner，runner是批量运行我们所有的case下的所有自动化case的，最终生成一个报告

# APP自动化的环境搭建，基于python+Appium，先搭python，然后jdk的环境，SDK的环境，下载Appium server，pip安装Appium python Client，然后有
# 对应的模拟器或手机，看设备是否连接上，跑自动化，启动Appium server