from core.handler import BaseHandler
from core import app

@app.route("/")
class HomeHandler(BaseHandler):
    def get(self):
        self.render("index.html",username=self.get_cookie("userName"))
