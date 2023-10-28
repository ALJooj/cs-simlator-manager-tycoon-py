'''
класс Команда.
функционал:
-создавать карточку команды где храниться
--инфа игрков
--деньги
--имя команды
--статистика игр против других команд
--любимые/не любимые карты
-способность менять состав
-изменять кол-во денег
-изменять любимые не любимые карты
-изменять имя команды
----- принимает на вход -----
имя
деньги
состав из классов игроков
список топа карт
'''
import os


def get_player_from_txt(link):
    f = open(link, 'r')
    s = f.readlines()
    pars = []
    vals = []
    for i in s:
        if i == '\n':
            pass
        first, last = i.split()
        pars.append(first)
        vals.append(last)

    f.close()
    return Player(vals[0], int(vals[1]), int(vals[2]))  # True if vals[2] == 'True' else False)


def get_team_from_txt(link):
    a = open(link, 'r')
    s = a.readlines()
    players = []
    args = []
    dsa = []
    x = 0
    while x < len(s):
        if 'player' in s[x]:
            temp = []
            for i in range(x + 1, x + 4):
                temp.append(s[i][:-1])
            x += 4
            players.append(Player(temp[0], int(temp[1]), int(temp[2])))#True if temp[2] == 'True' else False))

        elif s[x] == '\n':
            pass
        else:
            if s[x][:-1].endswith('}'):
                filt = ['[', ']', '{', '}']
                asd = list(filter(lambda x: x not in filt and (x.isdigit() or x == ' '), s[x][:-1]))
                dsa = ''.join(asd).split()
                dsa = [int(i) for i in dsa]
            first, *last = s[x][:-1].split()
            args.append(last)

        x += 1
    a.close()
    team = Team(args[0][0], int(args[1][0]), players, dsa)
    return team


def write(link, first_col, *args):
    f = open(link, 'w')
    for i in range(len(first_col)):
        if type(args[i]) == Player:
            f.writelines([first_col[i], '\n'])
            f.writelines([args[i].get_name(), '\n'])
            f.writelines([str(args[i].get_automatic_skill()), '\n'])
            f.writelines([str(args[i].get_awp_skill()), '\n'])
        else:
            f.write(first_col[i] + str(args[i]))
        f.write('\n')
    f.close()


class Team:
    def __init__(self, name, money, players, maps):
        self.name = name
        self.money = money
        self.players = players
        self.maps = maps
        self.par = ['name: ', 'player1: ', 'player2: ',
                    'players3: ', 'money: ', 'fav_maps: ']
        self.path = self.name + '.txt'
        write(self.path, self.par, self.name, *players, self.money, str(Map(self.maps)))

    #  money
    def get_money(self):
        return self.money

    def change_money_to(self, val):
        self.money += int(val)
        write(self.path, self.par, self.name, *self.players, self.money, self.maps)

    def __irshift__(self, other):
        self.money = int(other)

    def __rshift__(self, other):
        self.money += int(other)
    #

    #  имя
    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name
        self.path = self.name + '.txt'
        write(self.path, self.par, self.name, *self.players, self.money, self.maps)
    #

    #  состав
    def get_players(self):
        return [i.get_name() for i in self.players]

    def change_player(self, old_p, new_p):
        if old_p not in self.players:
            return False
        if type(new_p) == str:
            return False
        self.players.remove(old_p)
        self.players.append(new_p)
        write(self.path, self.par, self.name, *self.players, self.money, self.maps)
    #

    #  карты
    def get_maps(self, n=7):
        if n > 7:
            return False
        return Map(self.maps[:n])

    def change_maps(self, new_arr):
        self.maps = new_arr
        write(self.path, self.par, self.name, *self.players, self.money, self.maps)

    def change_map(self, old_m, new_m):
        if old_m not in self.maps:
            return False
        self.maps.remove(old_m)
        self.maps.append(new_m)
        write(self.path, self.par, self.name, *self.players, self.money, self.maps)

    def __eq__(self, other):
        if self.maps != other.maps:
            return False
        if self.name != other.name:
            return False
        if self.money != other.money:
            return False
        for i in range(3):
            if self.players[i].get_name() != other.players[i].get_name():
                return False
            if self.players[i].get_automatic_skill() != other.players[i].get_automatic_skill():
                return False
            if self.players[i].get_awp_skill() != other.players[i].get_awp_skill():
                return False
        return True

    def __str__(self):
        return self.name
    #

    #

    def describe(self):
        pass

# класс Игрок
# функционал:
# -создает карточку игрока в которой храниться:
# авп или нет
# --имя
# --очки скилла
# --слава
# -способность менять очки скилла
# -способность менять очки славы
# --- принимает на вход ---
# имя
# скилл
# деньги
# awp/not awp


class Player:
    def __init__(self, name, skill, skill_awp):
        self.name = name
        self.skill_automatic = skill
        self.skill_awp = skill_awp
        self.par = ['name: ', 'skill_automatic: ', 'skill_awp: ']
        self.path = self.name + '.txt'
        write(self.path, self.par, self.name, self.skill_automatic, self.skill_awp)

    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name
        self.path = self.name + '.txt'
        write(self.path, self.par, self.name, self.skill_automatic, self.skill_awp)

    def get_automatic_skill(self):
        return self.skill_automatic

    def change_automatic_skill(self, delta_val_automatic):
        self.skill_automatic += delta_val_automatic
        write(self.path, self.par, self.name, self.skill_automatic, self.skill_awp)

    def get_awp_skill(self):
        return self.skill_awp

    def change_awp_skill(self, delta_val):
        self.skill_awp = delta_val
        write(self.path, self.par, self.name, self.skill_automatic, self.skill_awp)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.skill_automatic != other.skill_automatic:
            return False
        if self.skill_awp != other.skill_awp:
            return False
        return True


class Map:
    def __init__(self, args):
        self.maps = ['inferno','cache','train','overpass','mirage','dust2','nuke'] #  ['inferno', 'dust', 'overpass', 'nuke', 'cache', 'train', 'mirage']
        self.level = args

    def ai_bans(self, team1, team2):
        pass

    def __str__(self):
        d = ''
        for i in range(7):
            d += '[' + self.maps[i] + ' ' + str(self.level[i]) +']'
            d += ', '
        d = d[:-2]
        return '{' + d + '}'


Dev1ce = Player('Dev1ce', 1000, 2000)
Rain = Player('Rain', 900, 3000)
Oscar = Player('Oscar', 8900, 2500)
S1mple = Player('S1mple', 1100, 7900)
XyR9X = Player('XyR9X', 5000, 5000)
ColdZera = Player('ColdZera', 4250, 7100)

Renegades = Team('Renegades', 10000, [Dev1ce, Rain, Oscar], [1, 2, 3, 4, 5, 6, 7])
Renegades1 = get_team_from_txt('Renegades.txt')
G2A = get_team_from_txt('G2A.txt')


def picks_bans(team1, team2):
    pass


def fight(team1, team2, bo=1, *maps):
    pass