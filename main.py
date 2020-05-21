
print("I am a Delta Dental DevOps engineer");

# Below is the input string
input = '5,8,10:30,11:30'
input_split = input.split(',')
#validating corner case to check the inputs
if float(input_split[2].replace(':','.')) >= float(input_split[3].replace(':','.')) :
    print("Invalid Input--> start time of the meeting is after the end-time or length of meeting 0 mins")
    quit()



#this function will merge the possible intevals of conf rooms availabilities and appends them to input meeting time
def possible_split_meetings(temp_list, input_split):

    temp_list_sorted = dict(sorted(temp_list.items()))
    schedules = []
    for item in temp_list_sorted.keys():
        schedules.append(list(item))
    print(schedules)
    print(temp_list_sorted.get(tuple(schedules[0])))
    merged_list = []
    result_dict = {}
    # for schedule in schedules:
    #     if not merged_list or merged_list[-1][1] < schedule[0]:
    #         merged_list.append(schedule)
    #         result_dict[schedule[0]] = list(temp_list_sorted.get(tuple(schedules[0])))
    #     else:
    #         merged_list[-1][1] = max(merged_list[-1][1], schedule[1])
    #         result_dict.get(schedule[0]).append(temp_list_sorted.get(tuple(schedules[0])))
    #
    #
    # for x in range(0, len(merged_list)):
    #     if merged_list[x][0] <= float(input_split[2].replace(':', '.')) and merged_list[x][1] >= float(input_split[3].replace(':', '.')):
    #         print( merged_list[x]  )
    #         return True
    return False

# This defines the structure for room with room number, capacity and list of available times
class Room:

    def __init__(self, room_number,max_capacity, schedules):
        #self.name = name    # instance variable unique to each instance
        self.room_number = room_number
        self.max_capacity = max_capacity
        self.schedules = schedules

#this function is just for our reference to see print all information about a particular room.
    def room_print(self):
        print("room number: ", self.room_number , "max_caapcity:", self.max_capacity, "schedule is ", self.schedules)





# Using readlines() to read rooms.txt in the same location of this file.
file1 = open('rooms.txt', 'r')
Lines = file1.readlines()

# List to store room objects created from each line of the room.txt file
room_list = []

# Strips the newline character
for line in Lines:
    line_split = line.split(",");
    rows, cols = (int((len(line_split)-2)/2), 2)
    temp_schedule = [[0 for i in range(cols)] for j in range(rows)]
    index = 0
    for x in range(2, len(line_split),2):
        temp_schedule[index][0] = float(line_split[x].replace(':','.'));
        temp_schedule[index][1] = float(line_split[x+1].replace(':','.'));
        index += 1
    temp = Room(float(line_split[0]),float(line_split[1]),temp_schedule)
    room_list.append(temp) #appending room object to room_list


# initializing result to infinity and later on assigned to closest distance meeting room
result = float("inf")
input_floor_number = float(input_split[1].replace(':', '.')) #input floot number
temp_list = {} #creating a temp_list to store all the rooms_schedules with room_numbers eligible for our input team size
for room in room_list:
    if room.max_capacity >= float(input_split[0]):
        for x in range(0,len(room.schedules)):
            temp_list[room.schedules[x][0],room.schedules[x][1]] = room.room_number
            if room.schedules[x][0] <= float(input_split[2].replace(':','.')) and  room.schedules[x][1] >= float(input_split[3].replace(':','.')):
                if abs(input_floor_number-room.room_number) < abs(input_floor_number-result):
                    result = room.room_number

# print(temp_list)
if result == float("inf") :
    if len(temp_list) == 0 :
        print("team size is bigger than any conference room. No room can be allocated")
    else:
        print("No single slot conf rooms available. Hence we need need to check if it is possible to split meetings and assign rooms")
        print("tmep list has all meeting rooms with accepted capacity")
        print("Now check if spliting is possible")
        if possible_split_meetings(temp_list, input_split) :
            print("spliting meeting room is possible")
        else:
            print("spliting also not possible")

else:
    print( "Your conference room number is: ",result)




