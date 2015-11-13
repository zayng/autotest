#-*-coding:utf-8-*-
from com.deppon.foss.login import loginFoss,menuNav
from com.deppon.foss.login import driver,sleep
from selenium.webdriver.common.action_chains import ActionChains

loginFoss()
menuNav() 

sleep(2)  
manTree=driver.find_element_by_xpath(u"//div[text()='交接单管理']").click()
sleep(2)
print("输入车牌号码")
vehicleNo=driver.find_element_by_xpath(u"//input[@name='vehicleNo']")
vehicleNo.send_keys(u"浙AY887R")
print("点击查询放大镜")
clVehicle=driver.find_element_by_xpath(u"//td[input[@name='vehicleNo']]/following-sibling::td[2]/div")
clVehicle.click()
sleep(2)
print("选择结果")
quVehicle=driver.find_element_by_xpath(u"//li[contains(text(),'浙AY887R')]")
quVehicle.click()
print("点击查询")
query=driver.find_element_by_xpath(u"//div[@id='T_load-handoverbillqueryindex']//button[span[text()='查询']]")
query.click()