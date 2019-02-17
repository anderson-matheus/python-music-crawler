# -*- coding: utf-8 -*-

import requests
from slugify import slugify

class Request:
    def __init__(self, url, artist):
        """Construtor da classe Request, reponsável pelas requisições

        Parâmetros:
        url -- url do site que será feito a request
        artist -- nome do artista/banda escolhido
        """
        self.__url = url
        self.__artist = artist

    def content_page(self):
        """Método reponsável por montar a url e fazer a requisição para o site
        e retornar o conteúdo
        """
        # monta a url e faz um slug do artisan/banda escolhido
        url = self.__url + '/' + slugify(self.__artist).lower()
        try:
            response = requests.get(url)
        except Exception:
            return False

        response.encoding = 'utf-8'
        if response.status_code != 200:
            return False
        return response.text
