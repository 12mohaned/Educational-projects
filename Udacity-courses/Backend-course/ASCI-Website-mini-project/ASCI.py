import webapp2
import os
import jinja2
import cgi
from google.appengine.ext.remote_api import remote_api_stub
template_dir = os.path.join(os.path.dirname(__file__))
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)
class Handler(webapp2.RequestHandler):
    def write(self,*template,**params):
        self.response.out.write(*template,**params)
    def render_str(self,template,**params):
        profile = jinja_env.get_template(template)
        return profile.render(params)
    def render(self,template,**params):
        self.write(self.render_str(template,**params))
class Art(db.model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
class MainPage(Handler):
    def get (self):
        self.render("ASCI.html")
    def post (self):
        title = self.request.get("title")
        art = self.request.get_all("art")
        arts = db.GqlQuery("SELECT * FROM Art created ORDERED by desc")
        result = ""
        if not title or not art :
            if not title :
                result = "title"
            if not art :
                result+=" art"
            self.render('ASCI.html',error = result +" is not filled")
        else:
            self.render('ASCI.html',Title = title,art = art)
app = webapp2.WSGIApplication([('/HomePage',MainPage)], debug=True)
def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8000')

if __name__ == '__main__':
    main()
