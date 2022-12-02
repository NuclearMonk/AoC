def read_elves(stream):
    calorie_total = 0
    for line in stream.readlines(): #for every line in the file
        if not line.strip(): # if the line is empty
            yield calorie_total #yield the total for this elf
            calorie_total = 0 #reset it for the next elf
        else:
            calorie_total+=int(line) #increment the total for this elf
    
def find_max_x_calories(f,x): #Reads the sum of the highest x calories
    calories = [x for x in read_elves(f)] #list all elves calories total
    calories.sort(reverse=True) #sort from highest to lowers
    return sum(calories[0:x]) #take the sum of the x highest calories

def day1_one_liner(f,x):
    print(sum(sorted(read_elves(f),reverse=True)[:x]))

if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        day1_one_liner(f,3)