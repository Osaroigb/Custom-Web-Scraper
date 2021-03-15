# import required modules
from selenium import webdriver
from time import sleep
import pandas

# setup selenium web driver
chrome_driver_path = "/Development/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

website_link = "https://www.nba.com/stats/alltime-leaders/"
driver.get(url=website_link)
sleep(3)

player_list = []
points_list = []
rebound_list = []
assist_list = []
steal_list = []
block_list = []

# scrape the top 50 players and their stats
for i in range(1, 51):

    player = driver.find_element_by_xpath(xpath=f"/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]"
                                                f"/div[1]/table/tbody/tr[{i}]/td[2]").text
    player_list.append(player)

    points = driver.find_element_by_xpath(xpath=f"/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]"
                                                f"/div[1]/table/tbody/tr[{i}]/td[5]").text
    points_list.append(points)

    rebound = driver.find_element_by_xpath(xpath=f"/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]"
                                                 f"/div[1]/table/tbody/tr[{i}]/td[17]").text
    rebound_list.append(rebound)

    assist = driver.find_element_by_xpath(xpath=f"/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]"
                                                f"/div[1]/table/tbody/tr[{i}]/td[18]").text
    assist_list.append(assist)

    steal = driver.find_element_by_xpath(xpath=f"/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]"
                                               f"/div[1]/table/tbody/tr[{i}]/td[19]").text
    steal_list.append(steal)

    block = driver.find_element_by_xpath(xpath=f"/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]"
                                               f"/div[1]/table/tbody/tr[{i}]/td[20]").text
    block_list.append(block)


# store the top players stats in a dictionary
stats_dict = {
    "Player": player_list,
    "Points": points_list,
    "Rebound": rebound_list,
    "Assist": assist_list,
    "Steal": steal_list,
    "Block": block_list
}

stats_df = pandas.DataFrame(stats_dict)  # create a Dataframe from the dictionary
stats_df.to_csv("all_time_leaders.csv")  # convert the Dataframe to csv and save it
