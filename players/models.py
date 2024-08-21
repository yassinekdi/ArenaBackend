from django.db import models

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    bankroll = models.IntegerField()
    hand = models.JSONField()
    is_active = models.BooleanField(default=True)
    phase_bet = models.IntegerField()
    total_game_bet = models.IntegerField()
    best_hand = models.CharField(max_length=255)
    ai_flag = models.BooleanField(default=False)

class PlayerMetrics(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    total_games = models.IntegerField()
    win_rate = models.FloatField()
    avg_bet = models.FloatField()
    nb_folds = models.IntegerField()
    nb_checks = models.IntegerField()
    nb_bets = models.IntegerField()
    nb_calls = models.IntegerField()
    total_bets = models.IntegerField()
    total_win_money = models.IntegerField()
    total_loose_money = models.IntegerField()
