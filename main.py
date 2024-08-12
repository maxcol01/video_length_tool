# Target study time
study_time = int(input('Enter how long you want to study [h]: '))
TARGET = study_time * 3600


def ask_input():
    video_name = input('Enter video\'s name:')
    video_duration_min = int(input('Enter video\'s duration [min]: ')) * 60
    video_duration_sec = int(input('Enter video\'s duration [s]: '))
    return video_name, video_duration_min, video_duration_sec


is_target_reached = True
titles_list = list()
total_sum = 0

while is_target_reached:
    video = ask_input()
    if total_sum + sum(video[1:]) < TARGET:
        total_sum += sum(video[1:])
    else:
        is_target_reached = False
    with open('video_list.txt', 'a') as file:
        file.write(f'{video[0]}\n\n')
