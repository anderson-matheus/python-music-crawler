# -*- coding: utf-8 -*-

import os
import platform
import sys
from classes.site import Site
from classes.crawler import Crawler
from classes.request import Request

while True:
    site = Site()
    sites = site.available_sites() # retorna a lista de sites disponíveis para pesquisa
    print('Pesquise as músicas de seu artista favorito\n')
    print('Digite o número do site que deseja fazer essa pesquisa:')

    # Faz a iteração na lista de sites disponíveis
    i = 0
    for site_name in sites:
        print('%d) %s' % (i, site_name))
        i = i + 1

    # Tratamento de input de usuário que deve somente um número inteiro
    print('\n')
    try:
        site_key = int(input('Digite o número do site: '))
    except ValueError:
        print('\nInforme um número inteiro para escolher o site')
        sys.exit()

    # Tratamento de exceção se o usuário informar o número de um site que não exista
    try:
        sites[site_key]
        url = site.find_url_site(site_key) # pesquisa a url do site selecionado
        artist = input('Digite o nome do artista: ')
        # Tratamento de input de usuário que deve ser um número inteiro
        try:
            number_songs = int(input('Digite a quantidade de músicas que deseja pesquisar o default são 15: '))
        except ValueError:
            number_songs = 15
            print('\nComo não foi informado um número inteiro será retornado 15 músicas do artista/banda')

        request = Request(url, artist)
        content = request.content_page() # retorna o texto html da página do artista/banda escolhido
        # Condição que faz a verificação se a página foi encontrada
        if content == False:
            print('\nA página do cantor escolhido não foi encontrada')
            sys.exit()

        crawler = Crawler(content, number_songs)
        musics = crawler.find_musics() # retorna uma lista com as músicas
        i = 0
        print('\nForam encontradas %d músicas da banda/artista %s' % (crawler.number_songs(musics), artist.upper()))
        # Faz a iteração na lista de músicas
        for music in musics:
            print('%d) %s' % (i, music))
            i = i + 1
    except IndexError:
        print('O site informado não existe\n')

    # Condição para sair do laço caso o usuário não queira fazer mais pesquisas
    continue_search = input('\nDigite (sim) se deseja fazer outra pesquisa: ')
    if (continue_search.lower() != 'sim'):
        sys.exit()

    # Condição para limpar tela do terminar de acordo com o SO
    if platform.system() == 'Linux':
        clear = lambda: os.system('clear')
        clear()
    elif platform.system() == 'Windows':
        clear = lambda: os.system('cls')
        clear()
