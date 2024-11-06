
#lendo e tratando dados csv

f = open ("games_steam.csv")
for line in f:
  print (line.strip().split(","))

#criando classe Game e atribuindo condição para Games gratuitos
#Games que não são gratuitos tem valor acima de 0.0
class Game:
  def __init__(self, name, price, release_year):
      self.name = name
      self.price = price
      self.release_year = release_year

  def is_free(self):
      return self.price == 0.0
