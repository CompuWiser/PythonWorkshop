# allowed papers: 100, 50, 10, 5, and rest of request

money = 500

request = 277


def req(amount, credit):
    while amount < credit:
        if amount >= 100:
            print("give 100")
            amount -= 100
            continue
        elif amount >= 50:
            print("give 50")
            amount -= 50
            continue
        elif amount >= 10:
            print("give 10")
            amount -= 10
            continue
        elif amount >= 5:
            print("give 5")
            amount -= 5
            continue
        else:
            print("give " + str(amount))
            break


req(277, money)
