import requests
import time

line_token = 'zO29kfiZhpQrxjXTurjBleVR2cnkfpwMnfTKunfZHEV'
URL_LINE = "https://notify-api.line.me/api/notify" 

class line:
    def line_pic(message, path_file):
        time.sleep(1)
        file_img = {'imageFile': open(path_file, 'rb')}
        msg = ({'message': message})
        LINE_HEADERS = {"Authorization":"Bearer "+line_token}
        session = requests.Session()
        session_post = session.post(URL_LINE, headers=LINE_HEADERS, files=file_img, data=msg)
        print('---------Notification Success!---------')