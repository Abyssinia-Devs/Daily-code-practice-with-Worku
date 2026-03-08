def bottle(fullbottel, excbottle):
    drink = fullbottel
    empty_bottle = fullbottel
    
    exchange = excbottle
    while empty_bottle >= exchange:
        new_full = empty_bottle // exchange
        
        drink += new_full
        
        empty_bottle = new_full + empty_bottle % exchange
    return drink
        
        
numBottles = 15
numExchange = 4
print(bottle(numBottles, numExchange))