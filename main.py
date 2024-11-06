#lendo e tratando dados CSV.

f = open("games_steam.csv")
for line in f:
    print(line.strip().split(","))

#criando classe Game e atribuindo condição para Games gratuitos (games com preço = 0.0).

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

    def calculate_counts(self): 
        for game in self.games:
            if game.is_free():
                self.free_count += 1
            else:
                self.paid_count += 1

    def get_free_paid_percentage(self):
        total = self.free_count + self.paid_count
        free_percentage = (self.free_count / total) * 100 if total else 0
        paid_percentage = (self.paid_count / total) * 100 if total else 0
        return free_percentage, paid_percentage

    def __str__(self):
        free_percentage, paid_percentage = self.get_free_paid_percentage()
        return f"PERGUNTA 1) Qual o percentual de jogos gratuitos e pagos na plataforma? RESPOSTA >>> Jogos gratuitos: {free_percentage:.2f}% | Jogos pagos: {paid_percentage:.2f}%"


#criando a classe YearAnalysis e método calculate_year_counts para calcular a quantidade de Games lançados por ano.

class YearAnalysis:
    def __init__(self, games):
        self.games = games
        self.year_counts = {}
        self.calculate_year_counts()

    def calculate_year_counts(self):
        for game in self.games:
            if game.release_year in self.year_counts:
                self.year_counts[game.release_year] += 1
            else:
                self.year_counts[game.release_year] = 1

    def get_year_with_most_new_games(self):
        max_games = max(self.year_counts.values(), default=0)
        most_popular_years = [year for year, count in self.year_counts.items() if count == max_games]
        return most_popular_years

    def __str__(self):
        years = self.get_year_with_most_new_games()
        return f"PERGUNTA 2) Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados. RESPOSTA >>> Anos(s) com maior número de novos jogos: {', '.join(map(str, years))}"


#criando classe PaidGamesByYear que responde a pergunta individual do projeto: "Qual a média dos preços dos jogos pagos filtrados por ano de lançamento?" 


class PaidGamesByYear:
    def __init__(self, games, release_year=None):
        self.games = games
        self.release_year = release_year

#Filtrando os jogos pagos do ano especificado
  
    def average_price(self):
        filtered_games = [
            game for game in self.games
            if game.price > 0 and (self.release_year is None or game.release_year == self.release_year)
        ]

        total_price = sum(game.price for game in filtered_games)
        total_paid_games = len(filtered_games)

        return total_price / total_paid_games if total_paid_games else 0

    def __str__(self):
        return f"PERGUNTA 3) Qual a média dos preços dos jogos pagos filtrados por ano de lançamento? RESPOSTA >>> Preço médio dos jogos pagos lançados em {self.release_year if self.release_year else 'qualquer ano'}: R${self.average_price():.2f}"

