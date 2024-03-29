from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    x = get_team_players('red rabbits')

    print(x)


def get_team_players(team):
    teams = ["red rabbits", "yellow yaks", "lime llamas", "cyan coyotes", "blue bats", "pink parrots", "green geckos",
             "purple pandas", " orange ocelots", " aqua axolotls"]

    match = False

    for i in teams:
        if team.lower() == i:
            match = True

    if not match:
        return None
    else:
        driver = webdriver.Chrome()
        driver.get("https://mcc.live")
        time.sleep(5)
        elem = driver.find_element(By.ID, 'app-body')
        elem = elem.find_element(By.ID, 'app-root')
        elem = elem.find_element(By.CLASS_NAME, 'container')
        elem = elem.find_element(By.CLASS_NAME, 'flexbox')
        elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]')
        elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]')
        elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div')
        elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul')
        counter = 1
        while counter < 10:
            team_name = elem.find_element(By.XPATH,
                                          f'//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[{counter}]/div/div/div[1]/h2/span')
            if team_name.text.lower() == team:
                break

            counter = counter + 1

        elem = elem.find_element(By.XPATH,
                                 f'//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[{counter}]/div/div/div[2]/div[1]/a/img')
        team_player1 = elem.get_attribute("alt").split(",", 1)

        elem = elem.find_element(By.XPATH,
                                 f'//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[{counter}]/div/div/div[2]/div[2]/a/img')
        team_player2 = elem.get_attribute("alt").split(",", 1)

        elem = elem.find_element(By.XPATH,
                                 f'//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[{counter}]/div/div/div[2]/div[3]/a/img')
        team_player3 = elem.get_attribute("alt").split(",", 1)

        elem = elem.find_element(By.XPATH,
                                 f'//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[{counter}]/div/div/div[2]/div[4]/a/img')
        team_player4 = elem.get_attribute("alt").split(",", 1)

        team_players = [team_player1[0], team_player2[0], team_player3[0], team_player4[0]]

        return team_players


def get_team_positions():
    driver = webdriver.Chrome()
    driver.get("https://mcc.live")
    time.sleep(5)
    elem = driver.find_element(By.ID, 'app-body')
    elem = elem.find_element(By.ID, 'app-root')
    elem = elem.find_element(By.CLASS_NAME, 'container')
    elem = elem.find_element(By.CLASS_NAME, 'flexbox')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]')

    team1 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[1]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[1]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[1]/div/div/div[1]/h3').text]

    team2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[2]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[2]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[2]/div/div/div[1]/h3').text]

    team3 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[3]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[3]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[3]/div/div/div[1]/h3').text]

    team4 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[4]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[4]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[4]/div/div/div[1]/h3').text]

    team5 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[5]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[5]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[5]/div/div/div[1]/h3').text]

    team6 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[6]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[6]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[6]/div/div/div[1]/h3').text]

    team7 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[7]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[7]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[7]/div/div/div[1]/h3').text]

    team8 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[8]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[8]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[8]/div/div/div[1]/h3').text]

    team9 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[9]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[9]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[9]/div/div/div[1]/h3').text]

    team10 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[10]/div/div/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[10]/div/div/div[1]/h2/span').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[1]/div[2]/div/ul/li[10]/div/div/div[1]/h3').text]

    team_list = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10]

    return team_list


def get_all_players():
    driver = webdriver.Chrome()
    driver.get("https://mcc.live")
    time.sleep(5)
    assert "MCC" in driver.title
    elem = driver.find_element(By.ID, 'app-body')
    elem = elem.find_element(By.ID, 'app-root')
    elem = elem.find_element(By.CLASS_NAME, 'container')
    elem = elem.find_element(By.CLASS_NAME, 'flexbox')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]')
    elem = elem.find_element(By.TAG_NAME, 'div')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul')
    elem = elem.find_element(By.CLASS_NAME, 'statistic')
    # player 1

    player1 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[1]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[1]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[1]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player3 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[3]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[3]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[3]/span[2]/p').text]
    player4 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[4]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[4]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[4]/span[2]/p').text]
    player5 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[5]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[5]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[5]/span[2]/p').text]
    player6 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[6]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[6]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[6]/span[2]/p').text]
    player7 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[7]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[7]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[7]/span[2]/p').text]
    player8 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[8]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[8]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[8]/span[2]/p').text]
    player9 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[9]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[9]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[9]/span[2]/p').text]
    player10 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[10]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[10]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[10]/span[2]/p').text]
    player11 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[11]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[11]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[11]/span[2]/p').text]
    player12 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[12]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[12]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[12]/span[2]/p').text]
    player13 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[13]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[13]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[13]/span[2]/p').text]
    player14 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[14]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[14]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[14]/span[2]/p').text]
    player15 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[15]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[15]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[15]/span[2]/p').text]
    player16 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[16]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[16]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[16]/span[2]/p').text]
    player17 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[17]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[17]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[17]/span[2]/p').text]
    player18 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[18]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[18]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[18]/span[2]/p').text]
    player19 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[19]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[19]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[19]/span[2]/p').text]
    player20 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[20]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[20]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[20]/span[2]/p').text]
    player21 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[21]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[21]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[21]/span[2]/p').text]
    player22 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[22]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[22]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[22]/span[2]/p').text]
    player23 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[23]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[23]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[23]/span[2]/p').text]
    player24 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[24]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[24]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[24]/span[2]/p').text]
    player25 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[25]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[25]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[25]/span[2]/p').text]
    player26 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[26]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[26]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[26]/span[2]/p').text]
    player27 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[27]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[27]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[27]/span[2]/p').text]
    player28 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[28]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[28]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[28]/span[2]/p').text]
    player29 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[29]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[29]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[29]/span[2]/p').text]
    player30 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[30]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[30]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[30]/span[2]/p').text]
    player31 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[31]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[31]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[31]/span[2]/p').text]
    player32 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[32]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[32]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[32]/span[2]/p').text]
    player33 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[33]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[33]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[33]/span[2]/p').text]
    player34 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[34]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[34]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[34]/span[2]/p').text]
    player35 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[35]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[35]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[35]/span[2]/p').text]
    player36 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[36]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[36]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[36]/span[2]/p').text]
    player37 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[37]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[37]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[37]/span[2]/p').text]
    player38 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[38]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[38]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[38]/span[2]/p').text]
    player39 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[39]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[39]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[39]/span[2]/p').text]
    player40 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[40]/h1').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[40]/span[1]/p').text,
        elem.find_element(By.XPATH,
                          '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[40]/span[2]/p').text]

    all_players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11,
                   player12, player13, player14, player15, player16, player17, player18, player19, player20, player21,
                   player22, player23, player24, player25, player26, player27, player28, player29, player30, player31,
                   player32, player33, player34, player35, player36, player37, player38, player39, player40]

    assert "No results found." not in driver.page_source
    driver.close()

    return all_players


if __name__ == '__main__':
    main()
