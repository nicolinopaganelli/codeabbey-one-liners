## Returns the some of as many numbers separated by a space as you'd like
# ex)
# IN: 1 2 3 4 5
# OUT: 15
print(sum(list(map(int, input('\n>> ').split(' ')))))
