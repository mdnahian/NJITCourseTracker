import sendgrid
import os
from sendgrid.helpers.mail import *

class Emailer:
	
	def __init__(self, to_email, from_email, subject, body):
		self.to_email = to_email
		self.from_email = from_email
		self.subject = subject
		self.body = body

	def send():
		sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
		from_email = Email(self.from_email)
		to_email = Email(self.to_email)
		content = Content("text/html", self.body)
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body = mail.get())
		# print(response.status_code)
		# print(response.body)
		# print(response.headers)
