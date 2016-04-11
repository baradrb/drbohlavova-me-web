import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html> <head><title>Bara Drbohlavova</title></head><body><h1>Bara Drbohlavova</h1><p>This page is under construction.</p><p>You can <a href="mailto:bara@drbohlavova.me">contact me</a>.</p></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

