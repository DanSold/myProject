import schedule


def wakes_up():
    print('Its already seven oclock. Get up!')


def sends_goodnight_wishes():
    print('Good night')


def start():
    schedule.every().monday.at('07:00').do(wakes_up)
    schedule.every().tuesday.at('07:00').do(wakes_up)
    schedule.every().wednesday.at('07:00').do(wakes_up)
    schedule.every().tuesday.at('07:00').do(wakes_up)
    schedule.every().friday.at('07:00').do(wakes_up)
    schedule.every().day.at('22:00').do(sends_goodnight_wishes)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    start()
