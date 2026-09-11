def avg_finder(markslist):
    avg=sum(markslist)/len(markslist)
    return avg
my_marks=[80, 70, 90, 60]
print(f"Average:{avg_finder(my_marks)}")