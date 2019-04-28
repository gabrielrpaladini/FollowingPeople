from selenium import webdriver
from time import sleep

def waiting_browser():
	sleep(5)

browser = webdriver.Chrome(executable_path=r"--block--")

browser.get("https://www.instagram.com/?hl=pt-br")


conect = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a""")
waiting_browser()
conect.click()

waiting_browser()

emailInput = browser.find_elements_by_css_selector('form input')[0]
passwordInput = browser.find_elements_by_css_selector('form input')[1]

emailInput.send_keys("--block--")
passwordInput.send_keys("--block--")

waiting_browser()

entrar = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button""")
waiting_browser()
entrar.click()

waiting_browser()

agora_nao = browser.find_element_by_xpath("""/html/body/div[3]/div/div/div[3]/button[2]""")
agora_nao.click()

waiting_browser()

novas = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div[2]/div/button""")
waiting_browser()
novas.click()

waiting_browser()

browser.implicitly_wait(30)
buscar = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""")
waiting_browser()
buscar.send_keys("nasa")
waiting_browser()
buscar.click()
waiting_browser()
nasa_perfil = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""")
nasa_perfil.click()

waiting_browser()

count = 0

while(count < 1001):
    seguidores = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a""")
    waiting_browser()
    seguidores.click()
    waiting_browser()
    waiting_browser()
    perfil = browser.find_element_by_xpath("""/html/body/div[3]/div/div[2]/ul/div/li[1]/div/div[3]/button""")
    perfil.click()
    count = count + 1
    print('Foram seguidos {} perfis!!'.format(count))
    sair =  browser.find_element_by_xpath("""/html/body/div[3]/div/div[1]/div/div[2]/button""")
    sair.click()
    waiting_browser()
    browser.refresh()
    waiting_browser()

print('Ao todo, foram adicionados {} seguidores na sua lista, finalizando script'.format(count))
    
