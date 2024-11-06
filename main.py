
#lendo e tratando dados csv

f = open ("games_steam.csv")
for line in f:
  print (line.strip().split(","))