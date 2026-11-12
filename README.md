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
 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    5.720    5.720    8.638    8.638 main.py:4(read_measurements)
 10000000    1.556    0.000    1.556    0.000 {method 'split' of 'str' objects}
  9999589    1.297    0.000    1.297    0.000 stats.py:33(update)
    16817    0.058    0.000    0.058    0.000 {built-in method _codecs.utf_8_decode}
    16817    0.008    0.000    0.065    0.000 <frozen codecs>:322(decode)

Основное время уходит на методы split и update из-за работы с кучей строк