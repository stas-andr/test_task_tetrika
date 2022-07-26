import itertools


def prepare_data(intervals):
    """Записваем исходные данные по времени в отсортированный массив кортежей (time, flag)
    time - время окончания (flag == 1) или начала (flag == -1) интервала"""
    prepared_data = []
    for key, interval in intervals.items():
        prepared_data += list (zip (interval, itertools.cycle ((-1, 1)), [key] * len(interval)))
    prepared_data =  sorted(prepared_data)
    for elem in prepared_data:
        print (elem, sep='\n')
    return prepared_data


def appearance(intervals):
    prepared_data = prepare_data(intervals)
    prev_flag, prev_time, time_start, time_end, sum_time = 0, 0, 0, 0, 0
    lesson_started = False
    for (time, flag, user) in prepared_data:
        flag = prev_flag + flag
        if flag == -3:
            time_start = time
            lesson_started = True
        elif lesson_started:
            time_stop = time
            sum_time += (time_stop - time_start)
            lesson_started = False
        prev_flag = flag
    return sum_time




tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       if i == 1:
           i = 1
       test_answer = appearance(test['data'])
       print("\n")
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
