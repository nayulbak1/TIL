import sys; sys.stdin=open('2056.txt', 'r')

calendar = {'01':'31', '02':'28', '03':'31', '04':'30', '05':'31', '06':'30', '07':'31', '08':'31', '09':'30', '10':'31', '11':'30', '12':'31'}
T = int(input())
for tc in range(T):
    N = input()
    if N[4:6] not in calendar.keys():
        print('#{} {}'.format(tc+1, -1))
    else:
        if N[6:8] > calendar[N[4:6]]:
            print('#{} {}'.format(tc + 1, -1))
        if N[6:8] <= calendar[N[4:6]] and int(N[6:8]) > 0:
            date = N[0:4] + '/' + N[4:6] + '/' + N[6:8]
            print('#{} {}'.format(tc+1, date))