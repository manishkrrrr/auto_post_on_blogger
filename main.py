#from keep_alive import keep_alive
#from index import indexing

#from termios import B75
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
#twitter api
import tweepy
import pandas as pd
import requests

#from selenium import webdriver

#from selenium.webdriver.chrome.options import Options
import shutil
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

from io import BytesIO

print("done")

url = "https://i.pinimg.com/736x/0a/ec/da/0aecda71bc82e8f4e995211ae653781c.jpg"
#url = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAABWVBMVEX////+/v709PT29vb5+fnx8fH///3///z8/////f////r///j8/Pz6///9//3//vs9hvRbjevr6+u13r4tpVC13MArpU75uQCfwPFFhPfu9f7h9+fOz9Hb3N69vsDk5ORFrGJChvBqm+uoqav3vQD/uACys7XR0tS4ubvW6f16p+y60/qDrvDqQTTmRDbt+vznOCpDgvz/7end7vvlRjPidmjF3fibnJ6ErONRiOzx/fJSiuK/38hTrGtjtH6XuvGDpOVcleiBqu5ale+tyPb83Nnzs6zrjojle3b5pqL9+M/855/41nX3y2Hy0WT62oT/6L78++D7z8nwmpbdSTzwwyP4w8HvOij86LLx0VXqpJfwwRPvyTzhVk30nZzdYl/36JfajYT25dzsYGLzua7dUkP/5+zvyTX899jvenf94Kba9Nxklt/o5Pf00dTutGHzwKrKX1R8rXoUJCG8AAAPC0lEQVR4nO2d6UPbSJrGVbIllVSukvFkGuz4GGNifIAPTExMpochnIF0ujmCExI223Qyk+xkZ3fm//8wT+kAc3QHEjcWoX5csrAK1aO33qN0oGkKheILIYSMehcU3xzk9PtnFxUKhUJxGcpnXpVrCKM0VCgUn8UrjvwK6bOLd4Wr5/bXqQLuSsVwHYuKrPWRU278bysUCoVCoTgDuZQrbWlbFtVMGmRahGq2Roe1V6agQhAxpOZuDJOYRDiWyZsS5jBG0YnhJDzElkfGFrctfTKJ7YhO/dFYr5hMjtUmqoIR1xxS27ZYXFy87962nJJoojrzOJlOStLJYrHW5aY5JDvR/vz999//ZXEojX3R3z/5fvX6y3ZMK7PUS0s1kum0/1l81GHD0uSP33333Z/u3yo7YbZVnYRxJJPFtqdK25NlrMuG0rzU5N5t04Ra1bF0uwgrWZ6od7v1iVpPjp/2X/lQPEpoJ7dqzsCpJnswj2KtygUiDmNOByOpXWs6Qzm0J5rcFmzH1jLL0rc+rnMWpjSOWV3+1GTDSSlunZ0gCItHRd97MDtcS1wn02SmM5Q/cQs1caqQJPm467g2CUVA2qk5zpD6cOs0IQ57InOSCeaQUxUIMRl1zNDFEkrliKJUUMJJaE1cvstCAiw/BTX9txPTMoUQKBUoZcIUDuT9Q6gJ1fx2CJXVQ1Q1IqzTSxbTKxnGf30XMcAI51RD7k+JE3oZKOJolDtMcMFPvDFkg7gSjEWbIa+3tT/cC3ysaQnBZV3FOSdDGprDx9FWZUqyatqaPMz+nPLZCpLIoyrW1jc2Nzeerrny+HrrbUGdre1nP/zw/MefdpgINhXSF3WXarWlesaKVzvVjgg1QbLMeXz36ebm5t5ujP/GQRgtFp2BJr2qJk5ykcs02d3Yb7VmW/h6uOsGjiFBt569GH8wDqb+vr0DBySbsFlmdbmYBsnlerfYSy5nTjQhwj34ON+SNN4eRHbsWLFlmMlk07I8TUyMDfMES2MIQbbmrO+3ZhuzHv3G3hyHiaCOfvkCakhFxqceTL3aoqgjCcbipFcwpZESpyfhvscygT8hwmaHjdYsWmpAmP1DRyORLJbNzBj2vSYC90oEr0+csjRR5y4nh9Bivo/ewE4ardaGDWdA+PZrqPFgakp+gzJvdjRGbaeznPYEgYUUsRBqcu9P9y0uNhpeA2gG4s4eUntIZeZwMTOo/dIzLAw5rLniF8ce7fRYk/CD/jz6cLTx7uC/3vax1FoX1HW2Xj+AIK+fb2//+Gocwoy/YljNH6FYahdrq93VSdRNyQFNqHbgGdrb9bXdvf3W/HxrTbOHNB8xVKAJdvxJGIYtcqqJ9AnFXtOeO5pvNWY35jiiBVtvYLmxxu3FH6QQb7YQQai7/Vqayn8LwVaT7V77cddE1HG6vXRxQBMtdiTt7SnjXONrv8Bk3rqRHDtOcwy9r8lcQx4y4TbH2ukQ9KjY1N7B3vs/xxEn4BVNOY76G4y/lL71zQeK5BdO+OVrjKA3zG6iTEj3qozIxsxuMbCTe6iLF6nX0B51kLOItY+zEPeA25/bwRFgxifR9eVMYMPCbM5MhozJHjXdTYz+o2NqWzIx4XN42fpljv8IM5l6qVHPIxD2bHz8weuftC5KyeSEcC0Lax06M6DJfW0TKhzNUS70g839Bvxs/+dIpijUWpJHtmta3kv4ziZGA4/H483mkoynfG4fHmSPct+QCF2XkWONwYeMv2HC9QIwo1tTiD3bJjYpFjtIdnylusUBTdyjfgMNOcdPf2nNz7b6s0eHa5EcOyarw8DTS6ZL/ZzNS81lnk6EDKpPtOMGovA7LZh3J3ytMTvfOth5gQD8nBE/yRDOzgs4lGdiBpqsNAlSfqylotMb0GTuPSxsfW1zvz/fmG3tP3w3p/Fojh0ZjIvpsQ4zz4UAtyP97Kq2KxOTg3CtTY/x2tdk/JlL/I0sZ+cNHMpz8QRDZ/IksLPm2KAm+435xvtGa77R6r/fW3Mjm8c6NltCItGuCXdgrUxf2YycZ6qKNdhJ6114sofQf3oaQYOp8edhBCfUtxMOTdor3PGVIs5ZO5GDEClOf/btujQR7ka0UkbhmnncLiaLE5o1sIcIQ10kXW0EpLn30p/YQZEnhO9PFl/Bxb7ZCdYmnC2Zu23TCWQnvU6giSNd7qkm7Gh2HonO/sYuo8iEXZdGdYbWJGa9LfPN1UWSEAIVDvwJdc3OY0hS7KK2fQhNjo65LHtQ5LqbfRk9ZNwZH3+JKpkLIRxHvkQY6sqp7lXhEmJZxGIncUfm9nxTJrF7xxY8OYoDjiowsiUPSSD3LLbTMx1mC9+/arzupSePOGFcGsYsMhLimpSKw9nWfP9nSn+CBihyiG3ChPjL14jFMJsMMr704yrjsvhB0lYc0ITuSk02KXUZoZQfvN1Fe6Pu/K/BmrJWK6Z7Sx0bYYeJTBdJS9GbVbEZ/duR9AMbSCyQsT5tIKAij3UQjBF5Xm0hK+XspZfHbnPXWUVL7ZWqhTTW6T5OD2pis7ey0tljMiF2371vNQ7nIutnE26z5p/w6q3UZmZmoJCs3tIrHQwj2+EHsihuHR0eHDx96y0easzmW1NSh6nn2y+3f5ALqHdMwfintByIM/VuvVZMJwf9iaAI47Khp7u76w9RL7T67yLqZeELiZaZ6MnaHs7WOzeahFdI1zomkdOFNsV4kaWfV9DCS27GuWuZVBqHrP3kbAF+/v0Dd+CMOsttaXPpdLvttYJMOMxjqbsOK/PbkQ21Nlw7qlcbID+zRPcTXIqsfdLyfGC63ZsIzmUgeXcP9/tSDBzl+f7s3hyXXkcjL194E0pSEzl/YjMZbpzOZNuvIeGiJ3u+JqgBv7+PzI69Q0MNbyam4Y2iSNbFPhgjThPGLu1EnhYtrix1kKOGO8zJ2sd9HNs+Du/HAxpMUzP7w/PXU56RTL3ZZtQ/Q2Y7zQnPO7VRHtcxCjF2/njvHupiYiHQHG96htKXE3a2HcUs1gcJvWk6piM63aUntcnJpdVqRk63hsUIFbbG5Hzsw43DtbgU0IsXcL9s53+evXrz6tlPO1i2TRc1pMVM15uPfVRvavUeNGnai/+4f/++Laf3KUkco6GPm7IhLie0R9rzK8GYECyYhzwLNV388nzspBTxxSJBkmZqtp1gnNlyMlowk616VWTQWth903EuNhRhkJSBy/JLQjlFj8+/XSBnY+FFGcj4mOjUO5YN/SyR4E/ayfaj81tw2ZBt35o7HnDQ5Wl06+JvqJfgngsT0MBxHdcN60eLd2d6ySdNeVoHeWxVXp3QPdd3JK9yUim6zvVSLj2A9OT8zyBBzwJNiHAftRHQl7iDpM3sINFJj2Uu9N4U38C9GlfF5azzuA2/OlnvdKqrPRSEyQknknNpN4aFkF6X+Xw72esl2zIZXs5E8nTFzUFdQlm9J3M+WR/DTD4hzbnbmkhcVq31vKsE0ygq77qV+CDg8O7S5MrKZG21Iy4JYHcQpKYmE7yZyQjEnuimZjd5L6NtWrKKsSzNpJREt6AZPZffHTFURt1FhUJxQyh/olAoFArF3UFFZYVCoVAoFAqFQqFQKBQKheI6/Nqprhs4wxZpLiqS0A1Dv7ug84lzsiQMI3FRp7sESUCVwVnpuBEf3d5EAxgJVDjVJG7cnln739OhECMROpaEcYuuL/gdNQFGqIl+hwcOEQ7jViK4C16L6/7PhD66XRo5RFjdTxP85NlpuhdqSCw0k0I+awTvvPmdGxGEmE/avfBhroTEY97P0MEWyqlcOTayvRsFprwzSmpCgoe5EuINGl8T09TyKU3L5ka4hzePJe8um0n3OiK8JNlXg3jjRWoCPbKF0e3gCDBN58NOrd373+OTy7QDTXw7IXopmy+lRreDI8B1rO1n3d7MPzdPHoSsD2iCb/FcIRWIEjxeUDv5xzdE+xY9L9HsD//3/39be7h+ssa3E32w0klVonsDxO8B4ccb/3p4sBjeshkkJvEzsSZ+5h7eb+n/Rl0KEWTx3/+gdvhsnyAxIWernfNPQ/q2IYyIPzcdhwcvQy2Q0H6bRnA15ANbQzsIyxyi6XcrU7tAWAKTmH5aDRuxu2woWhhdY2e8SOyOTypJLeKwjDOmkdCNWPwuEzPgS8g5nVAS3mXit2heTaFQKBQKhUKhUCiGz+n/qx9cjCjkOk/w+fJH/JyeyhhcvJTEV5SjXgNfW5PHyeV7+4WLQ4DEdP3L+qL7J1ISV9/80qvRYnrkJgrJV1xc583vxb+igYCoaZJQmlxAaXKRU01ihn7JiI8ZxuV+4Dc0Ma55uW5kNTHy5XJBOsKY73XzhrcwXS7l/LX+aj1/qtygJrFUfjoX9z1pvlTOBttkc9PxYOtYPuV5VLwo+L8OZY+iJjiuRiyf1wvZVD5r5Co5I5/PlVPZfCpmlHKprCHX5qfR6+l8rpTPehvg24km8mWqVChk83iDrpcKul7IT+tooJLDNlksZY0YVqdy+jRaw7um5VLUNSmlCvlsZTpbKRVK+Xy2XM7iw9BzpVIuD7K5hWxpupzLlnKlVGBZZ8ZOqhRPLeQWciVoUirnSln5Ua6gvWk0lFvQ46VCrFDRoel0tlQu4CNoJpKaeAerMm3kFkpGrlS2K6VcoVLOQxrdyOqFkqdRfiGbzeVj6HO5MDB2yKAm5VTJKMVgJ0ZqIZtHA1loUk5BUr2kw07ihUoMchjTCyUMsFwssnZieKBPlVJ+ulzOlfM4hOVyBQt5+IZyGWsrOObQxChV8mWjkgq28TUJty/HUpVU2cDRh2gYfZ69YTBVUhiIlQU9hjanS9JsyvlsNltYMAIi6GPDPTMKGBP4MgqGHC0pPVWQqwvSOcATFFIpb1UKH8ZFTQy5OuX/NuVtFzSQwiq4qbJupArYGqsL3tuyeT2ymhgneHd9+F/TWWjjO5pgjR9j5cLpBr4/MS4QbqeHNqj77Z15U/ZE2ihrMtirIM34bX5Nkys1d/r6lmhyNa6syW8TOU3I6DW5kbhzrYmFMG4YxucHy/m++NdeXne7c+g3cpfadTQhX35Xjeb//+uv5SYUUSgUwyScCCZXWFQoFAqFQqFQKBQKhUKhUCgUitvEUK+D/d2ujr1Zhnq99B15eIdCoVBEiP8AyuPiIL0UJgIAAAAASUVORK5CYII="
r = requests.head(url)
import requests
if r.status_code==200:

    #r = requests.head(url)
    print("r.status_code")
    #r.status_code == requests.codes.ok
