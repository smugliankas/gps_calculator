selection = input('What type of travel will you be making?: ')

if selection.lower() == 'walking':
    steps = int(input('Number of Steps: '))
    height = int(input('Your Height (in CM): '))
    avgspeed = input('Your Average Speed (leave blank for default 5 km/h): ')
    steplength = height * 0.414 / 100

    if avgspeed == '':
        avgspeed = 5
    else:
        avgspeed = int(avgspeed)

    distance = steps * steplength
    distancekm = distance / 1000
    durationmin = distancekm / avgspeed * 60
    hours = durationmin // 60
    minutes = durationmin % 60

    print('Distance:', round(distancekm, 2), 'KM')

    if hours == 0:
        print('Duration:', int(minutes), 'minutes')
    else:
        print('Duration:', int(hours), 'hours', int(minutes), 'minutes')


elif selection.lower() == 'vehicle' or selection.lower() == 'car':
    distance = int(input('How many KM is the journey?: '))
    speed = int(input('Your average speed: '))
    durationmin = distance / speed * 60
    hours = durationmin // 60
    minutes = durationmin % 60

    if hours == 0:
        print('Duration:', int(minutes), 'minutes')
    else:
        print('Duration:', int(hours), 'hours', int(minutes), 'minutes')


else:
    print('Invalid option, please type walking or vehicle.')