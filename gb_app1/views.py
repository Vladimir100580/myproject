# from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def main(request):
    http_txt = """
        <h1 class = 'cnt'> Главная страница </h1>
        <h2 class = 'cnt'> О моем первом Django сайте. </h2>
        <div style='margin: 0 20px 0 40px'>
        <h3 class= 'tx'> Во времена первой волны COVID-19 возникла идея написать скрипт, 
        который сможет быстро формировать множество задач (по физике, математике), <br> не опубликованных в интернете 
        (выбирая параметры, входящие в задачи рандомно, но разумно). <br>
        А, даже если, ученик и найдет похожую задачу, придется вникнуть в решения и подставить свои значения. Чтобы 
        предотвратить поголовное списывание готовых ответов. Скрипт постепенно писался (на python), задачи и темы 
        пополнялись. И, наконец, возникла идея всю эту красоту сделать общедоступной для всех учителей. От учителей 
        информатики помощи не нашлось. Пришло откровение, одновременно смотря бесплатные уроки Itproger и других авторов 
        различных IT-роликов, писать сайт на Django. </h3>
        <h3 class= 'tx'> Изначально сайт разрабатывался, как эксперимент, однако,
        при четкой цели и достаточном терпении ... <br> Идея воплотилась в жизнь 01.11.2021 - запуск сайта U4Help! </h3>
        <h3 class= 'tx'> Используя небольшую рекламу ВК, на данный момент, сайт насчитывает более 900 зарегистрированных
        учителей физики и  математики. Треть из которых, довольно активно его используют. </h3>
        <h3 class= 'tx'> Да, чего много писать - 
        <a style="font-style: italic;" href="https://u4help.ru" target="_blank">переходите</a>
        по вкладке "О сайте" можно найти подробную информацию. </h3>
        <h3 class= 'tx'> Описание сайта в
        <a style="font-style: italic;" href="https://youtu.be/IMKmEmG1V9A" target="_blank"> кратком 
        видео. </a> 
        </h3>
        </div>
        <style>
        .tx {
        text-indent: 40px;
        line-height: 1.5
        }
        .cnt {
        text-align: center;
        font-style: italic;
        }
        </style> 
        """
    return HttpResponse(http_txt)


def about(request):
    http_txt = """
        <h1 class = 'cnt'> О себе </h1>
        <h2 class = 'cnt'> Побойкин Владимир Яковлевич (43 года) </h2>
        <div style='margin: 0 20px 0 40px'>
        <h3 class= 'tx'> Более 17 преподаю математику и физику в Лицее (имею высшую квалификационную категорию)
        и ВУЗе (ст. преподаватель) <br> Окончил аспирантуру в 2013году. 
        <h3 class= 'tx'> Христианин-протестант! Вместе с супругой служим
         в <a style="font-style: italic; font-size: 18px;" href="https://vk.com/murmanchurch" target="_blank">
        Храме </a> </h3>
        <h3 class= 'tx'> P.S. Написал <a style="font-style: italic;" href="https://ustns4et.ru/" target="_blank">
        web-тренажер по устному счету </a> (используя Django + JS).
        </h3>
        </div>
        <style>
        .tx {
        text-indent: 40px;
        line-height: 1.5
        }
        .cnt {
        text-align: center;
        font-style: italic;
        }
        </style> 
        """
    try:
        t = 3       # Здесь можно написать 0 чтобы отловить ошибку.
        result = 15 / t
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("На ноль не делим!")
    else:
        logger.debug('About page accessed')
        return HttpResponse(http_txt)
