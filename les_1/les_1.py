import chardet
import subprocess
import platform


def task(n):
    line_sep = '#' * 30
    print(f'\n{line_sep} {n} {line_sep}')


"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
"""

task(1)


def get_type_n_content(lst):
    for item in lst:
        print(item, type(item))


strings = ['разработка', 'сокет', 'декоратор']

get_type_n_content(strings)

strings_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                   '\u0441\u043e\u043a\u0435\u0442', '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

get_type_n_content(strings_unicode)

"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе. 
Сделать это необходимо в автоматическом, а не ручном режиме, с помощью добавления литеры b к текстовому значению,
 (т.е. ни в коем случае не используя методы encode, decode или функцию bytes) 
 и определить тип, содержимое и длину соответствующих переменных."""

task(2)
words = ['class', 'function', 'method']


def word_in_bytes(word):
    new_bytes = eval(f"b'{word}'")
    print(f'{new_bytes=}, {type(new_bytes)=}, {len(new_bytes)=}')


for i in words:
    word_in_bytes(i)

"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
 байтовом типе. Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""
task(3)

words = ['attribute', 'класс', 'функция', 'type']


def try_write_in_bytes(my_str):
    try:
        str_to_bytes = eval(f"b'{my_str}'")
    except SyntaxError:
        print(f'слово "{my_str}" невозможно записать в байтовом типе')
    else:
        print(f'слово "{my_str}" в байтовом виде выглядит так: {str_to_bytes}')


for i in words:
    try_write_in_bytes(i)

""" 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode)."""

task(4)

words = ['разработка', 'администрирование', 'protocol', 'standard']
print(f'{words=}')


def encode_word(word):
    bytes_from_word = str.encode(word, encoding='utf-8')
    return bytes_from_word


def decode_bytes(bytes_):
    word_from_bytes = bytes.decode(bytes_)
    return word_from_bytes


my_bytes = []

for i in words:
    print(f'слово "{i}" закодировалось как {encode_word(i)}')
    my_bytes.append(encode_word(i))

print(f'{my_bytes=}')

for b in my_bytes:
    print(f'{b} декодировалось как - "{decode_bytes(b)}"')

"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице."""

# Не смотря на то, что обратили внимание на сложность такого подхода и что есть другой, интереснее именно так.

task(5)


def my_ping(url):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '4', url]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for ln in subproc_ping.stdout:
        result = chardet.detect(ln)
        ln = ln.decode(result['encoding']).encode('utf-8')
        print(ln.decode('utf-8'))


my_ping('yandex.ru')

my_ping('youtube.com')

"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое."""

task(6)
lines = ["сетевое программирование", "сокет", "декоратор"]
with open("test_file.txt", "w") as f_1:
    for line in lines:
        f_1.write(f'{line}\n')


def recode_n_read(file, my_encoding):
    sep = '\n' + '-' * 80
    try:
        with open(file, 'rb') as f:
            f_content = f.read()
            f_encoding = chardet.detect(f_content)['encoding']
            new_content = f_content.decode(f_encoding).encode(my_encoding)
            new_encoding = chardet.detect(new_content)['encoding']  # На всякий случай проверю новую кодировку
    except UnicodeEncodeError:
        print(f'Этот файл не кодируется в системе кодировки {my_encoding}, попробуйте другую.{sep}')
    except LookupError:
        print(f'{my_encoding.upper()}? Что-то мы не знаем такую систему кодировки!!! Попробуйте другую.{sep}')
    except FileNotFoundError:
        print(f'Поискали-поискали, не нашли файл {file}. Может возьмете другой файл?{sep}')
    else:
        print('encoding:', f_encoding)
        print(new_content.decode(my_encoding).rstrip())
        print('new_encoding: ', new_encoding, sep)


recode_n_read('test_file.txt', 'utf-8')
recode_n_read('test_file.txt', 'utf-16')
recode_n_read('test_file.txt', 'utf-32')
recode_n_read('test_file.txt', 'utf-64')
recode_n_read('test_file.txt', 'ascii')
recode_n_read('null_file.txt', 'utf-8')
