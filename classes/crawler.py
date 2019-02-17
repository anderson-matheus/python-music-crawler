# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re

class Crawler:
    def __init__(self, content, number_songs):
        """Construtor da classe Crawler que faz a iniciação das propriedades
        necessárias.

        Parâmetros:
        content -- texto html com o conteúdo retornado pela request
        number_songs -- quantidade de músicas que deve ser retornado
        """
        self.__content = content
        if number_songs < 0 or number_songs == 0:
            self.__number_songs = 15
        else:
            self.__number_songs = number_songs

    def find_musics(self):
        """Método responsável por criar uma lista com o nome das músicas do
        artista/banda escolhido
        """
        musics = list()
        soup = BeautifulSoup(self.__content, 'lxml')
        data = soup.findAll('a', attrs = {'class' : 'nameMusic'})
        for music in data:
            musics.append(music.get_text())
        return musics[0:self.__number_songs]

    def number_songs(self, musics):
        """Método responsável por retornar a quantidade de músicas

        Parâmetros:
        musics -- lista de músicas
        """
        return len(musics)
