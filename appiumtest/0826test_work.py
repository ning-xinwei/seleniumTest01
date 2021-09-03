from appium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 弹窗事件

class test_work(unittest.TestCase):
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
                                       desired_caps)  # 127.0.0.1和localhost代表本机  4723是端口号  wdWebDriver的缩写  hub主节点


    def tearDown(self) -> None:
        pass

    # 通过id定位
    # 定位推荐的搜索控件，输入内容并且点击搜索
    def test_01(self):
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # 定位搜索控件并点击
        current_activity = self.driver.current_activity
        time.sleep(10)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(3)
        # 定位输入框输入内容
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input")
        content = "起点中文网"
        ele.send_keys(content)
        self.driver.keyevent(84)
        new_activity = self.driver.current_activity
        self.assertEqual(ele.text,content)
        self.assertNotEqual(current_activity,new_activity)

    # 定位我的页面的最右好物，跳转最右好物页面
    def test_02(self):
        self.driver.implicitly_wait(60)
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # 定位我的控件并点击
        current_activity = self.driver.current_activity
        time.sleep(10)
        ele = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/textTabItem")
        ele[3].click()
        time.sleep(3)
        # 定位最右勋章控件
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/zy_medal").click()
        time.sleep(3)
        content = "最右勋章"
        ele_02 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/icon_title")
        ele_02.click()
        new_activity = self.driver.current_activity
        self.assertEqual(ele_02.text,content)
        self.assertNotEqual(current_activity,new_activity)

    # 定位动态控件，跳转动态页面
    def test_03(self):
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # 定位动态控件并点击
        time.sleep(10)
        ele = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/textTabItem")
        ele[1].click()
        time.sleep(3)
        # 定位动态页面的关注和广场
        ele_02 = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        content_01 = "关注"
        content_02 = "广场"
        self.assertEqual(ele_02[0].text,content_01)
        self.assertEqual(ele_02[1].text,content_02)

    # 定位推荐页的第一个帖子，点击进入帖子详情页面
    def test_04(self):
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # 定位第一个帖子并点击
        time.sleep(10)
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/expand_content_view")
        ele.click()
        title = ele.text
        time.sleep(3)
        # 定位帖子详情和帖子标题
        ele_02 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvTitle")
        tvTitle = "帖子详情"
        ele_03 = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvPostContent")
        self.assertEqual(title,ele_03.text)
        self.assertEqual(tvTitle,ele_02.text)

    # 检查推荐页顶部信息显示是否正确
    def test_05(self):
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        time.sleep(10)
        ele = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        self.assertEqual(ele[0].text,"关注")
        self.assertEqual(ele[1].text,"推荐")
        self.assertEqual(ele[2].text,"视频")
        self.assertEqual(ele[3].text,"图文")


    # 通过class_name定位
    # 定位推荐的搜索控件，输入内容并且点击搜索
    def test_06(self):
        self.driver.implicitly_wait(60)
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # 定位搜索控件并点击
        ele = self.driver.find_elements_by_class_name("android.widget.ImageView")
        ele[2].click()
        # 定位输入框输入内容
        ele_02 = self.driver.find_element_by_class_name("android.widget.EditText")
        content = "起点中文网"
        ele_02.send_keys(content)
        # self.driver.keyevent(84)
        self.assertEqual(ele_02.text,content)

    # 定位我的页面的最右好物，跳转最右好物页面
    def test_07(self):
        self.driver.implicitly_wait(60)
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # 定位我的控件并点击
        ele = self.driver.find_elements_by_class_name("android.widget.TextView")
        ele[-1].click()
        # 定位最右勋章控件
        self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[10].click()
        time.sleep(3)
        content = "最右勋章"
        ele_02 = self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual(ele_02[1].text,content)

    # 定位动态控件，跳转动态页面
    def test_08(self):
        self.driver.implicitly_wait(60)
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # 定位动态控件并点击
        ele = self.driver.find_elements_by_class_name("android.widget.TextView")
        ele[-4].click()
        # 定位动态页面的关注和广场
        ele_02 = self.driver.find_elements_by_class_name("android.widget.TextView")
        content_01 = "关注"
        content_02 = "广场"
        self.assertEqual(ele_02[2].text,content_01)
        self.assertEqual(ele_02[3].text,content_02)

    # 定位推荐页的第一个帖子，点击进入帖子详情页面
    def test_09(self):
        self.driver.implicitly_wait(60)
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        # 定位第一个帖子并点击
        ele = self.driver.find_elements_by_class_name("android.widget.TextView")
        ele[5].click()
        title = ele[5].text
        time.sleep(3)
        # 定位帖子详情和帖子标题
        ele_02 = self.driver.find_element_by_class_name("android.widget.TextView")
        tvTitle = "帖子详情"
        ele_03 = self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual(title,ele_03[4].text)
        self.assertEqual(tvTitle,ele_02.text)

    # 检查推荐页顶部信息显示是否正确
    def test_10(self):
        try:     # 有时最右APP会弹青少年模式，如果弹了，就把它关掉，如果不弹，也不会报错
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
        except:
            pass
        time.sleep(10)
        ele = self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual(ele[0].text,"关注")
        self.assertEqual(ele[1].text,"推荐")
        self.assertEqual(ele[2].text,"视频")
        self.assertEqual(ele[3].text,"图文")


    # 通过xpath定位
    # xpath通过id查找单个元素（定位关注按钮）
    def test_11(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/title']").click()
        content = "为你推荐10个右友"
        ele = self.driver.find_element_by_xpath("//*[@text='为你推荐10个右友']")
        self.assertEqual(ele.text,content)

    # xpath通过id查找多个元素，检查推荐页顶部信息显示
    def test_12(self):
        self.driver.implicitly_wait(60)
        ele = self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/title']")
        self.assertEqual(ele[0].text,"关注")
        self.assertEqual(ele[1].text,"推荐")
        self.assertEqual(ele[2].text,"视频")
        self.assertEqual(ele[3].text,"图文")

    # xpath通过text文本定位，有控件属性
    # 定位我的页面的小黑屋
    def test_13(self):
        self.driver.implicitly_wait(60)
        current_activity = self.driver.current_activity
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='小黑屋']").click()
        new_activity = self.driver.current_activity
        ele = self.driver.find_element_by_xpath("//android.widget.TextView[@text='小黑屋']")
        self.assertNotEqual(current_activity,new_activity)
        self.assertEqual(ele.text,"小黑屋")

    # xpath通过text文本定位，无控件属性
    # 定位我的页面的帮助和反馈
    def test_14(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//*[@text='我的']").click()
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        self.driver.swipe(width*0.7,height*0.8,width*0.7,height*0,3000)
        time.sleep(10)
        self.driver.find_element_by_xpath("//*[@text='帮助与反馈']").click()
        time.sleep(10)
        ele = self.driver.find_element_by_xpath("//*[@text='帮助与反馈']")
        self.assertEqual(ele.text, "帮助与反馈")

        # xpath通过class定位控件，定位搜索框，edittext
        # self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        # ele_05 = self.driver.find_element_by_xpath("//android.widget.EditText")
        # ele_05.click()

        # xpath通过class定位控件，定位搜索框，edittext
        # time.sleep(5)
        # ele = self.driver.find_elements_by_xpath("//android.widget.ImageView")
        # ele[3].click()
        # ele_06 = self.driver.find_element_by_xpath("//android.widget.EditText[@class='android.widget.EditText']")
        # ele_06.click()

        # xpath通过多个条件来定位
        # ele_07 = self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/title' and @text='视频']")
        # ele_07.click()

        # 通过父级找子级，定位搜索按钮
        # ele_08 = self.driver.find_element_by_xpath("//android.widget.FrameLayout[@resource-id='cn.xiaochuankeji.tieba:id/search_b']/android.widget.ImageView")
        # ele_08.click()

        # 通过父级找子级，多层级，定位个人头像
        # ele_09 = self.driver.find_element_by_xpath("//android.view.ViewGroup[@resource-id='cn.xiaochuankeji.tieba:id/avatar_view_root']/android.widget.ImageView[2]")
        # ele_09.click()

        # 通过子级找父级在找子级，从我的控件定位img控件
        # ele_10 = self.driver.find_element_by_xpath("//*[@text='我的']/../android.widget.ImageView")
        # ele_10.click()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_work)
    unittest.TextTestRunner(verbosity=2).run(suite)