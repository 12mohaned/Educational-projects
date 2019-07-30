import jinja2
import os
import webapp2
import re
import cgi
template_dir = os.path.join(os.path.dirname(__file__), 'Template')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)
class Handler(webapp2.RequestHandler):
    def write(self,*template,**params):
        self.response.out.write(*template,**params)
    def render_str(self,template,**params):
        profile = jinja_env.get_template(template)
        return profile.render(params)
    def render(self,template,**params):
        self.write(self.render_str(template,**params))
class MainPage(Handler):
        def valid_username(self,username):
            USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
            return USER_RE.match(username)
            print(1)
        def valid_password(self,password):
            user_pass = re.compile("^.{3,20}$")
            return user_pass.match(password)
        def valid_Verification(self,re_password,password):
            if(re_password != password):
                return False
            re_user_pass = re.compile(".{3,20}$")
            return re_user_pass.match(re_password)
        def valid_email(self,Email):
            user_email = re.compile("^[\S]+@[\S]+.[\S]+$")
            return user_email.match(Email)
        def get(self):
            self.write(self.render("t.html"))
        def post(self):
            Error = False
            Error_name = ""
            Error_pass = ""
            Error_re_pass=""
            Error_email = ""
            user_name = self.request.get("username")
            password = self.request.get("password")
            re_password = self.request.get("repassword")
            Email = self.request.get("Email")
            if(not self.valid_username(user_name)):
                Error_name = "That's not Valid Username"
                Error = True
            if(not self.valid_password(password)):
                Error_pass = "That's not Valid password"
                Error = True
            if(not self.valid_Verification(re_password,password)):
                Error_re_pass = "password doesn't match"
                Error = True
            if( self.valid_email(Email)):
                if (Email == ""):
                    Error = False
                else:
                    Error_email = "Email is not Valid"
                    Error = True
            if(Error):
                print("You have Error")
                self.render("t.html",username = user_name,email = Email,usernameError = Error_name,PasswordError = Error_pass
                ,VerificationError = Error_re_pass,EmailError = Error_email)
            else:
                self.render("Welcome.html",username = user_name)
app = webapp2.WSGIApplication([('/HomePage',MainPage)], debug=True)
def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8000')

if __name__ == '__main__':
    main()
