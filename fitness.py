import sys
import csv


def fitness_router():
    try:
        first_ask = input("Circuit or Run? ").strip().lower()
        if first_ask == "circuit":
            second_ask = input("Log or Stats? ").strip().lower()
            if second_ask == "log":
                log_circuit()
            elif second_ask == "stats":
                stats_circuit()
            else:
                raise ValueError("Input has to be log or stats")

        elif first_ask == "run":
            second_ask = input("Log or Stats? ").strip().lower()
            if second_ask == "log":
                log_run()
            elif second_ask == "stats":
                stats_run()
            else:
                raise ValueError("Input has to be either log or stats")
        else:
            raise ValueError("Input has to be either circuit or run")

    except ValueError as error:
        print(f"\n[Error] {error}")

def log_circuit():
    try:
        exercise, reps, sets, difficulty = circuit_input()
        circuit_write(exercise, reps, sets, difficulty)
    except ValueError as error:
        print(f"\n[Error] {error}")
        sys.exit(1)

def circuit_input(): #logs the circuit and writes to it according to input
    exercise = input("Exercise: ").strip()
    if exercise.isdigit() or exercise == "":
      raise ValueError("This format is not allowed for exercise")

    reps = input("Reps: ").strip()
    if not reps.isdigit():
      raise ValueError("A number is required")
    else:
       reps = int(reps)

    sets = input("Sets: ").strip()
    if not sets.isdigit():
      raise ValueError("A number is required")
    else:
       sets = int(sets)
    
    difficulty = input("Difficulty: ").strip()
    if not difficulty.isdigit():
      raise ValueError("A number is required")
    else:
      difficulty = int(difficulty)
    if not 1 <= difficulty <= 10:
      raise ValueError("Difficulty must be between 1 and 10")
    return exercise,reps,sets,difficulty

def circuit_write(exercise,reps,sets,difficulty):
  with open("circuit.csv", "a") as cl: #circuit log
         circuit_writer = csv.DictWriter(cl, fieldnames=["exercise", "reps", "sets", "difficulty"], lineterminator="\n")
         circuit_writer.writerow({"exercise": exercise, "reps": reps, "sets": sets, "difficulty": difficulty})



def stats_circuit():
    with open("circuit.csv") as cr: #Debate reader
      reader = csv.DictReader(cr)
      for row in reader:
         print(row)



def log_run():
    try:
      pace, distance, time = run_input()
      run_write(pace,distance,time)
    except ValueError as error:
      print(f"\n[Error] {error}")
      sys.exit(1)


def run_input():
   pace = input("Pace: ").strip()
   if pace.isdigit() or pace == "":
         raise ValueError("This format is not allowed for pace")
   
   distance = input("Distance: ").strip()
   if not distance.isdigit():
         raise ValueError("A number is required")
   else:
          distance = int(distance)
   
   time = input("Time: ").strip()
   if not time.isdigit():
         raise ValueError("A number is required")
   else:
          time = int(time)
       
   return pace,distance,time



def run_write(pace,distance,time):
    with open("run.csv", "a") as rl: #Run log
     run_writer = csv.DictWriter(rl, fieldnames=["pace", "distance", "time"], lineterminator="\n")
     run_writer.writerow({"pace": pace, "distance": distance, "time": time})




def stats_run():
    with open("run.csv") as sr:
      reader = csv.DictReader(sr)
      for row in reader:
         print(row)

if __name__ == "__main__":
    fitness_router()

