
#lendo e tratando dados csv

f = open ("games_steam.csv")
for line in f:
  print (line.strip().split(","))

#criando classe Game e atribuindo condição para Games gratuitos, games que não são gratuitos tem valor acima de 0.0.

class Game:
  def __init__(self, name, price, release_year):
      self.name = name
      self.price = price
      self.release_year = release_year

  def is_free(self):
      return self.price == 0.0

#criando a classe FreePaidAnalysis que calcula o percentual de Games gratuitos e pagos.

class FreePaidAnalysis:
  def __init__(self, games):
      self.games = games
      self.free_count = 0
      self.paid_count = 0
      self.calculate_counts()

#o metodo calculate_counts faz a contagem dos Games gratuitos e pagos.
  
  def calculate_counts(self): 
      for game in self.games:
          if game.is_free():
              self.free_count += 1
          else:
              self.paid_count += 1

#o metodo get_free_praid_percentage faz a contagem dos Games gratuitos e pagos e __str__ retorna o percentual de Games gratuitos e pagos.
  
  def get_free_paid_percentage(self):
      total = self.free_count + self.paid_count
      free_percentage = (self.free_count / total) * 100 if total else 0
      paid_percentage = (self.paid_count / total) * 100 if total else 0
      return free_percentage, paid_percentage

  def __str__(self):
      free_percentage, paid_percentage = self.get_free_paid_percentage()
      return f"Jogos gratuitos: {free_percentage:.2f}% | Jogos pagos: {paid_percentage:.2f}%"
