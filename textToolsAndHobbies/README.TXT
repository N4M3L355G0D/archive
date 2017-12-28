id how fast computer can finish a acharacterspace segment
identify where the other slaves have completed
assign new slave to process segment

once segment is completed, halt, wait for slaves of same speed to finish, get new assignment from the first slave of similar speed added, cascade

everyone gets a segment of the character space with equal size according to how fast the computer is
slower computers pair together to create the equivalent of a faster computer's segment
the clustered slower computer segment will, when completed, jump to the next segment immediately after the faster computer segment, and the faster segment after the slower computer segment.

insert segment address in each for loop.
current version, as of Mon Feb 27 00:44:44 EST 2017, can do up to the 26 char characterspace


who ever reaches the end of his segment, will check the master completed segment list and select his segment according to the order of hosts having completed their segments, mark his completed segment as done, announce that he is starting a new segment, mark selected segment as taken, mark master completed segment list as running segment, begin segment


current version, as of Sat Mar  4 15:11:45 EST 2017, can do up to the 32 char characterspace

cluster manager will be written in python for cross -architecture operability

need to add argparse to num2ascii
need to add character based stop points in for loops to stop in character end string:
 take below in put into c-based macro
  ## pseudo-code
  take character combos = put into array;
   if array == end string:
    stop
    print end string
current version, as of Sun Mar  5 11:04:30 EST 2017, can do up to the 40 char characterspace
