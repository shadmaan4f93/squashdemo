from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body> <div><img src='https://www.dropbox.com/s/g9qb5ai22hr6f72/happy.png?raw=1' width='200' height='200'><br><h1>Hi User</h1> <h4>It is now %s.</h4></div></body></html>" % now
    return HttpResponse(html)