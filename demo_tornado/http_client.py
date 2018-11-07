
import tornado.httpclient


#from tornado import template
#t = template.Template("<html>{{ myvalue }}</html>")
#print (t.generate(myvalue="XXX"))


http_client = tornado.httpclient.HTTPClient()
try:
    response = http_client.fetch("http://localhost:8888/pi?n=200")
    print(response.body)
except tornado.httpclient.HTTPError as e:
    # HTTPError is raised for non-200 responses; the response
    # can be found in e.response.
    print("Error: " + str(e))
except Exception as e:
    # Other errors are possible, such as IOError.
    print("Error: " + str(e))
http_client.close()


