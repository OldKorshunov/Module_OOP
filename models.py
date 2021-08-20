from random import randint


import settings as set
import exceptions as exc


class Enemy:
    def __init__(self, level):
        self.level = self.lives = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives  == 0:
            raise exc.EnemyDownExceptions()


class Player:
    def __init__(self, name, lives=set.LIFE_CONST, score=0, allowed_at=set.ALLOWED_ATTACKS):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_at

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        elif attack == 1 and defense == 2 or attack == 2 and defense == 3 or attack == 3 and defense == 1:
            return 1
        elif attack == 1 and defense == 3 or attack == 2 and defense == 1 or attack == 3 and defense == 2:
            return -1
        else: return 'wtf'


    def decrease_lives(self):
        self.lives -= 1
        if self.lives  == 0:
            exc.GameOver.save_score(self.name, self.score)
            raise exc.GameOver() 


    def attack(self, enemy_obj):
        while True:
            try:
                player_attack = int(input("Выберите персонажа для защиты: \nВолшебник - введите 1;\nВоин - введите 2;\nРазбойник - введите 3\n->"))
                
            except ValueError:
                print("Ввод должен состоять из 1, 2 или 3!!!")
                pass
            else:
                if player_attack in self.allowed_attacks:
                    break
                elif player_attack is None:
                    print("Ввод должен состоять из 1, 2 или 3!!!")
                else: 
                    print("Ввод должен состоять из 1, 2 или 3!!!")
        
        enemy_attack = Enemy.select_attack()

        res = Player.fight(player_attack, enemy_attack)

        if res == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        elif res == -1:
            print("You missed!")
        elif res == 0:
            print("It's a draw!")
        else: print("What happend?")


    def defence(self, enemy_obj):
        while True:
            try:
                player_attack = int(input("Выберите персонажа для защиты: \nВолшебник - введите 1;\nВоин - введите 2;\nРазбойник - введите 3\n->"))
                
            except ValueError:
                print("Ввод должен состоять из 1, 2 или 3!!!")
                pass
            else:
                if player_attack in self.allowed_attacks:
                    break
                elif player_attack is None:
                    print("Ввод должен состоять из 1, 2 или 3!!!")
                else: 
                    print("Ввод должен состоять из 1, 2 или 3!!!")
        
        enemy_attack = Enemy.select_attack()

        res = Player.fight(enemy_attack, player_attack)

        if res == 1:
            print("Enemy attacked successfully!")
            Player.decrease_lives(self)
        elif res == -1:
            print("Enemy missed!")
        elif res == 0:
            print("It's a draw!")
        else: print("What happend?")
