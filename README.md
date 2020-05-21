# Conference-room-scheduling
## Problem: 
Find the nearest open conference room for a team in which a team can hold its meeting.

## Approach: 
I tried to analyse the problem constraints and framed an algorithm which returns the room number that matches the criteria of team members. The algorithm does the following:
1. Reads the input text file, formats it and bind the values to the properties of room object like room number, max capacity of the room, open time schedules etc. We now have list of objects of type “Room” for each record in text file. Meeting Times are converted to double values so that it will be easy to compare the intervals. (Eg: 10:30 -> 10.30)
1. Iterate through the list of room objects and ignore the ones which has its capacity less than that of the team member size provided in input. If the room capacity is greater than or equal to the number of team members, iterate through open schedules of the room and check if the interval satisfies the time they want to meet. We have to do bookkeeping to check if this room number is closest to the floor in which team members work.
1. Return the closest room number (if any) obtained from above step. If we are unable to provide a single room that matches meeting time of team members, the algorithm tries to split the meeting across more than one room.


## Test Cases: 
Algorithm has been tested for various scenarios by considering number of team members, longer meeting times, rooms with random booking times, multiple rooms closest to the floor in which team members work etc. Testcase3 is still work in progress

Case 1.	Rooms.txt
```
8.43,7,11:30,12:30,17:00,17:30
9.511,9,9:30,10:30,12:00,12:15,15:15,16:15
9.527,4,9:00,11:00,14:00,16:00
Input: 11,7,10:30,11:30
Output: None
None of the rooms are available which can accommodate 11 members.
```
Case 2.	Rooms.txt
```
10.511,9,9:30,11:45,12:00,12:15,15:15,16:15
9.527,4,9:00,11:00,14:00,16:00
9.547,8,10;30,11:30,13:30,15:30,16:30,17:30
Input: 6,8,10:30,11:30 (6 team members working in 8th floor)
Output: 9.547
Rooms 10.511 and 9.547 are available for 6 team members in time slot 10:30 to 11:30. But, 9.547 is returned as it is close to 8th floor.
```
Case 3.	Rooms.txt
```
10.511,9,9,12:30,12:45,13:15,15:15,16:15
9.527,4,9:00,11:00,14:00,16:00
9.547,8,10;30,11:30,12:30,16:30,16:50,17:30
Input: 6,8,9:00,16:30 (6 team members working in 8th floor)
Output: 10.511,9.547
We can’t accommodate a single room for the time specified by team members. So, we split the meeting into 2 rooms.
Room no. 10.511 is available from 9:00 to 12:30
Room no. 9.547 is available from 12:30 to 16:30
```
