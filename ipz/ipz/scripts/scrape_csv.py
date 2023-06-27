import requests
from bs4 import BeautifulSoup
import os, shutil
from django.conf import settings
import pandas as pd
import zipfile
from googlesearch import search
import datetime
import re


date_dict = dict()
queue_dict = dict()

def check_tracab_user(username: str, password: str):
    request_url = 'https://portal.tracab.com/login'
    with requests.Session() as session:
        # dostawanie sie do tracaba
        get_url = session.get(request_url)
        HTML = BeautifulSoup(get_url.text, 'html.parser')
        csrfmiddlewaretoken = HTML.find_all('input')[0]['value']
        print(csrfmiddlewaretoken)
        payload = {
            'identity': username,
            'password': password,
            'csrf_test_name': csrfmiddlewaretoken
        }
        headers = {
            'Referer': request_url
        }
        login_request = session.post(request_url,payload, headers=headers)
        league_results = session.get('https://portal.tracab.com/user/results/Ekstraklasa/2020')
        if len(league_results.text) == 0:
            raise Exception

def get_transfermarkt_url(player_name):
    try:
        first_name = player_name.split(" ")[0]
        second_name = player_name.split(" ")[1]
        request_url = f'https://www.transfermarkt.pl/schnellsuche/ergebnis/schnellsuche?query={first_name}+{second_name}'
    except:
        request_url = f'https://www.transfermarkt.pl/schnellsuche/ergebnis/schnellsuche?query={player_name}'
    #print(request_url)
    r = requests.get(request_url, headers = {'User-agent': 'your bot 0.1'})
    #print(r.text)
    try:
        soup = BeautifulSoup(r.text, 'html.parser')
        td = soup.find('td', {'class': 'hauptlink'})
        link = td.findChildren('a', recursive=False)[0]['href']
        ret_link = 'https://www.transfermarkt.pl'+link
    except:
        ret_link = 'nie udało się znaleźć linku'
    return ret_link

def scrapeTracab(username: str, password: str, base_dir):
    request_url = 'https://portal.tracab.com/login'
    with requests.Session() as session:
        # dostawanie sie do tracaba
        get_url = session.get(request_url)
        HTML = BeautifulSoup(get_url.text, 'html.parser')
        csrfmiddlewaretoken = HTML.find_all('input')[0]['value']
        print(csrfmiddlewaretoken)
        payload = {
            'identity': username,
            'password': password,
            'csrf_test_name': csrfmiddlewaretoken
        }
        headers = {
            'Referer': request_url
        }
        login_request = session.post(request_url,payload, headers=headers)
        # wyliczanie roku
        today = datetime.date.today()
        year = today.year
        league_results = session.get(f'https://portal.tracab.com/user/results/Ekstraklasa/{year}')
        print(league_results.ok)
        if league_results.ok:
            for i in range(year-2, year+1):
                print(i)
                league_results = session.get(f'https://portal.tracab.com/user/results/Ekstraklasa/{i}')
                HTML = BeautifulSoup(league_results.text, 'html.parser')
                weeks = HTML.find_all('a', {'class': 'mwTabs'})[0]['data-mw']
                game_ids = HTML.find_all('td', string=re.compile('Poland.'))
                download_link = HTML.select('a[href*=download]')
                # tworzenie linku do pobierania
                for a in download_link:
                    if 'default' in a['data-link'].lower() and 'false' not in a['data-link'].lower():
                        data_link = a['data-link']
                # pobieranie id gry i dodawnie daty gry
                for j in game_ids:
                    gid = j.text.split(' ')[1]
                    gid = gid.strip('(')
                    gid = gid.strip(')')
                    x = HTML.select(f'[matchid="{gid}"]')[0]
                    game_date = x.find('span').parent
                    date_dict[gid] = game_date.text
                # tworzenie folderu danego roku ekstraklasy
                dir_path = os.path.join(base_dir, 'ipz', 'zips', f'Ekstraklasa_{i}')
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                for j in range(1, int(weeks)+1):
                    mw_div = HTML.find('div',{'id': f'mw-{j}'})
                    td_gids = mw_div.select('[matchid]')
                    for k in td_gids:
                        gid = k.get('matchid')
                        queue_dict[gid] = [j,i]

                    # sprawdzanie których zipów brakuje
                    zip_name = f'week_{j}.zip'
                    zip_path = os.path.join(dir_path, zip_name)
                    if not os.path.exists(zip_path):
                        # tworzenie linku do danej kolejki jeśli zip nie istnieje
                        week_link = ''
                        week_link = data_link.replace("{matchWeekValue}", f"{j}")
                        week_link = 'https://portal.tracab.com' + week_link
                        # pobieranie zipa
                        download_request = session.get(week_link, allow_redirects=True)
                        open(zip_path, 'wb').write(download_request.content)
        else:
            for i in range(year-3, year):
                print(i)
                league_results = session.get(f'https://portal.tracab.com/user/results/Ekstraklasa/{i}')
                HTML = BeautifulSoup(league_results.text, 'html.parser')
                weeks = HTML.find_all('a', {'class': 'mwTabs'})[0]['data-mw']
                game_ids = HTML.find_all('td', string=re.compile('Poland.'))
                download_link = HTML.select('a[href*=download]')
                # tworzenie linku do pobierania
                for a in download_link:
                    if 'default' in a['data-link'].lower() and 'false' not in a['data-link'].lower():
                        data_link = a['data-link']
                # pobieranie id gry i dodawnie daty gry
                for j in game_ids:
                    gid = j.text.split(' ')[1]
                    gid = gid.strip('(')
                    gid = gid.strip(')')
                    x = HTML.select(f'[matchid="{gid}"]')[0]
                    game_date = x.find('span').parent
                    date_dict[gid] = game_date.text
                # tworzenie folderu danego roku ekstraklasy
                dir_path = os.path.join(base_dir, 'ipz', 'zips', f'Ekstraklasa_{i}')
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                for j in range(1, int(weeks)+1):
                    mw_div = HTML.find('div',{'id': f'mw-{j}'})
                    td_gids = mw_div.select('[matchid]')
                    for k in td_gids:
                        gid = k.get('matchid')
                        queue_dict[gid] = [j,i]

                    # sprawdzanie których zipów brakuje
                    zip_name = f'week_{j}.zip'
                    zip_path = os.path.join(dir_path, zip_name)
                    if not os.path.exists(zip_path):
                        # tworzenie linku do danej kolejki jeśli zip nie istnieje
                        week_link = ''
                        week_link = data_link.replace("{matchWeekValue}", f"{j}")
                        week_link = 'https://portal.tracab.com' + week_link
                        # pobieranie zipa
                        download_request = session.get(week_link, allow_redirects=True)
                        open(zip_path, 'wb').write(download_request.content)
                

