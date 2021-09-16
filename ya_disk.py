from pprint import pprint


import requests


class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _upload_link(self, disk_file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, disk_file_path, filename):
        href = self._upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':

    token = ""
    uploader = YaUploader(token)
    uploader.upload("File/file.txt", "file.txt")