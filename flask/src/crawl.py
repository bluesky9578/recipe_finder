#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from codecs import open as codecopen
import re

#태그 번호(페이지)
page = 971
count = 932

#구글 드라이버 경로
driver = webdriver.Chrome('C:/Users/younh/Desktop/chromedriver_win32/chromedriver.exe')

#range = 횟수
for k in range(1,1070):
    #레시피 정보 저장파일
    f = codecopen('C:/Users/younh/Desktop/tmp/recipe_' + str(count) + '.txt', 'w', 'utf-8')
    #재료 저장 파일
    #g = codecopen('C:/Users/JSW/Desktop/recipe_data/ingredient/ingredient_' + str(count) + '.txt', 'w', 'utf-8')

    #사이트 주소
    driver.get('http://2bob.co.kr/recipe.php?id=view&eTheme=1&idx=' + str(page))

    driver.implicitly_wait(5)
    try:
        html = driver.page_source
    except:
        alter = driver.switch_to_alert()
        alter.accept()
        page = page + 1
    else:
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

        #요리 이름
        recipe_name = soup.select('#container > div > div > div.rec_view_top.clr > div.fr.rec_info > div.rec_exp > h2')
        #재료
        recipe_ingredient = soup.select('#container > div > div > div.rec_view_top.clr > div.fr.rec_info > div.rec_mate > div')
        #방법
        recipe_method = soup.select('#container > div > div > div.rec_content > ul > li > div > div.text_wrap.clr')
        #카테고리
        recipe_tema1 =  soup.select('#container > div > div.contain.tag_wrap > div.tag_area.on > ul > li.first.on > a > p')
        recipe_tema2 = soup.select('#container > div > div.contain.tag_wrap > div.tag_area > ul > li.on > a > p')
        recipe_tema3 = soup.select('#container > div > div.contain.tag_wrap > div.tag_area.on > ul > li.mtm1.firston > a > p')
        recipe_tema4 = soup.select('#container > div > div.contain.tag_wrap > div.tag_area > ul > li.mtm1.first.on > a > p')
        recipe_tema5 = soup.select('#container > div > div.contain.tag_wrap > div.tag_area.on > ul > li.mtm1.on > a > p')

        regex_tmp1 = re.compile(u'필수재료\\n')
        regex_tmp2 = re.compile(', \\n')
        regex_tmp3 = re.compile(',\\n')

        for i in recipe_name:
            print(i.text.strip())
            f.write(i.text.strip())
            f.write('\n')
            #g.write(i.text.strip())
            #g.write('\n\n')
        f.write('\n')
        print '\n'

        for i in recipe_tema1:
            print(i.text.strip())
            f.write(i.text.strip())
        for i in recipe_tema2:
            print(i.text.strip())
            f.write(i.text.strip())
        for i in recipe_tema3:
            print(i.text.strip())
            f.write(i.text.strip())
        for i in recipe_tema4:
            print(i.text.strip())
            f.write(i.text.strip())
        for i in recipe_tema5:
            print(i.text.strip())
            f.write(i.text.strip())
        print '\n\n'
        f.write('\n\n')

        for i in recipe_ingredient:
            print(i.text.strip())
            f.write(i.text.strip())
            f.write('\n\n')
        #f.write('\n')


        for i in recipe_ingredient[1:2]:
            k = i.text.strip()
            m = re.sub(regex_tmp1, '', k)
            m = re.sub(regex_tmp2, ', ', m)
            l = re.sub(regex_tmp3, ', ', m)
            #g.write(l)

        for i in recipe_method:
            print '\n'
            f.write('\n')
            print(i.text.strip())
            f.write(i.text.strip() + '\n')

        f.close()
        #g.close()

        page = page + 1
        count = count + 1

