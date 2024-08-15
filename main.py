# Target study time
study_time = float(input('Enter how long you want to study [h]: '))
TARGET = study_time * 3600


def ask_input():
    video_name = input('Enter video\'s name:')
    video_duration_min = int(input('Enter video\'s duration [min]: ')) * 60
    video_duration_sec = int(input('Enter video\'s duration [s]: '))
    return video_name, video_duration_min, video_duration_sec


def clear_file():
    with open('video_list.txt', 'r') as initial_file:
        content = initial_file.read()
        if content:
            with open('video_list.txt', 'w') as initial_file_rep:
                content2 = initial_file_rep.write('')
                print('yes', content2)


is_target_reached = True
titles_list = list()
total_sum = 0

while is_target_reached:
    clear_file()
    video = ask_input()
    if total_sum + sum(video[1:]) < TARGET:
        total_sum += sum(video[1:])

    else:
        is_target_reached = False
    with open('video_list.txt', 'a') as file:
        file.write(f'{video[0]}\n\n')

print(f'Video time for the day: {total_sum} [s]')
print(f'Video time for the day: {total_sum / 3600} [h]')
