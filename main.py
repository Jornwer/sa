import click
import os
import peewee
import time
import datetime
from dateutil import parser

heroes = {
    '0': 'Archer',
    '1': 'Huntress',
    '2': 'Forest Mage',
    '3': 'Druid',
    '4': 'Giant',
    '5': 'Ghoul',
    '6': 'Necromancer',
    '7': 'Crypt Fiend',
    '8': 'Shade',
    '9': 'Butcher',
    '10': 'Water Elem',
    '11': 'Shaman',
    '12': 'Witcher',
    '13': 'BomberMan',
    '14': 'Golem',
    '15': 'Lizard',
    '16': 'Shadow Lord',
    '17': 'Dryad',
    '18': 'Ice Troll',
    '19': 'Minotaur',
    '20': 'Skeleton Mage',
    '21': 'Skeleton Archer',
    '22': 'Arachnid',
    '23': 'Murloc',
    '24': 'Warlock',
    '25': 'Mystical Tauren',
    '26': 'Trent',
    '27': 'Vampire',
    '28': 'Red Warlock',
    '29': 'Priest',
    '30': 'Banshee',
    '31': 'Naga',
    '32': 'Wolf',
    '33': 'Hound',
    '34': 'Knight',
    '35': 'Goblin',
    '36': 'Cultist',
    '37': 'Wizard',
    '38': 'Grant',
    '39': 'Phanto',
}

player_map = {
    'Jornwer': 'marisha',

    'GOGOJoeriJonaEC': 'Alllayar',
    'piskadron_kun': 'Alllayar',

    'Johor': 'Gohor',
    'Gowhore': 'Gohor',
    'SABot': 'Gohor',

    'LightInfernal': 'fredber227',
    'Astarot1': 'fredber227',
    'ValeraVarulIl': 'fredber227',
    'mamatkunem': 'fredber227',

    'modeKorolek': 'Taxelor',
    'Krakolek': 'Taxelor',
    'KurokawaAkane': 'Taxelor',

    'govno4': 'KoroRain',
    'modeTaxelorejke': 'KoroRain',
    'DragonsHuyagons': 'KoroRain',
    'EtoZheKoro': 'KoroRain',
    'Taxevor': 'KoroRain',

    'AncientWORLD.': 'AncientWORLD',

    'DragonsLayer': 'DragonsLover',
    'Закрыто': 'DragonsLover',

    'Taza4to': 'The_NEXT_LVL',

    'JackFartGame': 'Andatra',

    'OtbelivatelZada': 'Andoral',

    'K1mal4ik': 'K1mall',

    'Oткpыто': 'GressKo',
    'PussyEater2': 'GressKo',

    'SAHYAKAMEHb': '333as555',

    'SonyaMarmelad': 'ValeraVarulll',

    'alex322': 'alexayka',

    'fyefhfr': 'Koktel',

    'D_J107': 'SA_Killer69',

    'PruPru(7)': 'ImperatorPruPru',
    'PruPru(6)': 'ImperatorPruPru',

    'Quiet Rain': '_G_',
    'Barrad': '_G_'
}

database_proxy = peewee.Proxy()

class BaseModel(peewee.Model):
    class Meta:
        database = database_proxy

class Match(BaseModel):
    id = peewee.AutoField(primary_key=True)
    file = peewee.TextField(unique=True)
    winner = peewee.TextField(choices=('red', 'blue'))
    created_at = peewee.DateField()
    player_count = peewee.IntegerField()
    time = peewee.IntegerField()
    red_tower  = peewee.IntegerField()
    blue_tower  = peewee.IntegerField()
    dragon_one  = peewee.IntegerField()
    dragon_two  = peewee.IntegerField()
    dragon_three  = peewee.IntegerField()
    dragon_four  = peewee.IntegerField()
    dragon_five  = peewee.IntegerField()

class Player(BaseModel):
    id = peewee.AutoField(primary_key=True)
    game = peewee.ForeignKeyField(Match, related_name='players')
    team = peewee.TextField(choices=('red', 'blue'))
    winner = peewee.BooleanField()
    order  = peewee.IntegerField()
    name = peewee.TextField()
    hero = peewee.TextField()
    kills  = peewee.IntegerField()
    deaths  = peewee.IntegerField()
    skillshot_damage  = peewee.IntegerField()
    magic_damage  = peewee.IntegerField()
    pure_damage  = peewee.IntegerField()
    damage_taken  = peewee.IntegerField()
    damage_blocked  = peewee.IntegerField()
    healed_self  = peewee.IntegerField()
    healed_ally  = peewee.IntegerField()
    healed_self_fight  = peewee.IntegerField()
    healed_ally_fight  = peewee.IntegerField()
    impact  = peewee.IntegerField()
    quest_completed  = peewee.IntegerField(null=True)
    quest_progress  = peewee.IntegerField(null=True)
    talents = peewee.TextField()
    item_one  = peewee.IntegerField(null=True)
    item_two  = peewee.IntegerField(null=True)
    item_three  = peewee.IntegerField(null=True)
    item_four  = peewee.IntegerField(null=True)
    item_five  = peewee.IntegerField(null=True)
    item_six  = peewee.IntegerField(null=True)

