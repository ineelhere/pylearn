# import the "requests package"
import requests
# get the work done in just one line
open('image.jpg', 'wb').write((requests.get("https://images.pexels.com/photos/327533/pexels-photo-327533.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940")).content)


#requests.get() actually downloads the file and the other codes are used to write the downloaded file in a desired fashion.
