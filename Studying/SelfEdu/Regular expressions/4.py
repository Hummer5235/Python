#Проверки флаги
import re , os
a = os.system('CLS')

#| - канал , используется для выбора альтернативных вариантов
text = 'подоходный налог'
match = re.findall(r'прибыль|обретение|доход',text)
print(match)

r'''
^
Начало текста (с флагом re.MULTILINE – начало строки)

$
Конец текста (с флагом re.MULTILINE – позиция перед символом переноса строки \n)

\A
Начало текста

\b
Граница слова (внутри символьных классов [] соответствует символу BACKSPACE)

\B
Граница не слова (зависим от флага re.ASCII)

\Z
Конец текста

(?=exp)
Проверка на совпадение с выражением exp продолжения строки. При этом позиция поиска не смещается на выражение exp (опережающая проверка).

(?!exp)
Проверка на несовпадение с выражением exp продолжения строки. (Также опережающая проверка).

(?<=exp)
Проверка на совпадение с выражением exp хвоста уже обработанной (проверенной) строки. Она также называется позитивной ретроспективной проверкой.

(?<!exp)
Проверка на несовпадение с выражением exp хвоста уже обработанной (проверенной) строки. Еще она называется негативной ретроспективной проверкой.
'''


text = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type    " content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
<p align=center> Hello World! </p>

</body>
</html>"""


match = re.findall(r'^<script.*?>([\w\W]+)(?=</script>)',text, re.MULTILINE)
match2 = re.findall(r'([-\w]+)\s*=\s*[\'"]+(.+)(?<!\s)',text, re.MULTILINE)

#Чтобы найти еще строку align=center,добавим проверку на наличие группирующего выражения
#(?P<q>[\'''])     (?(id|name)yes_pattern|no_pattern)
match3 = re.findall(r'([-\w]+)\s*=\s*(?P<q>[\'"])?(?(q)([^\'"]+(?<!\s))|([^\s>]+))',text)
print(match)
print(match2)
print(match3)

#В противном случае выполняем проверку пока не встретим пробел или закрывающую угловую скобку