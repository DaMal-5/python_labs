import sys
from stats import StationStats

def read_measurements(filename: str) -> dict:
    city_stats = {}
    with open(filename, "rb") as f:
        for line in f:
            parts = line.split(b";")
            station = parts[0].decode("utf-8")
            temperature = float(parts[1])
            
            if station not in city_stats:
                city_stats[station] = StationStats(temperature)
            else:
                city_stats[station].update(temperature) 
    return city_stats

def print_sorted(city_stats: dict) -> None:
    for station in sorted(city_stats.keys()):
        print(f"{station};{city_stats[station]}")

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
        
    print_sorted(stats)

if __name__ == "__main__":
    main()