# python-music-crawler
O python-music-crawler é responsável por fazer a pesquisa de músicas de um artisa/banda no site http://www.vagalume.com.br

## Requisitos
Python3.6

## Instalação

git clone https://github.com/anderson-matheus/python-music-crawler.git<br />
cd python-music-crawler<br />
virtualenv venv<br />
source venv/bin/activate<br />
pip3 install -r requiremets.txt<br />

## Testes

pytest tests.py

## Modo de uso
No terminal entre na pasta do projeto e rode o seguinte comando: python3 main.py<br />
Será exibido as informações abaixo:<br />
Você deve informar o número do site desejado, nome do artista e quantidade de músicas que devem ser retornadas, com isso será retornado o resultado.<br />
Ao final será feita uma pergunta se deseja fazer mais alguma pesquisa, caso a resposta for sim, o ciclo será executado novamente.<br />

```bash
Pesquise as músicas de seu artista favorito

Digite o número do site que deseja fazer essa pesquisa:
0) Vagalume


Digite o número do site: 0
Digite o nome do artista: Michael Jackson
Digite a quantidade de músicas que deseja pesquisar o default são 15: 20

Foram encontradas 20 músicas da banda/artista MICHAEL JACKSON
0) Billie Jean
1) Love Never Felt So Good (Feat. Justin Timberlake)
2) Heal The World
3) Thriller
4) Ben
5) You Are Not Alone
6) We Are The World
7) Smooth Criminal
8) Bad
9) Beat It
10) They Don't Care About Us
11) Man In The Mirror
12) Don't Stop 'Til You Get Enough
13) Earth Song
14) Black Or White
15) The Way You Make Me Feel
16) Human Nature
17) I'll Be There
18) Will You Be There
19) Rock With You

Digite (sim) se deseja fazer outra pesquisa:
```
