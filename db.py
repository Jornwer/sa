import peewee

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