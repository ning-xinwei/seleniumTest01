from selenium import webdriver
import time


# 通过id定位控件
'''
driver = webdriver.Firefox()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id('cart_num').click()
'''

# 通过name定位控件
'''
driver = webdriver.Firefox()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_name('key').send_keys('乔丹')
'''

# 通过class定位控件
'''
driver = webdriver.Firefox()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_class_name('but1').send_keys('lining')
'''

# 进入百度页面，点击百度一下，因为百度一下的class_name是bg s_btn，是一个复合类，所以通过class_name定位不到，报错
'''
driver = webdriver.Firefox()
driver.get('http://baidu.com')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_class_name('bg s_btn').click()
'''

# 要定位一个a标签，并且有href属性，并且是一个可跳转链接，我们可以用find_element_by_link_text去定位它,文字要全部匹配
'''
driver = webdriver.Firefox()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_link_text('秒杀').click()
'''

# 要定位一个a标签，并且有href属性，并且是一个可跳转链接，我们可以用find_element_by_link_text去定位它,文字部分匹配即可，要匹配的这部分文字必须是唯一的
'''
driver = webdriver.Firefox()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_partial_link_text('活动').click()
'''

# 通过xpath查找控件
'''
driver = webdriver.Firefox()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
time.sleep(5)
# 绝对路径，以/开始 /html/body/div[2]/div/div[2]/div[1]/form/input[1]
#driver.find_element_by_xpath('/html/body/div/div/div/div/form/input[1]').send_keys('liuxiang')
# 相对路径，以//开始
#driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys('xiaoyan')
#driver.find_element_by_xpath('//input[@class="but1"]').send_keys('libai')
# contains包含，@后跟属性，后面跟该属性值要包含的内容
#driver.find_element_by_xpath('//input[contains(@placeholder,"请输入")]').send_keys('lindong')
# and，多个条件同事成立
#driver.find_element_by_xpath('//input[@class="but1" and @name="key"]').send_keys('muchen')
# //后边跟星号*，不管它是什么，只要能满足条件即可
driver.find_element_by_xpath('//*[@class="but1" and @name="key"]').send_keys('yuduxiu')
'''
