from selenium import webdriver
import time

# 通过id定位控件，定位淘宝首页购物车按钮并点击，跳转登录页面
'''
driver = webdriver.Chrome()
driver.get('http://taobao.com')
driver.maximize_window()
driver.find_element_by_id("mc-menu-hd").click()
'''

# 通过id定位控件，定位京东首页logo并点击，跳转页面
'''
driver = webdriver.Chrome()
driver.get('http://jd.com')
driver.maximize_window()
driver.find_element_by_id("logo").click()
'''

# 通过id定位控件，定位百度首页搜索框输入内容并点击，跳转页面
'''
driver = webdriver.Chrome()
driver.get('http://baidu.com')
driver.maximize_window()
driver.find_element_by_id("kw").send_keys('xiaohu')
driver.find_element_by_id('su').click()
'''

# 通过id定位控件，定位亚马逊首页登录按钮并点击，跳转登录页面
'''
driver = webdriver.Chrome()
driver.get('http://amazon.cn')
driver.maximize_window()
driver.find_element_by_id('nav-link-yourAccount').click()
'''

# 通过id定位控件，定位苏宁首页购物车控件并点击，跳转登录页面
'''
driver = webdriver.Chrome()
driver.get('http://suning.com')
driver.maximize_window()
driver.find_element_by_id("showTotalQty").click()
'''

# 通过name定位控件，定位2345头条首页的搜索框，输入内容，点击搜索
'''
driver = webdriver.Chrome()
driver.get('http://news.2345.com')
driver.maximize_window()
driver.find_element_by_name("w").send_keys('生活')
driver.find_element_by_class_name("search-btn").click()
'''

# 通过name定位控件，定位百度首页的更多控件，并点击
'''
driver = webdriver.Chrome()
driver.get('http://baidu.com')
driver.maximize_window()
driver.find_element_by_name("tj_briicon").click()
'''

# 通过name定位控件，定位12306首页并点击logo，刷新页面
'''
driver = webdriver.Chrome()
driver.get('http://12306.cn')
driver.maximize_window()
driver.find_element_by_name("g_href").click()
'''

# 通过name定位控件，定位云商系统首页输入框输入内容，点击搜索，跳转页面
'''
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php/')
driver.maximize_window()
driver.find_element_by_name("key").send_keys('libai')
driver.find_element_by_class_name('but2').click()
'''

# 通过name定位控件，定位当当网首页购物车控件并点击，跳转页面
'''
driver = webdriver.Chrome()
driver.get('http://dangdang.com')
driver.maximize_window()
driver.find_element_by_name("购物车").click()
'''

# 通过class_name定位控件，定位中关村在线首页拆机堂控件，跳转页面
'''
driver = webdriver.Chrome()
driver.get('http://zol.com.cn')
driver.maximize_window()
driver.find_element_by_class_name("tools-dismantle").click()
'''

# 通过class_name定位控件，定位优酷首页开通会员控件，跳转页面
'''
driver = webdriver.Chrome()
driver.get('http://youku.com')
driver.maximize_window()
driver.find_element_by_class_name("vip_icon_3Vril").click()
'''

# 通过class_name定位控件，定位爱奇艺首页热搜榜控件，跳转页面
'''
driver = webdriver.Chrome()
driver.get('http://iqiyi.com')
driver.maximize_window()
driver.find_element_by_class_name("search-right-entry").click()
'''

# 通过class_name定位控件，定位小说阅读网首页我的书架控件，跳转页面
'''
driver = webdriver.Chrome()
driver.get('http://readnovel.com')
driver.maximize_window()
driver.find_element_by_class_name("head-shelf").click()https://finance.sina.com.cn/
'''

# 通过class_name定位控件，定位新浪财经首页搜索控件，跳转页面
'''
driver = webdriver.Chrome()
driver.get('https://finance.sina.com.cn')
driver.maximize_window()
driver.find_element_by_class_name("cheadSeaSmt").click()
'''






