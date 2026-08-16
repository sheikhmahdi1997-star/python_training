def analyse_scores(scores):

    max_score= max(scores)
    min_score= min(scores)
    average_score= round(sum(scores) / len(scores))

    return{
        "Max":max_score,
        "Min":min_score,
        "Average":average_score
    }

student_scores=[10,12,13.5,12,14,18]
print(analyse_scores(student_scores))