def init_db(path: str):
    db = peewee.SqliteDatabase(path)
    database_proxy.initialize(db)
    db.create_tables([Match, Player])

def process(path: str, output:str, from_date: int):
    create_db(output)
    read_files(path, from_date)

def create_db(output: str):
    if os.path.exists(output):
        os.remove(output)
    open(output, 'a').close()
    init_db(output)

def read_files(path: str, from_date: int):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            date = time.ctime(os.path.getctime(os.path.join(path, filename)))
            if from_date is not None:
                if datetime.datetime.now() > parser.parse(date) + datetime.timedelta(days=from_date):
                    continue
            print(filename, date)
            with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
                game = Match(file=filename, created_at=date, id=None)
                players = []
                player = Player(game=game)
                players.append(player)
                for line in file:
                    line = line.rstrip()
                    if line.startswith('winner=') or line.startswith('Winner='):
                        winner = line[7:]
                        if winner == '1' or winner == 'blue' or winner == 'Blue':
                            game.winner = 'blue'
                        elif winner == '0' or winner == 'red' or winner == 'Red':
                            game.winner = 'red'
                        else:
                            raise ValueError(f'Ахтунг - "{winner}"')
                    if line.startswith('playerCount='):
                        game.player_count = int(line[12:])
                    if line.startswith('time='):
                        game.time = int(line[5:])
                    if line.startswith('redTeamEngineeringBaseLevel='):
                        game.red_tower = int(line[28:])
                    if line.startswith('blueTeamEngineeringBaseLevel='):
                        game.blue_tower = int(line[29:])
                    if line.startswith('dragonsKilledBy[0]='):
                        game.dragon_one = int(line[19:])
                    if line.startswith('dragonsKilledBy[1]='):
                        game.dragon_two = int(line[19:])
                    if line.startswith('dragonsKilledBy[2]='):
                        game.dragon_three = int(line[19:])
                    if line.startswith('dragonsKilledBy[3]='):
                        game.dragon_four = int(line[19:])
                    if line.startswith('dragonsKilledBy[4]='):
                        game.dragon_five = int(line[19:])


                    if line.startswith('[player'):
                        if not line.startswith('[player1]'):
                            player = Player(game=game)
                            players.append(player)
                        player.order = int(line[7:-1])
                        player.team = 'red' if player.order <= game.player_count / 2 else 'blue'
                        player.winner = True if player.team == game.winner else False
                    if line.startswith('name='):
                        player.name = player_map.get(line[5:]) or line[5:]
                        if player.name == 'JackFastGame' and parser.parse(date) > parser.parse('03.01.2025'):
                            player.name = 'GressKo'
                    if line.startswith('heroId='):
                        player.hero = heroes.get(line[7:])
                    if line.startswith('kills='):
                        player.kills = int(line[6:])
                    if line.startswith('deaths='):
                        player.deaths = int(line[7:])
                    if line.startswith('skillshotDamage='):
                        player.skillshot_damage = int(line[16:])
                    if line.startswith('magicDamage='):
                        player.magic_damage = int(line[12:])
                    if line.startswith('pureDamage='):
                        player.pure_damage = int(line[11:])
                    if line.startswith('gotDamage='):
                        player.damage_taken = int(line[10:])
                    if line.startswith('blockedDamage='):
                        player.damage_blocked = int(line[14:])
                    if line.startswith('healedSelf='):
                        player.healed_self = int(line[11:])
                    if line.startswith('healedAlly='):
                        player.healed_ally = int(line[11:])
                    if line.startswith('healedSelfFight='):
                        player.healed_self_fight = int(line[16:])
                    if line.startswith('healedAllyFight='):
                        player.healed_ally_fight = int(line[16:])
                    if line.startswith('questTime='):
                        player.quest_completed = int(line[10:])
                    if line.startswith('questProgress='):
                        player.quest_progress = int(line[14:])
                    if line.startswith('impactPoints='):
                        player.impact = int(line[13:])
                    if line.startswith('talent='):
                        talents = []
                        i = int(line[7:])
                        c = 0
                        while i != 0:
                            if i % 2 == 1:
                                talents.append(c)
                            c += 1
                            i //= 2
                        player.talents = str(talents)
                    if line.startswith('item[0]='):
                        player.item_one = int(line[8:])
                    if line.startswith('item[1]='):
                        player.item_two = int(line[8:])
                    if line.startswith('item[2]='):
                        player.item_three = int(line[8:])
                    if line.startswith('item[3]='):
                        player.item_four = int(line[8:])
                    if line.startswith('item[4]='):
                        player.item_five = int(line[8:])
                    if line.startswith('item[5]='):
                        player.item_six = int(line[8:])

                if game.player_count % 2 == 1:
                    print('В игре "{filename}" нечетное количество игроков')
                    continue
                game.save()
                for p in players:
                    p.save()

@click.command()
@click.option('--path', '-p', help='Путь до папки', required=True)
@click.option('--output', '-o', help='Имя файла с базой', required=True)
@click.option('--from-date', '-f', help='Статистику за сколько дней собирать', type=int)
def main(path: str, output: str, from_date: int):
    if not os.path.isdir(path):
        print(f'Нет такой папки с файлами - "{path}"')
    else:
        process(path, output, from_date)

main()