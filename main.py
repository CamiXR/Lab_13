import os
# Задание 1: деление с обработкой ошибок
try:
    a = int(input("Введи первое число: "))
    b = int(input("Введи второе число: "))
    result = a / b
    print("Результат:", result)
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
# Задание 2
try:
    x = int(input("Введи число: "))
    result = 10 / x 
    print("Результат:", result)
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
finally:
    print("Программа завершена")
# Задание 3: запись и чтение файла
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет\n")
    f.write("Как дела?\n")
    f.write("Пока\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
 
print(lines)              # все строки списком
real_lines = [x for x in lines if x != ""]
print("Строк в файле:", len(real_lines))
# Задание 4
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("Ещё одна строка\n")
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
print(lines)              # все строки списком
real_lines = [x for x in lines if x != ""]
print("Строк в файле:", len(real_lines))
#Задание 5
class Streamer:
    def __init__(self, nickname, subscribers, donates):
        self.nickname = nickname
        self.subscribers = subscribers
        self.donates = donates    # список чисел
 
    def to_line(self):
        # донаты сохраняем через запятую внутри одного поля
        donates_str = ",".join(str(d) for d in self.donates)
        return f"{self.nickname};{self.subscribers};{donates_str}"
    
    def total_donates(self):
        total = 0
        for i in self.donates:
            total = total + i
        return total
    
    def average_donate(self):
        if len(self.donates) == 0:
            return 0
        return self.total_donates() / len(self.donates)
 
def streamer_from_line(line):
    nickname, subscribers, donates_str = line.strip().split(";")
    if donates_str == "":
        donates = []
    else:
        donates = [int(d) for d in donates_str.split(",")]
    return Streamer(nickname, int(subscribers), donates)
a = Streamer("Shadow", 100, [400 , 200 , 30])
line = a.to_line()
b = streamer_from_line(line)
a.nickname == b.nickname
a.subscribers == b.subscribers
a.donates == b.donates
print ("Тест пройден")



def save_to_file(objects, filename):
    # сохраняет список объектов: одна строка - один объект
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(obj.to_line() + "\n")
 
def load_from_file(filename):
    # загружает объекты из файла, возвращает список
    objects = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                objects.append(streamer_from_line(line))
    except FileNotFoundError:
        print("Файл не найден, начинаем с пустого списка.")
    except ValueError:
        print("Ошибка в формате данных.")
    return objects
#Задание 7
def print_stats(streamer):
    print("Стример:", streamer.nickname)
    print("Подписчиков:", streamer.subscribers)
    print(f"Всего донатов: {streamer.total_donates()}")
    print(f"Средний донат: {round(streamer.average_donate(), 1)}\n")
    
    
a2 = Streamer("GolubKin", 1200 , [100 , 400 , 50])
a3 = Streamer("FrostMiron", 10000 , [200 , 500 , 2000])
s = [a , a2 , a3]
save_to_file(s , "data.txt")
s = []
s = load_from_file("data.txt")
for streamer in s:
    print_stats(streamer)
  
    
print("\nПроверка отсутствующего файла:")
missing = load_from_file("data_old.txt")
print("Загружено героев:", len(missing))
    
    
#Задание 8
PLAYER_FILE = "player.txt"
class Player:
    def __init__(self, name, points=0, level=1):
        self.name = name
        self.points = points
        self.level = level

    def to_line(self):
        return f"{self.name};{self.points};{self.level}"

def player_from_line(line):
    name, points, level = line.strip().split(";")
    return Player(name, int(points), int(level))

def save_player(player):
    with open(PLAYER_FILE, "w", encoding="utf-8") as f:
        f.write(player.to_line() + "\n")

def load_player():
    if not os.path.exists(PLAYER_FILE):
        return None
    try:
        with open(PLAYER_FILE, "r", encoding="utf-8") as f:
            line = f.readline()
        return player_from_line(line)
    except ValueError:
        return None

def show_player(player):
    print(f"Игрок: {player.name} | Очки: {player.points} | Уровень: {player.level}")
QUIZ = [
    ("Сколько будет 2 + 2 * 2?", ["4", "6", "8"], "1"),
    ("Какое животное не умеет летать?", ["орёл", "пингвин", "сова"], "1"),
    ("Столица Франции?", ["Париж", "Лондон", "Берлин"], "0"),
    ("Сколько минут в часе?", ["50", "60", "100"], "1"),
]
POINTS_PER_WIN = 10
POINTS_TO_LEVEL_UP = 50 

def play_round(player):
    """Один раунд: случайный вопрос викторины."""
    import random
    question, options, correct = random.choice(QUIZ)
    print("\nВопрос:", question)
    for i, option in enumerate(options):
        print(f"  {i}. {option}")
    answer = input("Твой ответ (цифра): ").strip()
    if answer == correct:
        print("Верно! +10 очков")
        player.points += POINTS_PER_WIN
    else:
        print("Неверно :( Очков нет, но раунд всё равно сохранён.")
    new_level = player.points // POINTS_TO_LEVEL_UP + 1
    if new_level > player.level:
        player.level = new_level
        print(f"Поздравляем! Новый уровень: {player.level}")
    save_player(player)
    show_player(player)


def game():
    """Главный цикл игры."""
    player = load_player()
    if player is None:
        name = input("Введи имя игрока: ").strip() or "Игрок"
        player = Player(name)
        save_player(player)
        print(f"Новая игра! Привет, {player.name}!")
    else:
        print(f"С возвращением, {player.name}! Очки: {player.points}")
        show_player(player)

    while True:
        answer = input("\nИграем ещё раунд? (да/нет): ").strip().lower()
        if answer == "да":
            play_round(player)
        elif answer == "нет":
            print("Пока! Прогресс сохранён :)")
            break
        else:
            print("Ошибка.")


if __name__ == "__main__":
    game()

#Задание 9
ans = input("Желаете открыть файл? (да/нет) ")
if ans == "да":
    a = input("Введите имя файла: ")
    try:
        with open(a, "r", encoding="utf-8") as f:
            b = f.read()
            print("Файл прочитан")
            print(b)
    except FileNotFoundError:
        print(f"Ошибка. Такого файла ({a}) не существует.")
    except PermissionError:
        print("Ошибка. Нет прав доступа.")
    except UnicodeDecodeError:
        print("Ошибка. Проблема с кодировуой")
elif ans == "нет":
    print("Тогда в другой раз.")
else:
    print("Ошибка. Введите да/нет.")

#Заданеи 10
# Формат хранения данных: одна запись (игрок) на одной строке.
# Поля внутри строки разделяются вертикальной чертой '|':
# никнейм|уровень|очки
#
# Почему выбран такой формат: Вертикальная черта '|' редко используется в обычном тексте и именах, в отличие от запятой (,), точки с запятой (;) или пробела.

def save(filename, players_data):
    with open(filename, "w", encoding="utf-8") as file:
        for player in players_data:
            line = f"{player['nickname']}|{player['level']}|{player['score']}\n"
            file.write(line)

def load(filename):
    players_data = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:  
                continue
                
            parts = clean_line.split("|")
            player = {
                "nickname": parts[0],
                "level": int(parts[1]),
                "score": int(parts[2])
            }
            players_data.append(player)
    return players_data

players = [
    {"nickname": "Shadow;Hunter", "level": 15, "score": 4200},
    {"nickname": "Pro_Gamer,2026", "level": 8, "score": 1550},
    {"nickname": "THEMaster,gg", "level": 8, "score": 1550}    
]

save("players_stats.txt", players)
loaded_players = load("players_stats.txt")
print(loaded_players)
        