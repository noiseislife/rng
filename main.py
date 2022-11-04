import random

dice_sides = 6
dice_count = 3
roll_count = 100000
dice_monitor = [0] * dice_sides

def roll_dice(sides, count):
    global dice_monitor
    roll_total = 0
    for cnt in range(count):
        dice_roll = random.randrange(sides)
        dice_monitor[dice_roll] += 1
        roll_total += dice_roll + 1
    return roll_total


def main():
    random.seed(1)
    global dice_monitor
    global dice_sides
    global dice_count
    global roll_count
    rand_cnt = [0] * (dice_sides * dice_count)
    cnt = 0
    while cnt < roll_count:
        rand_cnt[roll_dice(dice_sides, dice_count) - 1] += 1
        cnt += 1
    print('Number of rolls: %s' % roll_count)
    print('Single die distribution: %s' % dice_monitor)
    print('Distribution for %sd%s:' % (dice_count, dice_sides))
    cnt = dice_count - 1
    scale = 1
    max_roll_count =  max(rand_cnt)
    scale_threshold = 60
    if max_roll_count > scale_threshold:
        scale = max_roll_count // scale_threshold
    while cnt < len(rand_cnt):
        x = rand_cnt[cnt]
        bar_count = (max(1, x // scale))
        if x == 0:
            bar_count = 0
        print("%s - %s:%s" % (str(cnt+1).rjust(2), str(x).rjust(len(str(max_roll_count))), '#' * bar_count))
        cnt += 1
    #print(rand_cnt)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