def concatenate_csvs(base_dir):
    zip_dir = os.path.join(base_dir,'ipz','zips')
    csv_path = os.path.join(base_dir, 'csvs', 'Tracab_Data_Concatenated.csv')
    zip_contents = os.path.join(base_dir, 'ipz', 'zip_contents')
    count_concat = 0
    # tworzenie pustego pliku finalnego
    with open(csv_path, 'w'):
        pass
    for filename in os.listdir(zip_dir):
        ekstraklasa_path = os.path.join(zip_dir, filename)
        # dostanie sie do danego folderu danego sezonu
        # TODO: testowanie czy zip jest dobry, jeśli nie to continue na loopa żeby zrobić skip do kolejnej iteracji
        for ekstraklasa_file in os.listdir(ekstraklasa_path):
        # iterowanie po folderze z zipami
            print(ekstraklasa_file)
            ekstraklasa_file = os.path.join(ekstraklasa_path, ekstraklasa_file)
            try:
                with zipfile.ZipFile(ekstraklasa_file) as zip_file:
                    #otworzenie danego zipa
                    for name in zip_file.namelist():
                        # unzipowanie potrzebnych plików
                        if name.split("_")[-2] == "Summary" or name.split("_")[-2] == "Splits":
                            zip_file.extract(name, path=zip_contents)
            except:
                continue
        # przetwarzanie zip_contents - wejdź w folder, zajmij się plikami w nim, w między czasie usuń te niepotrzebne
        for dir in os.listdir(zip_contents):
            dir_path = os.path.join(zip_contents, dir)
            for csv in os.listdir(dir_path):
                #print(csv)
                if csv.split("_")[-2] == "Summary":
                    zip_csv_path = os.path.join(dir_path,csv)
                    #print(zip_csv_path)
                    game_id = csv.split("_")[0]
                    df = pd.read_csv(zip_csv_path, skiprows=9)
                    delimiter = df.loc[df['ID']=='ID'].index[0]
                    df_t1 = df[:delimiter]
                    df_t2 = df[delimiter+1:]
                    df_t1 = df_t1.drop('ID', axis=1)
                    df_t2 = df_t2.drop('ID', axis=1)
                    document_name = csv.split("_")
                    document_name[-2] = "Splits"
                    splits_csv = "_".join(document_name)
                    splits_csv_path = os.path.join(dir_path,splits_csv)
                    with open(splits_csv_path, 'r', encoding='utf8') as file:
                        lines = file.readlines()
                        druzyny = lines[1].replace("\"", "")
                        druzyny = druzyny.replace("\n", "")
                        #print(druzyny)
                    team1 = druzyny.split(" vs ")[0]
                    team2 = druzyny.split(" vs ")[1]
                    df_t1['team'] = team1
                    df_t2['team'] = team2
                    df_t1['game'] = druzyny
                    df_t2['game'] = druzyny
                    df_t1['season'] = queue_dict[game_id][1]
                    df_t2['season'] = queue_dict[game_id][1]
                    df_t1['date'] = date_dict[game_id]
                    df_t2['date'] = date_dict[game_id]
                    df_t1['queue'] = queue_dict[game_id][0]
                    df_t2['queue'] = queue_dict[game_id][0]
                    df_t1['transfermarkt'] = ''
                    df_t2['transfermarkt'] = ''
                    
                    if count_concat == 0:
                        df_t1.to_csv(csv_path, mode='a', header=True, index=False)
                    else:
                        df_t1.to_csv(csv_path, mode='a', header=False, index=False)
                    df_t2.to_csv(csv_path, mode='a', header=False, index=False)
                    count_concat += 1

        #usuwanie wszystkiego w zip_contents
        for f in os.scandir(zip_contents):
            path = os.path.join(zip_contents,f)
            shutil.rmtree(path)


def add_transfermarkt(base_dir):
    csv_path = os.path.join(base_dir, 'csvs', 'Tracab_Data_Concatenated.csv')
    df = pd.read_csv(csv_path)
    unique_players = df.iloc[:, 0].unique()
    # for i in unique_players:
    #     print(i)
    #df[df.shape[1]] = ""
    for i in unique_players:
        transfermarkt_url = get_transfermarkt_url(i)
        df.loc[df.iloc[:, 0] == i, df.columns[-1]] = transfermarkt_url
        #time.sleep(1)
        print(i)
        #print(df)
    df.to_csv(csv_path, sep=';', decimal=',', encoding='utf-8', index=False)
