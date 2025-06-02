import requests

# Predefined dataset for sustainability and fallback
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Fetch real-time data from CoinGecko
def get_crypto_data():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
        response = requests.get(url, params={"ids": "bitcoin,ethereum,cardano"})
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        print("\n📡 Real-time crypto prices:")
        for coin in data:
            print(f"{coin['name']} - ${coin['current_price']} (Trend: {'rising' if coin['price_change_percentage_24h'] > 0 else 'stable'})")
        return {coin['id'].capitalize(): {"current_price": coin['current_price'], "price_change_24h": coin['price_change_percentage_24h']} for coin in data}
    except Exception as e:
        print(f"Oops, couldn't fetch real-time data: {e}. Using fallback data! 😎")
        return None

def cryptobuddy():
    print("Yo, what's good? I am CryptoBuddy, your crypto advisor! ")
    print("Ask me stuff like 'Which coin is trending?' or 'What's the greenest coin?'")
    print("Type 'help' for tips or 'exit' to bounce. ⚡ Crypto is risky—DO YOUR OWN RESEARCH! ⚡")

    # Fetch real-time data
    api_data = get_crypto_data()

    while True:
        user_query = input("\nWhat's your vibe? ").lower()

        if user_query == "exit":
            print("Peace out! Catch you on the blockchain! ✌️")
            break

        if user_query == "help":
            print("💡 CryptoBuddy can help with:")
            print("- Trending coins: 'trending,' 'hot coin,' 'moon,' 'bullish,' 'up,' 'profitable'")
            print("- Sustainable coins: 'sustainable,' 'green,' 'eco,' 'environment,' 'planet-friendly'")
            print("- Long-term picks: 'long-term,' 'growth,' 'future,' 'investment,' 'hold,' 'HODL'")
            print("- General: 'best coin,' 'recommend,' 'which coin'")
            continue

        # Query for trending coins (profitability: rising price, high market cap)
        if any(keyword in user_query for keyword in ["trending", "trending up", "hot coin", "moon", "bullish", "up", "profitable"]):
            if api_data:
                trending_coins = [
                    coin for coin, data in api_data.items()
                    if data["price_change_24h"] > 0
                ]
                if trending_coins:
                    print(f"🚀 {trending_coins[0]} is mooning at ${api_data[trending_coins[0]]['current_price']}! Up {api_data[trending_coins[0]]['price_change_24h']:.2f}% in 24h! Go get it, but DYOR! 🌙")
                else:
                    print("No coins are trending up right now. Try sustainable picks! 🤔")
            else:
                trending_coins = [
                    coin for coin in crypto_db
                    if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"
                ]
                if trending_coins:
                    print(f"🚀 {trending_coins[0]} is mooning with a rising trend and high market cap! Go get it, but DYOR! 🌙")
                else:
                    print("No coins are trending up with high market cap right now. Try sustainable picks! 🤔")

        # Query for sustainable coins (low energy use, sustainability score > 7/10)
        elif any(keyword in user_query for keyword in ["sustainable", "eco-friendly", "green", "eco", "environment", "planet-friendly"]):
            sustainable_coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            if crypto_db[sustainable_coin]["sustainability_score"] > 7/10:
                print(f"🌱 {sustainable_coin} is the greenest pick with a sustainability score of {crypto_db[sustainable_coin]['sustainability_score']*10}/10! Invest for the planet! 🌍")
            else:
                print("No super sustainable coins (score > 7/10) right now. Check back later! 😎")

        # Query for long-term growth (rising trend and sustainability)
        elif any(keyword in user_query for keyword in ["long-term", "growth", "future", "investment", "hold", "hodl"]):
            long_term_coins = [
                coin for coin in crypto_db
                if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["sustainability_score"] > 7/10
            ]
            if long_term_coins:
                print(f"📈 {long_term_coins[0]} is your long-term champ! Rising prices and eco-friendly vibes! 🚀 DYOR, fam!")
            else:
                print("No coins match both rising trends and high sustainability. Try something else! 🤙")

        # General recommendation (best coin, recommend, which coin)
        elif any(keyword in user_query for keyword in ["best coin", "recommend", "which coin", "buy now"]):
            long_term_coins = [
                coin for coin in crypto_db
                if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["sustainability_score"] > 7/10
            ]
            if long_term_coins:
                print(f"📈 {long_term_coins[0]} is the best pick right now! Rising prices and eco-friendly vibes! 🚀 DO YOUR OWN RESEARCH fam!")
            else:
                print("No top picks match both rising trends and high sustainability. Try trending or sustainable queries! 🤙")

        else:
            print("Hmmm, not sure what you mean. Try 'trending,' 'green,' 'investment,' 'best coin,' or 'help' for tips! 😎")

# Run the chatbot
if __name__ == "__main__":
    cryptobuddy()