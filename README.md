# Для запуска нужен uv
git clone https://github.com/DaMal-5/python-lab1.git
cd python-lab1
# Генерация файла с данными
uv run data/generate_measurements.py N -o measurements_*.txt
# Изменение кодировки (при ошибке на windows)
## $env:PYTHONIOENCODING="utf-8"
# Запуск программы
uv run main.py data/measurements_*.txt
# Проверка
uv run main.py data/measurements_*.txt \
    | python data/check.py data/measurements_*.out

# Профилирование
Исходное время до оптимизаций

  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    7.436    7.436   11.245   11.245 main.py:4(read_measurements)
 10000000    2.010    0.000    2.010    0.000 {method 'split' of 'str' objects}
  9999589    1.703    0.000    1.703    0.000 stats.py:33(update)
    16817    0.082    0.000    0.082    0.000 {built-in method _codecs.utf_8_decode}
    16817    0.013    0.000    0.095    0.000 <frozen codecs>:322(decode)

Основное время уходит на основной цикл, методы split и update из-за работы с кучей строк

Добавлено бинарное чтение и разделение

 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    6.616    6.616   10.609   10.609 main.py:4(read_measurements)
 10000000    1.545    0.000    1.545    0.000 {method 'split' of 'bytes' objects}
  9999589    1.227    0.000    1.227    0.000 stats.py:33(update)
 10000000    1.221    0.000    1.221    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}

    Чтение и деление стало быстрее