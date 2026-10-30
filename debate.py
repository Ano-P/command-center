import sys
import csv

def debate_log():
   try:
      motion, time, personaldifficulty = get_input()
      write(motion, time, personaldifficulty)
   except ValueError as error:
      print(f"\n[Error] {error}")
   
    

def get_input(): #Input with exception handling
   motion = input("Motion: ").strip()
   if motion.isdigit() or motion == "":
      raise ValueError("This format is not allowed for motions")

   time = input("Time: ").strip()
   if not time.isdigit():
      raise ValueError("A number is required")
   else:
      time = int(time)  
   personaldifficulty = input("Difficulty: ").strip()
   if not personaldifficulty.isdigit():
      raise ValueError("A number is required")
   else:
      personaldifficulty = int(personaldifficulty)
   if not 1 <= personaldifficulty <= 10:
      raise ValueError("Difficulty must be between 1 and 10")

   return motion, time, personaldifficulty                                                                                            


def write(motion, time, personaldifficulty):
    with open("debate.csv", "a") as dl: #Debate log
     debate_writer = csv.DictWriter(dl, fieldnames=["motion", "time", "personaldifficulty"], lineterminator="\n")
     debate_writer.writerow({"motion": motion, "time": time, "personaldifficulty": personaldifficulty})


def debate_stats():
   with open("debate.csv") as dr: #Debate reader
      reader = csv.DictReader(dr)
      for row in reader:
         print(row)
      





