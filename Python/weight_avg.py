'''
weighted average for discrete structures.

-Omar Barazanji-
'''

participation = 0.05
practice_probs = 0.05
quizzes = 0.20
test1 = 0.15
test2 = 0.20
final_exam = 0.35

def avg(array):
    sum = 0.0
    for x in array:
        sum += x
    average = sum / len(array)
    return average

quiz_scores = [75.0,83.0]
quiz_avg = avg(quiz_scores)
print('Quiz average: %s' % quiz_avg)

test2_predicted = input('Test 2: ')
final_predicted = input('Final exam: ')

grade = (100.0)*participation \
    + (100.0)*practice_probs \
    + quiz_avg*quizzes \
    + (14.5/22.0)*test1 \
    + test2_predicted*test2 \
    + final_predicted*final_exam

print('Your grade will be a: %s' % grade)
