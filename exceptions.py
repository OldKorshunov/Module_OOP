import operator


class GameOver(Exception):
    @staticmethod
    def save_score(name, new_scr=int):
        score = ()
        all_scores = {}
        sorted_tuples = ()
        keys = []
        count = 1

        
        with open('scores.txt', 'r') as f:
            for line in f:
                score = line.split()[1:]
                all_scores[score[0]]=int(score[1])
            f.close
                
        all_scores[name] = new_scr
        sorted_tuples = sorted(all_scores.items(), key=operator.itemgetter(1), reverse=True)
        sorted_scores = {k: v for k, v in sorted_tuples}
        keys = sorted_scores.keys()
        
        with open('scores.txt', 'w') as f:
            for el in keys:
                if count > 1:
                    f.write('\n')
                line = "%s) %s %s" % (count, el, sorted_scores[el])
                f.write(line)
                count += 1
            f.close


class EnemyDownExceptions(Exception):
    pass
