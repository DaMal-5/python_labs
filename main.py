import sys
import math

def read_measurements(filename: str) -> dict:
    city_stats = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            text = line.split(";")
            station = text[0]
            temperature = float(text[1])
            if station not in city_stats:
                city_stats[station] = [temperature, temperature, temperature, 1] # max, min, sum, quant
            else:
                if temperature > city_stats[station][0]:
                    city_stats[station][0] = temperature
                if temperature < city_stats[station][1]:
                    city_stats[station][1] = temperature
                city_stats[station][2] += temperature
                city_stats[station][3] += 1
    return city_stats



def normalize_dict(city_stats: dict) -> dict:
    for station in city_stats:
        max_temperature, min_temperature, total_sum, count = city_stats[station]
        avg = total_sum / count
        rounded_avg = math.floor(avg * 10 + 0.5) / 10
        city_stats[station] = (min_temperature, rounded_avg, max_temperature)
    return city_stats



def print_sorted(normalized: dict) -> None:
    sorted_keys = sorted(normalized.keys())
    for key in sorted_keys:
        min_by_station, avg_by_station, max_by_station = normalized[key]
        print(f"{key};{min_by_station:.1f};{avg_by_station:.1f};{max_by_station:.1f}")



def main():
    if len(sys.argv) != 2:
        print("ошибка: укажите путь к файлу.", file=sys.stderr)
        sys.exit(1)
    filename = sys.argv[1]
    try:
        stats = read_measurements(filename)
    except FileNotFoundError:
        print("Файл не найден", file=sys.stderr)
        sys.exit(1)
    normalized_stats = normalize_dict(stats)
    print_sorted(normalized_stats)

if __name__ == "__main__":
    main()