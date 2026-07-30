def check_student_status(*inputs):
    name=[]
    scores=[]
    for item in inputs:
        if isinstance(item,(int,float)):
            scores.append(item)
              
        else:
            name.append(item)
    

    if not scores:
        ave=0
        status="No Scores"

    else:
        average_scores= sum(scores)/len(scores)
        if average_scores > 0:
            status="Passed"
        if average_scores < 0:
            status="Failed"

    return{
        "name":name,
        "average":average_scores,
        "status":status
    }        
       
print(check_student_status("Ali", 15, 18, 12, 10))