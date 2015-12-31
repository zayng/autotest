from com.deppon.hrss.publ.log4 import log

def categor(driver, li, le):
    """
    新增开班，选择认证大类和层级
    """
    log.info("选择认证大类")
    # 点击认证大类下拉选择框
    ciidenti = driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='identificationkind']")
    ciidenti.click()
    # 选择具体大类//body/div[contains(@id,'boundlist')]//li[text()='IT类']
    selarge = driver.find_element_by_xpath("//ul[count(li)=13]/li[%s+1]" % li)
    selarge.click()
    log.info("选择认证层级")
    # 点击认证层级下拉选择框
    cileve = driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='classlevel']")
    cileve.click()
    log.info("选择认证层级")
    # 选择层级
    seleve = driver.find_element_by_xpath("//ul[count(li)=4]/li[%s+1]" % le)
    seleve.click()
    log.info("填写笔试成绩占比")
    if le in [0, 1, 2]:
        # 专业笔试成绩
        log.info("填写专业笔试成绩占比")
        writtenratio = driver.find_element_by_name("writtenratio")
        writtenratio.clear()
        if li in range(4, 7):
            writtenratio.send_keys(0)
        else:
            writtenratio.send_keys(20)
    elif le == 3:
        # 专业影响力
        log.info("填写专业影响力占比")
        majorratio = driver.find_element_by_name("majorratio")
        majorratio.clear()
        majorratio.send_keys(10)
    else:
        log.error("填写笔试成绩咱比异常")
