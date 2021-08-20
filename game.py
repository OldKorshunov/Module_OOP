import exceptions as exc
import models as mod
import settings as set


def play():
    name = input("Введите имя: ")
    level = 1
    player = mod.Player(name)
    enemy = mod.Enemy(level)
    comm = None
    while comm != 'exit':
        try:
            comm = input("*************************************************\nВведите start для начала игры или help для вывода списка комманд!\n->")
        except:
            print('Такой комманды не существует. Введите help!')
        else:
            if comm == 'start':
                try:
                    player.attack(enemy)
                    player.defence(enemy)
                except exc.EnemyDownExceptions:
                    level += 1
                    enemy = mod.Enemy(level)
                    player.score += 5
                    print('Player lives: ', player.lives,'Enemy lives: ', enemy.lives, '| Score: ', player.score)
            elif comm == 'help':
                print('Allowed commands: ', set.ALLOWED_COMMANDS)
            elif comm == 'show scores':
                with open('scores.txt', 'r') as f:
                    for line in f:
                        print(line)
            elif comm == 'exit':
                print('Exit...')
            else:
                print('Такой комманды не существует. Введите help!')
    

if __name__ == "__main__":
    try:
        play()
    except exc.GameOver:
        print("Game Over!")
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
