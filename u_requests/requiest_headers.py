#
#     requests by urllib3
###
import urllib3
import json
import logging
logging.getLogger("urllib3").setLevel(logging.WARNING)


http = urllib3.PoolManager()


def headers():
    #   You can specify headers as a dictionary in the headers argument
    r = http.request('GET', 'http://httpbin.org/headers', headers={'X-Something': 'value'})
    print(json.loads(r.data.decode('utf-8'))['headers'])


def parameters():
    #   You can specify headers as a dictionary in the headers argument
    r = http.request(
        'GET',
        'http://httpbin.org/get',
        fields={'arg': 'value'})
    print(json.loads(r.data.decode('utf-8'))['args'])


def emb_args():
    #
    from urllib.parse import urlencode
    encoded_args = urlencode({'arg': 'value'})
    url = 'http://httpbin.org/post?' + encoded_args
    r = http.request('POST', url)
    print(json.loads(r.data.decode('utf-8'))['args'])


def form_args():
    #   For PUT and POST requests, urllib3 will automatically form-encode the dictionary in the fields argument
    r = http.request(
        'POST',
        'http://httpbin.org/post',
        fields={'field': 'value'})
    print(json.loads(r.data.decode('utf-8'))['form'])


def send_json():
    #   You can send a JSON request by specifying the encoded data as the body argument and setting the Content-Type header
    data = {'attribute': 'value'}
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request(
        'POST',
        'http://httpbin.org/post',
        body=encoded_data,
        headers={'Content-Type': 'application/json'})
    print(json.loads(r.data.decode('utf-8'))['json'])


def upload_file():
    #   For uploading files using multipart/form-data encoding you can use the same approach as Form
    #   data and specify the file field as a tuple of (file_name, file_data):
    with open('example.txt') as fp:
        file_data = fp.read()
        r = http.request(
            'POST',
            'http://httpbin.org/post',
            fields={
            'filefield': ('example.txt', file_data),
            })
    print(json.loads(r.data.decode('utf-8'))['files'])


def upload_file_mime():
    #   For uploading files using multipart/form-data encoding you can use the same approach as Form
    #   data and specify the file field as a tuple of (file_name, file_data):
    #   You can also pass a third item in the tuple to specify the file’s MIME type explicitly
    with open('example.txt') as fp:
        file_data = fp.read()
        r = http.request(
            'POST',
            'http://httpbin.org/post',
            fields={
            'filefield': ('example.txt', file_data, 'text/plain'),
            })
    print(json.loads(r.data.decode('utf-8'))['files'])

def upload_image():
    with open('example.jpg', 'rb') as fp:
        binary_data = fp.read()
    r = http.request(
        'POST',
        'http://httpbin.org/post',
        body=binary_data,
        headers={'Content-Type': 'image/jpeg'})
    print(json.loads(r.data.decode('utf-8'))['data'])

def exceptions():
    try:
        http.request('GET', 'nx.example.com', retries=False)
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed.')

#exceptions()
