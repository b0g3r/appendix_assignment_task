from aiohttp import web

import files

routes = web.RouteTableDef()


@routes.view('/appendix/{file_name}')
class AppendixView(web.View):
    async def get(self):
        """
        возвращает содержимое файла в теле ответа. Также в ответе должен
        присутствовать заголовок "SCA-Checksum: X" с SCA чексуммой содержимого файла
        """
        file_name = self.request.match_info['file_name']
        file_content = files.get_file_content(file_name)
        checksum = files.calculate_checksum(file_content)
        return web.Response(body=file_content, headers={'SCA-Checksum': checksum})

    async def put(self):
        """
        добавляет байты к файлу по имени {filename}. Если файла с таким именем не существует, создает его.
        """
        file_name = self.request.match_info['file_name']
        payload = await self.request.content.read()
        written_bytes = files.append_content(file_name, payload)
        return web.json_response({'written_bytes': written_bytes})

    async def delete(self):
        """
        удаляет файл {filename}
        """
        file_name = self.request.match_info['file_name']
        files.delete(file_name)
        return web.json_response({'deleted_file': file_name})


app = web.Application()
app.add_routes(routes)
web.run_app(app)
