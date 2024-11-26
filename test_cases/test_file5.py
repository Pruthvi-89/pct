from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_credence:

    def test_credence(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        offer = driver.find_element(By.XPATH,"//span[@class='text-white b label']").text
        print(offer)
        print(driver.title)
        if driver.title == "Credence":
            assert True
        else:
            assert False


    def test_contact_Number(self):
        driver=webdriver.Chrome()
        driver.get("https://credence.in/")

        driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()

        l = len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p////a"))
        list = []
        for r in range(1,l+1):
            contact=driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//a["+str(1)+"]")
            # print(contact)
            list.append(contact)


        if  "+91 9579064658" in list:
            assert True

        else:
            assert False





