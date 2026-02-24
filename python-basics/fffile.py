try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Sumting wong when writing to the file")
  finally:
    f.close()
except:
  print("Sumting wong when writing to the file") 