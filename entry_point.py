from aiohttp import web

routes = web.RouteTableDef()


@routes.view('/appendix/{file_name}')
class AppendixView(web.View):
    async def get(self):
        """
        возвращает содержимое файла в теле ответа. Также в ответе должен
        присутствовать заголовок "SCA-Checksum: X" с SCA чексуммой содержимого файла
        """
        file_name = self.request.match_info['file_name']
        return web.Response(text=file_name)

    async def put(self):
        """
        добавляет байты к файлу по имени {filename}. Если файла с таким именем не существует, создает его.
        """
        return web.Response(text='aa')


    async def delete(self):
        """
        удаляет файл {filename}
        """
        return web.Response(text='aa')


app = web.Application()
app.add_routes(routes)
web.run_app(app)
