start = "On the"
day = "day of christmas my true love gave to me "
dayIndex = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh",
            "twelfth")
end = ""
first = "a partidge in a pear tree."
second = "two turtle doves"
third = "three french hens,"
fourth = "four calling birds,"
fifth = "five golden rings,"
sixth = "six geese a laying,"
seventh = "seven swans a swimming,"
eighth = "eight maids a milking,"
ninth = "nine ladies dancing,"
tenth = "ten lords a leaping,"
eleventh = "eleven pipers piping,"
twelfth = "twelve drummers drumming,"
i = 0
while (i < 8):
    if (i == 0):
        print(start, dayIndex[i], day, first, "\n")
    elif (i == 1):
        print(start, dayIndex[i], day, second, "and", first, "\n")
    elif (i == 2):
        print(start, dayIndex[i], day, third, second, "and", "\n", first, "\n")
    elif (i == 3):
        print(start, dayIndex[i], day,fourth, third, "\n", second, "and", first, "\n")
    elif (i == 4):
        print(start, dayIndex[i], day, fifth, fourth, "\n", third, second, "and", first, "\n")
    elif (i == 5):
        print(start, dayIndex[i], day, sixth, fifth, "\n", fourth, third, second, "and", first, "\n")
    elif (i == 6):
        print(start, dayIndex[i], day, seventh, sixth, "\n", fifth, fourth, third, second, "\n", "and", first, "\n")
    elif (i == 7):
        print(start, dayIndex[i], day,eighth, seventh, "\n", sixth, fifth, fourth, third, "\n", second, "and",
              first, "\n")
    elif (i == 8):
        print(start, dayIndex[i], day, ninth, eighth, "\n", seventh, sixth, fifth, fourth, "\n", third, second, "and",
              first, "\n")
    elif (i == 9):
        print(start, dayIndex[i], day, tenth, ninth, "\n", eighth, seventh, sixth, fifth, "\n", fourth, third, second,
              "and", first, "\n")
    elif (i == 10):
        print(start, dayIndex[i], day, eleventh, tenth, "\n", ninth, eighth, seventh, sixth, "\n", fifth, fourth, third,
              second, "\n", "and", first, "\n")
    elif (i == 11):
        print(start, dayIndex[i], day, twelfth, eleventh, "\n", tenth, ninth, eighth, seventh, "\n", sixth, fifth,
              fourth, third, "\n", second, "and", first, "\n")

    i = i + 1
