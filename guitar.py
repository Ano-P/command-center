import csv
import sys
def guitar_log():
    try:
      song,time,Technique,date = get_input()
      write(song, time, Technique, date)
    except ValueError as error:
      print(f"\n[Error] {error}")


def get_input():
    song = input("Song: ").strip().lower()
    if song.isdigit() or song == "":
          raise ValueError("This format is not allowed for songs")
    
    time = input("Time: ").strip()
    if not time.isdigit():
          raise ValueError("A number is required")
    else:
          time = int(time)  
    Technique = input("Technique: ").strip()
    if Technique.isdigit() or Technique == "":
         raise ValueError("This format is not allowed for technique")

    date = input("Date: ").strip()
    
    return song,time,Technique,date


def guitar_stats():
   with open("guitar.csv") as gr: #Guitar reader
      reader = csv.DictReader(gr)
      for row in reader:
         print(row)



def write(song,time,Technique,date):
     with open("guitar.csv", "a") as gl: #Guitar log
          guitar_writer = csv.DictWriter(gl, fieldnames=["song", "time", "Technique", "date"], lineterminator="\n")
          guitar_writer.writerow({"song": song, "time": time, "Technique": Technique, "date": date})


