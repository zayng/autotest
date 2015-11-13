#-*-coding:utf-8-*-
from com.deppon.nhr.login.login import loginNhr
from com.deppon.nhr.login.login import menu
from com.deppon.nhr.login.login import driver,sleep
from selenium.webdriver.common.action_chains import ActionChains

loginNhr()
menu()
#认证开班管理
menuMan=driver.find_element_by_xpath(u"//div[text()='认证开班管理']")
menuMan.click()
sleep(2)
#新增开班

nBtnClass=driver.find_element_by_xpath(u"//div[@id='T_authinfo-authClassMng']//button[span[text()='新开班']]")
nBtnClass.click()

#输入开班名称

classNa=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='classname']")
classNa.send_keys(u"2015年一百届高级认证开班")

#输入地点

classAddr=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='address']")
classAddr.send_keys(u"德邦学院D122")
print("选择认证大类")
#点击认证大类下拉选择框

ciIdenti=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='identificationkind']")
ciIdenti.click()

#选择具体大类//body/div[contains(@id,'boundlist')]//li[text()='IT类']
seLarge=driver.find_element_by_xpath(u"//body/div[contains(@id,'boundlist')]//li[text()='IT类']")
seLarge.click()

print("选择认证层级")
#点击认证层级下拉选择框
ciLeve=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='classlevel']")
ciLeve.click()

#选择层级
seLeve=driver.find_element_by_xpath(u"//body/div[contains(@id,'boundlist')]//li[text()='中级']")
seLeve.click()
print("选择开始时间")
#选择开始时间
newBegin=driver.find_element_by_xpath(u"//td[@id='newClassbegintime-inputCell']/following-sibling::td/div[1]")
newBegin.click()

#切换到时间控件
frabegin=driver.find_element_by_xpath(u"//*[@width='97' and @height='9']")
driver.switch_to_frame(frabegin)
#driver.switch_to_frame(0)

#选择时间
seTime=driver.find_element_by_xpath(u"//td[@onclick='day_Click(2015,11,2);']")
#seTime.click()
ActionChains(driver).double_click(seTime).perform()
#点击确定
# btnOk=driver.find_element_by_id("dpOkInput")
# btnOk.click()

#切换表单

driver.switch_to_default_content()

#选择结束时间
newEnd=driver.find_element_by_xpath(u"//td[@id='newClassendtime-inputCell']/following-sibling::td/div[1]")
newEnd.click()

#切换到时间控件
fraend=driver.find_element_by_xpath(u"//*[@width='97' and @height='9']")
driver.switch_to_frame(fraend)
#driver.switch_to_frame(0)

#选择结束时间
seEndTime=driver.find_element_by_xpath(u"//td[@onclick='day_Click(2015,11,2);']")
#ActionChains(driver).double_click(seEndTime).perform()
btnOk=driver.find_element_by_id("dpOkInput")
btnOk.click()

driver.switch_to_default_content()

#保存新开班级
saClass=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//button[span[text()='确定']]")
saClass.click()
sleep(1)

#确定保存
reOk=driver.find_element_by_xpath(u"//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]")
reOk.click()

#新增班级成功
print("新增班级成功")
sleep(5)
driver.quit()
