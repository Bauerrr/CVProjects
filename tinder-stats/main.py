from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from os.path import exists
import keyboard
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#żeby program dobrze działał trzeba najpierw rozwinąć
#profil bo inaczej strona nie zassie wszystkich zainteresowan
#program reaguje na dwa przyciski
#q swipe w lewo
#w swipe w prawo
options = Options()
options.add_argument("user-data-dir=")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=options)
driver.get("https://tinder.com/app/recs")

#Nazwa pliku przechowującego dotychczasowe dane
file = ""

if exists(file):
    df = pd.read_csv(file)
    df_max_id = df['Id'].max()
else:
    df = pd.DataFrame(columns= ['Id','Interest', 'Like'] )
    df_max_id = -1
print(df_max_id)


def getInterest(like):
    '''
    Funkcja czyta input ze strony i
    wpisuje go do listy / lub do data frame
    df_max_id: najwyższe id w DataFrame
    like: 1 lub 0 zależnie od przesunięcia w prawo lub w lewo
    '''
    global df
    global df_max_id
    actions = ActionChains(driver)
    df_max_id += 1
    interests = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='interest']")
    for i in interests:
        df = df.append({'Id': df_max_id, 'Interest': i.text, 'Like': like}, ignore_index=True)
        print(i.text)
    if not interests:
        df = df.append({'Id': df_max_id, 'Interest': 'None', 'Like': like}, ignore_index=True)
    df.to_csv(file, index=False)

    if like == 1:
        actions.send_keys(Keys.RIGHT)
        actions.perform()
    else:
        actions.send_keys(Keys.LEFT)
        actions.perform()


while True:
    #strzalka w prawo
    if keyboard.read_key() == "w":
        print('w')
        getInterest(1)

    #strzalka w lewo
    if keyboard.read_key() == "q":
        print('q')
        getInterest(0)

    if keyboard.read_key() == "esc":
        driver.quit()
        break
