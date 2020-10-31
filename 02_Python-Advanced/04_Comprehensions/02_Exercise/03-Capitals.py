country = input().split(", ")
capital = input().split(", ")

country_and_capital = zip(country, capital)

country_and_capital = {country : capital for(country,capital) in country_and_capital}

{print(f"{country} -> {capital}") for country , capital in country_and_capital.items()}

