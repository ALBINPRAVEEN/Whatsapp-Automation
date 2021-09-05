from time import sleep

from selenium import webdriver

driver = webdriver.Chrome('/home/s0umyajit/Downloads/chromedriver')
driver.get('https://web.whatsapp.com/')
print('Scan the QR code')


def send_msg():
    name = input("Enter the User Name or Group Name \t")
    msg = input("Enter the message \t")
    count = input("Enter the the number of times you want to send message \t")
    count = int(count)
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_3u328')
    for i in range(count):
        msg_box.send_keys(msg)
        btn = driver.find_element_by_class_name('_3M-N-')
        btn.click()
    return "Message Sent Successfully"


def send_doc():
    name = input("Enter the name of group or user\t")
    doc = input("Enter the path of the doc\t")
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()

    attach_box = driver.find_element_by_xpath('//div[@title="Attach"]')
    attach_box.click()

    document_box = driver.find_element_by_xpath('//input[@accept="*"]')
    document_box.send_keys(doc)
    sleep(6)
    btn = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
    btn.click()
    return "Document Sent Successfully"


def send_img():
    name = input("Enter the name of the user or group\t")
    image = input("Enter the path of the image/video\t")
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()

    attach_box = driver.find_element_by_xpath('//div[@title="Attach"]')
    attach_box.click()

    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(image)
    sleep(6)
    btn = driver.find_element_by_class_name('_1g8sv')
    btn.click()
    return "Image Sent Successfully"


if __name__ == "__main__":
    try:
        k = 1
        while k:
            print("Enter 1 to send message")
            print("Enter 2 to send doc")
            print("Enter 3 to send image and videos")
            print("Enter 4 to quit")
            x = int(input("Enter your choice\n"))
            if x == 1:
                y = send_msg()
                print(y)
            if x == 2:
                y = send_doc()
                print(y)
            if x == 3:
                y = send_img()
                print(y)
            if x == 4:
                exit()

    except Exception as e:
        print(e)
