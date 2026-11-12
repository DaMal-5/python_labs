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

Чтение и разделение стало быстрее

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    4.991    4.991    7.496    7.496 main.py:4(read_measurements)
 10000000    1.351    0.000    1.351    0.000 {method 'split' of 'bytes' objects}
  9999589    1.154    0.000    1.154    0.000 stats.py:33(update)
        3    0.000    0.000    0.000    0.000 {built-in method nt.stat}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}

Теперь декодируется только итоговый список станций, а вся логика работает с сырыми байтами

Добавлено __slots__

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    4.975    4.975    7.488    7.488 main.py:4(read_measurements)
 10000000    1.340    0.000    1.340    0.000 {method 'split' of 'bytes' objects}
  9999589    1.174    0.000    1.174    0.000 stats.py:35(update)
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
      411    0.000    0.000    0.000    0.000 stats.py:7(__init__)

Время почти не изменилось, так как конкретно в нашей задаче slots влияет незначительно 