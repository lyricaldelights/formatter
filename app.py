#!/usr/bin/env python
# coding: utf-8


#!pip install langdetect
#!pip install selenium
#!pip install webdriver-manager
#!pip install more_itertools
#!pip install streamlit

import streamlit as st
import sys
import io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
from langdetect import detect
import more_itertools as mit
from itertools import groupby
from selenium.webdriver.chrome.options import Options

old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout


st.title('Lyrical Delights: Upload your translations')

txt = st.text_area('Put your translations here in the format we all agreed', placeholder='''
<songname>
Minnale nee vanthathenadi 
</songname>

<desc>
Here is a fact! This album came out in 1994. My parents haven’t even met then. If you have not yet listened, please drop whatever you are doing and give this a listen. This song is to reflect the pain of the guy who had to face a separation from his loved one after learning she is ill from her father. Also, you can follow the translation if you don’t follow the lyrics! Thank me later.
</desc>

<youtube>
https://www.youtube.com/watch?v=6bq8FURdGVk
</youtube>

<meta>
Movie: May Madham
Music: AR Rahman
Singer: SPB
Lyricist: Vairamuthu
</meta>

<song>
மின்னலே என் வானம் உன்னைத் தேடுதே
My sky is searching lightning (His heart longs for her)
 
கண் விழித்துப் பார்த்தபோது கலைந்த வண்ணமே
Like the dissolved colors when I opened my eyes
உன் கைரேகை ஒன்று மட்டும் நினைவுச் சின்னமே
Your fingerprints (her touch) are the only memory
 
கண் விழித்துப் பார்த்தபோது கலைந்த வண்ணமே
Like the dissolved colors when I opened my eyes
உன் கைரேகை ஒன்று மட்டும் நினைவுச் சின்னமே
Your fingerprints (her touch) are the only memory
 
கதறிக் கதறி எனது உள்ளம் உடைந்து போனதே
My heart hooted and hooted for you and got broken.
 
இன்று சிதறிப் போன சில்லில் எல்லாம் உனது பிம்பமே
Today, the scattered remains of the chiseled out stones show your image.
 
கண்ணீரில் தீ வளர்த்து காத்திருக்கிறேன்
I am waiting with fire grown in my tears
 
உன் காலடித் தடத்தில் நான் பூத்திருக்கிறேன்
I flower in your footsteps.
 
மின்னலே நீ வந்ததேனடி
என் கண்ணிலே ஒரு காயமென்னடி
You (she) lightning. Why did you come?
And wound my eye.
 
என் வானிலே நீ மறைந்துப் போன மாயமென்னடி
What is the magic in your disappearance in my sky?
(She is the lightening; he is the sky metaphorically)
 
சில நாழிகை நீ வந்து போனது
A few seconds you came and went
 
என் மாளிகை அது வெந்து போனது
My palace has burnt down.
 
மின்னலே என் வானம் உன்னைத் தேடுதே
My sky is searching lightning (His heart longs for her)
 
மின்னலே நீ வந்ததேனடி
என் கண்ணிலே ஒரு காயமென்னடி
You (she) lightning. Why did you come?
And wound my eye.
 
என் வானிலே நீ மறைந்துப் போன மாயமென்னடி
What is the magic in your disappearance in my sky?
(She is the lightening; he is the sky metaphorically)
 
சில நாழிகை நீ வந்து போனது
A few seconds you came and went
 
என் மாளிகை அது வெந்து போனது
My palace has burnt down.
 
மின்னலே என் வானம் உன்னைத் தேடுதே
My sky is searching lightning (His heart longs for her)
 
பால் மழைக்குக் காத்திருக்கும் பூமியில்லையா?
Doesn’t land wait for the gentle rain?
 
ஒரு பண்டிகைக்குக் காத்திருக்கும் சாமியில்லையா?
Isn’t there God waiting for his festivals?
 
பால் மழைக்குக் காத்திருக்கும் பூமியில்லையா?
Doesn’t land wait for the gentle rain?
 
ஒரு பண்டிகைக்குக் காத்திருக்கும் சாமியில்லையா?
Isn’t there God waiting for his festivals?
 
வார்த்தை வரக் காத்திருக்கும் கவிஞனில்லையா?
Isn’t there a poet waiting for his words?
 
நான் காத்திருந்தால் காதலின்னும் நீளுமில்லையா
Doesn’t my waiting (for you) increase our love?
 
கண்ணீரில் தீ வளர்த்து காத்திருக்கிறேன்
I am waiting with fire grown in my tears
 
உன் காலடித் தடத்தில் நான் பூத்திருக்கிறேன்
I flower in your footsteps.
 
மின்னலே நீ வந்ததேனடி
என் கண்ணிலே ஒரு காயமென்னடி
You (she) lightning. Why did you come?
And wound my eye.
 
என் வானிலே நீ மறைந்துப் போன மாயமென்னடி
What is the magic in your disappearance in my sky?
(She is the lightening; he is the sky metaphorically)
 
சில நாழிகை நீ வந்து போனது
A few seconds you came and went
 
என் மாளிகை அது வெந்து போனது
My palace has burnt down.
 
மின்னலே என் வானம் உன்னைத் தேடுதே
My sky is searching lightning (His heart longs for her)

</song>

	 ''', height=500)

