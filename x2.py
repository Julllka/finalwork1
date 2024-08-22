import x

class YD_connector:

    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}
        token = 'y0_AgAAAABgrLWwAAA'

    def create_folder(self, folder_name):
        url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = request.put(url_create_folder,
                                headers=self.headers,
                                params={'path': folder_name})
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        create_folder('folder_name')

    def up_load_image(self):
        response = request.post('https://cloud-api.yandex.net/v1/disk/resources/upload')
        url = 'https://sun9-25.userapi.com/impf/c622216/v622216179/59ba/TsAYkjuqWaI.jpg?size=682x1024&quality=96&sign=736129f06efaa4ea86d5dc6dbff76475&type=album'
        params = 'https://disk.yandex.ru/client/disk/folder_name'
        with open ('image.json', 'w') as f:
            f.write(json.dumps(to_json))