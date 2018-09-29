
import urllib.request

def save_file(path, content):
    try:
        with open(path, "wb") as fw:
            fw.write(content)
        return True
    except Exception as e:
        print(e)
        return False

def post_file(url, name, content):
    try:
        post_data = {"file_name": name, "file_content": content}
        post_data = urllib.parse.urlencode(post_data).encode("utf-8")
        req = urllib.request.Request(url=url, data=post_data)
        urllib.request.urlopen(req)
        return True
    except Exception as e:
        return False