from bs4 import BeautifulSoup
import urllib2
import re

class NJITCourseTracker:
	
	def __init__(self, semester, subject):
		self.base_url = 'https://courseschedules.njit.edu/index.aspx?semester='+semester+'&subjectID='+subject

	def getHTML(self, inputURL):
		return urllib2.urlopen(inputURL)

	def match_class(self, target):
		def do_match(tag):
			classes = tag.get('class', [])
			return all(c in classes for c in target)
		return do_match

	def execute(self, coursesId):

		foundCourses = []

		# print "Getting HTML..."
		rawHTML = self.getHTML(self.base_url)
		html = BeautifulSoup(rawHTML, "html.parser")

		# print 'Finding Courses...'
		courses = html.findAll(self.match_class(['subject_wrapper']))
		for course in courses:
			for courseId in coursesId:
				foundCourse = course.findAll(text=re.compile(courseId.split()[1]))
				if len(foundCourse) != 0:
					sections = course.find_all('tr')
					sections.pop(0)

					for section in sections:
						status = section.findAll(self.match_class(['status']))[0]
						if status.text == 'Open':
							foundCourses.append(foundCourse[0])
							break

		return foundCourses

