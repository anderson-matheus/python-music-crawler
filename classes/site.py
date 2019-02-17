# -*- coding: utf-8 -*-

class Site:
    __sites = ['Vagalume']
    __url_default = 'http://www.vagalume.com.br'

    def available_sites(self):
        """Método responsável por retornar lista de sites disponíveis
        para pesquisa de músicas.
        """
        return self.__sites


    def find_url_site(self, key):
        """Método responsável por retornar a url do site escolhido para
        fazer a pesquisa de músicasself.

        Parâmetros:
        key -- número do site escolhido
        """
        try:
            site_name = self.__sites[key]
            if site_name.lower() == 'vagalume':
                return 'http://www.vagalume.com.br'
        except IndexError:
            return self.__url_default
        except TypeError:
            return self.__url_default
