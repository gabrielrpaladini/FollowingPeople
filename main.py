from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path=r"--block--")

browser.get("https://www.instagram.com/?hl=pt-br")

sleep(5)

conect = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a""")
sleep(4)
conect.click()

sleep(4)

emailInput = browser.find_elements_by_css_selector('form input')[0]
passwordInput = browser.find_elements_by_css_selector('form input')[1]

emailInput.send_keys("--block--")
passwordInput.send_keys("--block--")

sleep(4)

entrar = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button""")
sleep(4)
entrar.click()

sleep(4)

agora_nao = browser.find_element_by_xpath("""/html/body/div[3]/div/div/div[3]/button[2]""")
agora_nao.click()

sleep(4)

novas = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div[2]/div/button""")
sleep(4)
novas.click()

sleep(5)

browser.implicitly_wait(30)
buscar = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""")
sleep(4)
buscar.send_keys("nasa")
sleep(4)
buscar.click()
sleep(4)

nasa_perfil = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""")
nasa_perfil.click()

sleep(4)

count = 0

while(count < 1001):
    seguidores = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a""")
    sleep(2)
    seguidores.click()
    sleep(3)
    sleep(2)
    perfil = browser.find_element_by_xpath("""/html/body/div[3]/div/div[2]/ul/div/li[1]/div/div[3]/button""")
    perfil.click()
    count = count + 1
    print('Foram seguidos {} perfis!!'.format(count))
    sair =  browser.find_element_by_xpath("""/html/body/div[3]/div/div[1]/div/div[2]/button""")
    sair.click()
    sleep(2)
    browser.refresh()
    sleep(3)

print('Ao todo, foram adicionados {} seguidores na sua lista, finalizando script'.format(count))
    