def split_condition(x):
	return x in {'</songname>', '</desc>', '</meta>','</song>', '</youtube>'}


def send_to_olingoa(text):
	options = Options()
	options.headless = True
	username = "ttamilthathuvam2@gmail.com"
	password = "test12345!"
	site = "https://karky.in/karefo/labs/olingoa/olingoa.html"
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
	driver.get(site)
	time.sleep(2)
	driver.find_element_by_id("mail").send_keys(username)
	driver.find_element_by_id("password").send_keys(password)
	driver.find_element_by_id("newbut").click()
	time.sleep(2)
	select = Select(driver.find_element_by_id("sLang"))
	select.select_by_visible_text('Tamil')
	driver.find_element_by_id('one').clear()
	driver.find_element_by_id('one').send_keys(text)
	select2 = Select(driver.find_element_by_id("tLang"))
	select2.select_by_visible_text('Tamil')
	select2.select_by_visible_text('Olingoa')
	time.sleep(5)
	val = driver.find_element_by_name('two').get_attribute('value')
	driver.close()
	return val


if st.button('Convert format'):
	with st.spinner('Doing formatting magic.. please wait'):
		try:
			initial_lines=txt.splitlines()
			initial_lines = list(filter(None, filter(lambda name: name.strip(), initial_lines)))
			grouper = groupby(initial_lines, key=split_condition)
			res = dict(enumerate((list(j) for i, j in grouper if not i), 1))
			
			lines=[]
			for i in res:
				if '<song>'in res[i][0]:
					print('here')
					lines=res[i][1:]
				elif '<youtube>'in res[i][0]:
					print('<br>'.join(res[i][1:]))
					print('<br>')
				elif '<desc>'in res[i][0]:
					print('<br>'.join(res[i][1:]))
					print('<br>')
				elif '<meta>'in res[i][0]:
					print('<br>'.join(res[i][1:]))
					print('<br>')

			language_=[]
			for i in lines:
				try: 
					language = detect(i.strip())
				except:
					language = 'unknown'
				language_.append(language)

			final =[]
			for index, item in enumerate(language_):
				if item == 'ta':
					final.append(index)

			time.sleep(5)
			tamil_transliteration = send_to_olingoa('\n'.join([lines[i] for i in final])).split('\n')

			groups = [list(group) for group in mit.consecutive_groups(final)]

			def placement(text, lan):
				if lan=='en':
					return '<p><span class="has-inline-color has-vivid-cyan-blue-color">'+text+'</span></p>'
				elif lan=='ta':
					return '<blockquote class="wp-block-quote"><p>'+text+'</p></blockquote>'
				elif lan=='emp':
					return '<p><em>'+text+'</em></p>'

			from itertools import groupby
			count=0
			for i in [list(y) for x, y in groupby(language_)]:
				if len(i)==1:
					if i[0]=='en':
						print(placement(lines[count],'en'))
					elif i[0] == 'ta':
						print(placement(lines[count],'ta'))
						if count in final:
							list_ind = final.index(count)
							print(placement(tamil_transliteration[list_ind],'emp')) 
					count+=1
				elif len(i)>1:
					if i[0]=='en':
						print(placement('<br>'.join(lines[count:count+len(i)]),'en'))
					elif i[0]=='ta':
						print(placement('<br>'.join(lines[count:count+len(i)]),'ta'))
						if count in final:
							print(placement('<br>'.join(tamil_transliteration[list_ind:list_ind+len(i)]),'emp'))       
					count+=len(i)
			output = new_stdout.getvalue()
			sys.stdout = old_stdout
			st.code(output)
		except Exception as e: 
			st.code(e)
	




