from main import Main
from daemon import runner
from njitcoursetracker import NJITCourseTracker
from emailer import Emailer
import urllib, urllib2
import time
import json


app = NJITCourseTracker('2017s', 'CS')

class App:
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
        
    def run(self):
        while True:
            with open('courses.json') as data_file:
            	courses = json.load(data_file)
            
           	foundCourses = app.execute(courses)
            
            if len(foundCourses) != 0:
            	body = 'The following course(s) have just opened up: <br> <ul>'
            	
            	for foundCourse in foundCourses:
            		body = body + '<li>'+foundCourse+'</li>'

            	body = body + '</ul>'

            	email = Emailer('mdnahian@outlook.com', 'do_not_reply@njitcoursetracker.com', 'NJIT Course Tracker - Course(s) Opened', body)

            	body.send()

            time.sleep(1800)


application = App()
daemon_runner = runner.DaemonRunner(application)
daemon_runner.do_action()