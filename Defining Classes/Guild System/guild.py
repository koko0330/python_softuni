from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'

        if not player.guild == 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {player.guild}'

    def kick_player(self, player_name: str):
        if player_name in [p.name for p in self.players]:
            player = [p for p in self.players if p.name == player_name][0]
            player.guild = 'Unaffiliated'
            self.players.remove(player)
            return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        guild_inf = f'Guild: {self.name}' + '\n'

        player_inf = [f"{p.player_info()}" for p in self.players]

        return guild_inf + '\n'.join(player_inf)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())