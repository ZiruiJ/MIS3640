from datetime import datetime


def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
    # when is my birthday this year?
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # if it has gone by, when will it be next year
    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)

    # subtraction on datetime objects returns a timedelta object
    delta = next_birthday - today
    return delta.days    


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    person1 =datetime.date(*b1)
    person2 =datetime.date(*b2)

    age_diff= - (person1- person2)

    p1= int(age_diff.days)
    p2= 0

    while p2*2 !=p1:
        p1 +=1
        p2 +=1
    double_day= person2 + datetime.timedelta (days= p2)


def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week
    today = datetime.today()
    print (today.weekday())
    print(today.strftime('%A'))

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1997, 9, 17)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2018, 12, 25)
    b2 = datetime(2018, 11, 1)
    print('Double Day', end=' ')
    print(double_day(b1, b2))

def main():
    datetime_exercises()

if __name__ == '__main__':
    main()
