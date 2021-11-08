import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        file_name = os.path.basename(file_path)
        params = {"path": file_name, "overwrite": "true"}
        href = requests.get(upload_url, headers=headers, params=params).json()['href']
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл загружен')


if __name__ == '__main__':
    path_to_file = 'C:/Users/Sergey/PycharmProjects/pythonProject5/data.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