else:
    print("not")



time.sleep(100)
from PIL import Image
def is_jpg(filename):
    try:
        i=Image.open(filename)
        i.format =='JPEG'
        print("yah")
    except IOError:
        
        print("false")
is_jpg("https://i.pinimg.com/736x/0a/ec/da/0aecda71bc82e8f4e995211ae653781c.jpg")
print("wait")
time.sleep (100)

#keep_alive()

while True:

    api_key = "YP1G7gyfkvnhEgdYwCMqTsFVz"
    key_secert = "DtBGutN1dAOxhiipnwIFIOdS1MLAM2UMdgv8aw04vg7Wjlrcxu"
    token = "AAAAAAAAAAAAAAAAAAAAAAWpggEAAAAAHcIbtTtv5TTqNLNlCzEzUMQe90o%3DguXXQTJ7qDzwGKHzQAVS5yi12zn9wXRYM67RlU0eanZGlLUUXo"
    acess_token = "1565887186901372928-dEL2THzs4Ctd00Yf5bpLEzmAhB1A7P"
    access_token_secert = "GuudXjlwJ2YoLwPT5Xs055XyeJB3ao39Jyn0mlPns2feH"

    auth = tweepy.OAuthHandler(api_key, key_secert)
    auth.set_access_token(acess_token, access_token_secert)
    api = tweepy.API(auth)

    #get trending hashtag from twitter
    trend_hashtag = api.get_place_trends(23424848)
    hashtag = []
    for i in range(0, 3):
        hashtag.append(trend_hashtag[0]['trends'][i])

    signal_hashtag = hashtag[0]["name"]

    print(signal_hashtag)

    topic = signal_hashtag.replace("#", " ")
    print(topic)

    #get trending tweet from trending hashtag
    tweet = tweepy.Cursor(api.search_tweets,
                          q=signal_hashtag,
                          tweet_mode="extended").items(6)
    tweet_box = []
    col = ["tweet"]
    row = ["1", "2", "3", "4", "5", "6"]
    for item in tweet:
        tweet_box.append(item.full_text)

    #print(tweet_box)

    #create the datafram
    df = pd.DataFrame(tweet_box, index=row, columns=col)
    pd.set_option('display.max_colwidth', None)
    #print(df)

    #get signal tweet
    h1 = df.loc['1', 'tweet']
    print(h1)

    h2 = df.loc['2', 'tweet']

    print(h2)


    h3 = df.loc['3', 'tweet']
    print(h3)

    h4 = df.loc['4', 'tweet']
    print(h4)

    h5 = df.loc['5', 'tweet']
    print(h5)

    h6 = df.loc['6', 'tweet']
    print(h6)

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--lang=hi')
    driver = webdriver.Chrome(options=chrome_options)

    ###########################                    ##########################
    ###########                SEARCH REALTED IMAGE           ###############
    ###########################                    ##########################

    print("start searching  image")
    try:
        driver.get("https://www.google.com/")
        time.sleep(4)
        driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
        ).click()
        driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
        ).send_keys(topic)
        time.sleep(5)

        driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
        ).send_keys(Keys.ENTER)

        #click on the image section
        driver.find_element(by=By.LINK_TEXT, value="Images").click()
        time.sleep(4)
        #click on first image show on google
        driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img"
        ).click()
        #click on first image
        first_image = driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img"
        )
        time.sleep(4)
        src1 = first_image.get_attribute('src')
        print(src1)
        #get first image heading
        heading = driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[3]/div[1]/a[1]/h1"
        ).text
        print(heading)

        hd = heading.split()[:5]
        short_heading = " ".join(hd)
        time.sleep(3)

        #click on second image and get image link
        driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[2]/a[1]/div[1]/img"
        ).click()
        time.sleep(5)
        click_2_image = driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img"
        )
        src2 = click_2_image.get_attribute('src')
        print(src2)
        time.sleep(4)
        #click on second image and get image link
        driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[3]/a[1]/div[1]/img"
        ).click()
        time.sleep(4)
        click_3_image = driver.find_element(
            by=By.XPATH,
            value=
            "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img"
        )
        src3 = click_3_image.get_attribute('src')
        print(src3)
        time.sleep(4)

        time.sleep(4)
        #src = first_image.get_attribute('src')
        #print(src)

        #download image
        url = src1
        response = requests.get(url, stream=True)

        with open("img.png", "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)

        del response
        time.sleep(3)

    except:
        pass
    print("image is not search well")



    #########################################get image scource link######################################################################

    try:

        #for first image
        driver.get("https://postimages.org/web")
        time.sleep(5)
        driver.find_element(by=By.NAME, value="links").send_keys(src1)
        time.sleep(8)
        driver.find_element(by=By.CLASS_NAME, value="width100.btn.btn-lg").click()

        time.sleep(15)
        copy_image_link1 = driver.find_element(by=By.ID, value="code_direct")
        copy_image_src1 = copy_image_link1.get_attribute("value")
        print(copy_image_src1)
        time.sleep(4)

        #so sencond image
        driver.get("https://postimages.org/web")
        time.sleep(5)
        driver.find_element(by=By.NAME, value="links").send_keys(src2)
        time.sleep(8)
        driver.find_element(by=By.CLASS_NAME, value="width100.btn.btn-lg").click()
        time.sleep(15)
        copy_image_link2 = driver.find_element(by=By.ID, value="code_direct")
        copy_image_src2 = copy_image_link2.get_attribute("value")
        print(copy_image_src2)

        #for third image

        driver.get("https://postimages.org/web")
        time.sleep(5)
        driver.find_element(by=By.NAME, value="links").send_keys(src3)
        time.sleep(8)
        driver.find_element(by=By.CLASS_NAME, value="width100.btn.btn-lg").click()
        time.sleep(15)
        copy_image_link3 = driver.find_element(by=By.ID, value="code_direct")
        copy_image_src3 = copy_image_link3.get_attribute("value")
        print(copy_image_src3)
    except:
        pass
        print("there is problem in postimage url link")


    ###########################                    ##########################
    ###########                post on blogger           ###############
    ###########################                    ##########################


    print("start posting on blogger")

    #Enter your client id and client secert code
    auth = (
        "105088908205-iat5t5e0avt00c72ik48h6np5vikeahp.apps.googleusercontent.com",
        "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")

    #enter refersh token  to get new access token in parameter
    params = {
        "grant_type":
        "refresh_token",
        "refresh_token":
        "1//04YkcuTWoNxpOCgYIARAAGAQSNwF-L9Irm4j_Q15d5nRe57cZkHwc15ydHsgolMrJu7lWQPdb1GShZ_cS-LRXRyzwP26Xa8qpi3Q"
    }
    url = "https://oauth2.googleapis.com/token"

    #Request to get new access token
    response_access_token = requests.post(url, auth=auth, data=params)
    response_access_token.status_code
    get_access_token = response_access_token.json()

    #now you have new access token
    access_token = get_access_token["access_token"]
    access_token1 = "Bearer" + " " + access_token
    print(access_token1)
    #now you have acess token and you can apply for request new post in blogger

    #Enter your acess token in header data
    headers = {

        #'Authorization': 'Bearer 4/0AdQt8qjRcWYI_s5h-2zMDjnucvi80Yexm8UQNiHcS1gpbt89H8XQ3aWsMsuc8pyx7Z5FWw',
        'Authorization': access_token1,
        'Accept': 'application/json'
    }
    #abbbb = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg"

    html = f"  <h1 style='text-align: left;'> <span style='font-size: x-large;'> {heading} <a href='https://apnavicharr4.blogspot.com/'><b>Apna Vichar</b></a> </span> </h1> <br/> <br> <h2  style='text-align: left;'> <span style='font-size: large; '> {heading} </span> </h2>  <br>       <div class='separator' style='clear: both; text-align: center;'><a role='link' tabindex='0' rel='noopener' target= '_blank' href='https://apnavicharr4.blogspot.com/' aria-label='Visit Apna Vichar' style='margin-left: 1em; margin-right: 1em;'><img alt='{heading}' data-original-height='518' data-original-width='720' height='317' src='{copy_image_src1}' width='441' /></a></div> <br>         <h3 style='text-align: left; line-height:1.4; font-family: LocalFont;'><strong><span style='color: red;'> {h1} </span></strong></h3> <br> <h4>  <p style='line-height:1.4;  font-family: LocalFont; font-size: large;'> <b> {h2} </b> </p> </h4> <br>              <div class='separator' style='clear: both; text-align: center;'><a role='link' tabindex='0' rel='noopener' target= '_blank' href='https://apnavicharr4.blogspot.com/' aria-label='Visit Apna Vichar' style='margin-left: 1em; margin-right: 1em;'><img alt='{short_heading}' data-original-height='518' data-original-width='720' height='317' src='{copy_image_src2}' width='441' /></a></div>          <h2>  <p style='line-height:1.4;  font-family: LocalFont; '>  {h3}  </p> <h5> <br>     <p style='line-height:1.4;  font-family: LocalFont; font-size: medium;'>  {h4}  </p> <br>            <div class='separator' style='clear: both; text-align: center;'><a role='link' tabindex='0' rel='noopener' target= '_blank' href='https://apnavicharr4.blogspot.com/' aria-label='Visit Apna Vichar' style='margin-left: 1em; margin-right: 1em;'><img alt='{heading}' data-original-height='518' data-original-width='720' height='317' src='{copy_image_src3}' width='441' /></a></div>   <br>   <h2>   <p style='line-height:1.4;  font-family: LocalFont; font-size: large;'>   {h5}  </p> </h2> <br>   <p style='line-height:1.4;  font-family: LocalFont; font-size: medium;'>   {h6}  </p> <br>     "

    #hello = "<img src=""imageset.png"" >"

    #now enter the data you want to send on blogger site
    json_data = {
        "kind": "blogger#post",
        "blog": {
            "id": "6524067515348267014"
        },
        "title": short_heading,
        "content": html,
        "customMetaData": heading,
        "labels": ["hindi news", "news", topic]
    }

    #request to post your artical on blogger
    response_for_actical = requests.post(
        'https://blogger.googleapis.com/v3/blogs/6524067515348267014/posts?key=AIzaSyD7Oj2rzuvEcdb-WboglkW2ddXRKBlxnkY',
        headers=headers,
        json=json_data)
    print(response_for_actical)
    print("article is posted")
    time.sleep(200)

    print("indexing started")
    #indexing()
    print("indexing of atical is done")

    sitemap = "https://apnavicharr4.blogspot.com/sitemap.xml"
    request = requests.get(sitemap)
    soup = BeautifulSoup(request.text, 'xml')
    tag = soup.find('loc')
    blog_link_name = tag.text

    print(blog_link_name)



        
    ########################################################################
    ############################### POST ON FACEBOOK #######################
    ########################################################################
    #go to fb login page
    driver.get("https://www.facebook.com/")

    username = "8084180991"
    password = "apnavicha@@44"


    try:
        driver.find_element(by=By.XPATH, value= "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys(username)
        time.sleep(3)
        driver.find_element(by=By.XPATH, value= "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys(password)
        time.sleep(3)
        driver.find_element(by= By.NAME , value= "login").click()
        time.sleep(100)
    except :
        pass
        print("already fb is login")



    #find group and post
    group_number = [ 221936475950872 , 666954713881407,6933884136686993, 429549381873491, 3235098549834585, 130864450301482, 1522314447852409 ,"BIHAREXPRESSNEWSHINDI", "dehradunnews", "dehardun1", ]
    facebook_content = heading + " \n" + "Read Full Aticle" + "\n" + blog_link_name
    for group in group_number:
        driver.get(f"https://www.facebook.com/groups/{group}")
        time.sleep(9)

        try:

            #click to write on group
            driver.find_element(by=By.XPATH , value= "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span").click()
            time.sleep(10)

            #content want to post on fb group
            driver.find_element(by=By.XPATH , value= "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys(facebook_content)
            time.sleep(10)

            #post on group
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]").click()
            time.sleep(10)

        except:
            pass
            print("unable to post on fb group because there is problem to click")



    #############################create pin on pintrast#####################################
    # Your Pinterest account details

    user_name = "nifac39383@ulforex.com"
    user_password = "Apna@@00"

    # Definitions about pins
    pin_image_file = "/home/runner/demo/img.png"
    pin_description_upload = h1
    pin_image_link = blog_link_name
    pin_tittle = heading
    alt_text= short_heading

    #go to login page
    driver.get("https://in.pinterest.com/login/")
    time.sleep(5)


    try:

        # Log in
        user = driver.find_element(by=By.NAME, value="id")
        #user = driver.find_element(by = By.XPATH, value = "/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[3]/form/div[2]/fieldset/span/div/input")
        user.send_keys(user_name)
        time.sleep(3)
        pas = driver.find_element(by=By.NAME, value="password")
        #pas = driver.find_element(by = By.XPATH , value = "/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[3]/form/div[4]/fieldset/span/div/input")
        pas.send_keys(user_password)
        time.sleep(2)
        driver.find_element(by=By.XPATH, value=login_button).click()
        time.sleep(10)
        print("login in pinterest")
    except:
        pass
        print("unable to login in pinterest")


    try:
        #go to pin builder
        driver.get("https://in.pinterest.com/pin-builder/")
        time.sleep(10)

        #enter tittle of pin image
        #driver.find_element(by=By.XPATH, value="//*[starts-with(@id, 'pin-draft-title-')]")
        driver.find_element(by=By.XPATH, value="//*[@id='pin-draft-title-f681c11c-b071-41d6-a691-85d7cac587c9']").send_keys(pin_tittle)
        time.sleep(10)

        #enter description
        driver.find_element(by=By.XPATH, value= '//*[@id="pin-draft-description-f681c11c-b071-41d6-a691-85d7cac587c9"]/div/div[1]/div/div[2]/div/div/div/div').send_keys(pin_description)
        time.sleep(10)

        #click on alt 
        driver.find_element(by=By.XPATH, value='//*[@id="__PWS_ROOT__"]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[4]/div/button/div/div').click()
        #enter alt for image
        driver.find_element(by=By.XPATH, value='//*[@id="pin-draft-alttext-f681c11c-b071-41d6-a691-85d7cac587c9"]').send_keys(alt_text)

        #add external link
        driver.find_element(by=By.XPATH, value='//*[@id="pin-draft-link-f681c11c-b071-41d6-a691-85d7cac587c9"]').send_keys(pin_image_link)

        #add image
        driver.find_element(by=By.XPATH, value='//*[@id="media-upload-input-f681c11c-b071-41d6-a691-85d7cac587c9"]').send_keys(pin_image_file)

        #click on publish
        driver.find_element(by=By.XPATH, value='//*[@id="__PWS_ROOT__"]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]/div').click()
        print("posted on pinterest")
    except:
        pass
    print("Unable to post on pinterest")

    time.sleep(3000)
















    #############################create pin on pintrast#####################################
    # Your Pinterest account details

    user_name = "nifac39383@ulforex.com"
    user_password = "Apna@@00"

    # Definitions about pins
    pin_image_file = "/home/runner/demo/img.png"
    pin_description_upload = h1
    pin_image_link = blog_link_name
    pin_tittle = heading

    # Definitions for Selenium, don't change them
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--lang=hi')
    driver = webdriver.Chrome(options=chrome_options)

    pinterest_home = "https://in.pinterest.com/"
    pre_login_button = '/html/body/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div'

    login_button = "//button[@type='submit']"
    pin_builder = "https://www.pinterest.com/pin-builder/"
    pin_name = "//*[starts-with(@id, 'pin-draft-title-')]"
    pin_description = "//*[starts-with(@id, 'pin-draft-description-')]/div/div/div/div/div/div/div"
    image_input = "//*[starts-with(@id, 'media-upload-input-')]"
    pin_link = "//*[starts-with(@id, 'pin-draft-link-')]"
    drop_down_menu = "//button[@data-test-id='board-dropdown-select-button']"
    publish_button = "//button[@data-test-id='board-dropdown-save-button']"

    #publish_button = "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]/div"
    time.sleep(6)

    #go to login page
    driver.get("https://in.pinterest.com/login/")
    time.sleep(5)

    # Log in
    user = driver.find_element(by=By.NAME, value="id")
    #user = driver.find_element(by = By.XPATH, value = "/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[3]/form/div[2]/fieldset/span/div/input")
    user.send_keys(user_name)
    time.sleep(3)
    pas = driver.find_element(by=By.NAME, value="password")
    #pas = driver.find_element(by = By.XPATH , value = "/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[3]/form/div[4]/fieldset/span/div/input")
    pas.send_keys(user_password)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=login_button).click()
    time.sleep(10)

    print("loged in pin")

    # Go pin builder page
    driver.get(pin_builder)
    time.sleep(10)

    # Enter tittle of  pin
    driver.find_element(by=By.XPATH, value=pin_name).send_keys(pin_tittle)
    time.sleep(5)

    # Enter description
    driver.find_element(
        by=By.XPATH, value=pin_description).send_keys(pin_description_upload)
    time.sleep(5)

    # Click the upload button
    img_pinss = driver.find_element(by=By.XPATH, value=image_input)
    img_pinss.send_keys(pin_image_file)
    time.sleep(15)
    # Enter link
    driver.find_element(
        by=By.XPATH,
        value=
        "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/textarea"
    ).send_keys(pin_image_link)
    time.sleep(5)

    #menu
    #driver.find_element(by= By.XPATH, value= drop_down_menu).click()

  ## Select board
    #driver.find_element(by= By , value= board ).click()
    time.sleep(5)

    #alt text 
    driver.find_element(by=By.XPATH, value= "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[4]/div/button/div/div").click()

    driver.find_element(by= By.XPATH, value= "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div[1]/textarea").send_keys(short_heading)
    driver.get_screenshot_as_png()
    driver.save_screenshot("img.png")
    # Click publish button
    driver.find_element(by=By.XPATH, value=publish_button).click()
    print("pin is uploaded on pintrest ")
    time.sleep(155)


      
    time.sleep(30000)

