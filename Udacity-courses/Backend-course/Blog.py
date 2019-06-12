import jinja2
import os
import webapp2
import re
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
class Home(Handler):
    def get(self):
        self.render("Blog.html")
    def post(self):
        Body_Error = ""
        Subject_Error = ""
        Body = self.get.request("BlogBody")
        Subject = self.get.request("Subject")
        if not Body :
                Body_Error = "Body is missing"
        if not Subject:
                Subject_Error = "Subject is missing"
        if Subject and Body :
                self.render("Blog.html",BlogBody = Body,Subject = Subject,
                BodyError = Body_Error,SubjectError = Subject_Error)

app = webapp2.WSGIApplication([('/Blog',Home)], debug=True)
def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8000')

if __name__ == '__main__':
    main()
