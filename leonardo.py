import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >=0 and hour <12:
		speak("Good Morning!")
	elif hour >=12 and hour <18:
		speak("Good Afternoon!")
	else:
		speak("Good Evening!")
	speak("I am Leonardo sir, how may I help you?")

def takeCommand():
	'''
	takes microphone command and returns input
	'''

	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language = 'en-in')
		print(f"You said: {query}\n")
	except Exception as e:
		print(e)
		print("Say that again please...")
		return "None"
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('theconscienceofficial@gmail.com', 'conscience@google')
	server.sendmail('theconscienceofficial@gmail.com',to,content)
	server.close()





if __name__ == '__main__':
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	wishMe()
	while True:
	    query = takeCommand().lower()
	    if 'wikipedia' in query:
	    	speak("searching wikipedia...")
	    	query = query.replace("wikipedia","")
	    	results = wikipedia.summary(query,sentences=2)
	    	speak("According to wikipedia")
	    	speak(results)
	    elif 'exit' in query:
	    	exit()

	    elif 'shutdown' == query:
	    	speak("Do you really want to shut down your Computer boss?")
	    	query2 = takeCommand().lower()
	    	if(query == "yes shutdown"):
	    	    os.system("shutdown /s /t 1");

	    elif 'who are you' in query:
	    	speak("I am Leonardo, your virtual assistant, boss")

	    elif 'who am i' in query:
	    	speak("You are Tarang, boss. You are my creator")
	    elif 'hey leonardo' in query or 'hey leo' in query:
	    	speak("Hello boss")

	    elif 'open youtube' in query or 'youtube open' in query:
	    	webbrowser.get(chrome_path).open("youtube.com")

	    elif 'search youtube for' in query:
	    	query = query.replace("search youtube for ","")
	    	query=query.replace(" ","+")
	    	webbrowser.get(chrome_path).open("youtube.com/results?search_query="+query)


	    elif 'open facebook' in query:
	    	webbrowser.get(chrome_path).open("facebook.com")

	    elif 'open instagram' in query:
	    	webbrowser.get(chrome_path).open("instagram.com")

	    elif 'open linkedin' in query:
	    	webbrowser.get(chrome_path).open("linkedin.com")

	    elif 'open google' in query:
	    	webbrowser.get(chrome_path).open("google.com")

	    elif 'open udemy' in query:
	    	webbrowser.get(chrome_path).open("udemy.com")

	    elif 'open github' in query:
	    	webbrowser.get(chrome_path).open("github.com")

	    elif 'open heroku' in query:
	    	webbrowser.get(chrome_path).open("heroku.com")

	    elif 'open the conscience' in query:
	    	webbrowser.get(chrome_path).open("theconscience.cf")



	    elif 'search google for' in query:
	    	query = query.replace("search google for ","")
	    	query=query.replace(" ","+")
	    	webbrowser.get(chrome_path).open("google.com/search?q="+query)


	    elif 'open stackoverflow' in query:
	    	webbrowser.get(chrome_path).open("stackoverflow.com")

	    elif 'play music' in query:
	    	music_dir = "D:\\Alan Walker"
	    	songs = os.listdir(music_dir)
	    	print(songs)
	    	os.startfile(os.path.join(music_dir, songs[0]))

	    elif 'the time' in query:
	    	strTime = datetime.datetime.now().strftime("%H:%M:%S")
	    	speak(f"Sir, the time is {strTime}")

	    elif 'open sublime' in query:
	    	sublimePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
	    	os.startfile(sublimePath)
	    elif 'send email' in query:
	    	try:
	    		speak("What should I say?")
	    		content = takeCommand()
	    		to = "taranggarlapally@gmail.com"
	    		sendEmail(to, content)
	    		speak("Sir, your Email has been sent")
	    	except Exception as e:
	    		print(e)
	    		speak("Sorry sir, I am unable to send an Email")



