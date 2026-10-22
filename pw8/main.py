from test import load_data, save_data, saver

data = load_data("student_data.pkl.gz")
if data is None:
  print("No pickled data found. Loading from scores.csv...")
  import pandas as pd

  data = pd.read_csv("scores.csv")

saver.wait_till_finished()
print("Program exited safely.")