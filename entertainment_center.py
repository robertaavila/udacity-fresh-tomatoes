# coding: UTF-8
# importa o arquivo media, que contem a descricao da classe Movie. 
import media
# importa o arquivo fresh tomatoes, que sobrepoe instrucoes ao arquivo html. 
import fresh_tomatoes

#instancia referente ao filme Forrest Gump.
forrest_gump = media.Movie('Forrest Gump(1994)',
                           'Forrest Gump',
                           'Duracao: 2h22min',
                           'Drama, Romance',
                           'The presidencies of Kennedy and Johnson, Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.',
                           'https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg',
                           'https://www.youtube.com/watch?v=p0p5CQUjTxI')

#instancia referente ao filme Naufrago.
naufrago = media.Movie('Naufrago (2000)',
                       'Cast Away',
                       'Duracao: 2h23min',
                       'Aventura, Drama, Romance',
                       'A FedEx executive must transform himself physically and emotionally to survive a crash landing on a deserted island.', 
                       'https://m.media-amazon.com/images/M/MV5BN2Y5ZTU4YjctMDRmMC00MTg4LWE1M2MtMjk4MzVmOTE4YjkzXkEyXkFqcGdeQXVyNTc1NTQxODI@._V1_UX182_CR0,0,182,268_AL_.jpg',
                       'https://www.youtube.com/watch?v=OhrjakAt2GI')

#instancia referente ao filme Mensagem para Voce.
mensagem_voce = media.Movie('Mens@gem para Voce (1998)',
                            'You have Got Mail',
                            'Duracao: 1h59min',
                            'Comedia, Drama, Romance',
                            'Two business rivals who despise each other in real life unwittingly fall in love over the Internet.',
                            'https://m.media-amazon.com/images/M/MV5BZTcxNzgzZjMtYzZiZC00MmE1LTg3MzQtZDAxMTYyZWE4MDNhL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                            'https://www.youtube.com/watch?v=znESQTt3L80')

#instancia referente ao filme Sintonia de Amor.
sintonia_amor = media.Movie('Sintonia de Amor (1993)',
                            'Sleepless in Seattle',
                            'Duracao: 1h45min',
                            'Comedia, Drama, Romance',
                            'The son of a recently widowed man calls a radio talk-show in an attempt to find his father a partner.',
                            'https://m.media-amazon.com/images/M/MV5BNWY1MDJkZGUtZTE2OS00ODZiLTlmNzQtMDZjNzM2ZjkwM2QxXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_CR0,0,676,1000_AL_.jpg', 
                            'https://www.youtube.com/watch?v=Cr3MVu7TjC8')

#instancia referente ao filme O Terminal.
terminal = media.Movie('O Terminal (2004)',
                       'The Terminal',
                       'Duracao: 2h8min',
                       'Comedia, Drama, Romance',
                       'An Eastern European tourist unexpectedly finds himself stranded in JFK airport, and must take up temporary residence there.',
                       'https://m.media-amazon.com/images/M/MV5BMTM1MTIwNTMxOF5BMl5BanBnXkFtZTcwNjIxMjQyMw@@._V1_SY1000_CR0,0,737,1000_AL_.jpg',
                       'https://www.youtube.com/watch?v=GZjC9dAvWuU')

#instancia referente ao filme Quero ser Grande.
grande = media.Movie('Quero ser Grande (1988)',
                     'Big',
                     'Duracao: 1h44min',
                     'Comedia, Drama',
                     'After wishing to be made big, a teenage boy wakes the next morning to find himself mysteriously in the body of an adult.',
                     'https://m.media-amazon.com/images/M/MV5BMDQ1ODM5MTMtMjAwYi00ZGUxLTliNTMtN2ZhODAwMjVhMTRlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,682,1000_AL_.jpg',
                     'https://www.youtube.com/watch?v=pO1SROeo_JM')

#lista com todas as instâncias. 
movies = [naufrago, sintonia_amor, grande, terminal, mensagem_voce, forrest_gump]

#instrucao para abertura do arquivo fresh tomatoes. 
fresh_tomatoes.open_movies_page(movies)
