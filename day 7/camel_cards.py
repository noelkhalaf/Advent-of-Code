with open("D:\Projects\Python Testing\Advent of Code\day 7\input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

cards_dict = {
    "J" : 1, # Comment for part 2
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "T" : 10,
    # "J" : 11, # Uncomment for part 1
    "Q" : 12,
    "K" : 13,
    "A" : 14,
}

def isFiveOfAKind(hand):
    if hand[0]*5 == hand:
        return True
    return False

def isFourOfAKind(hand):
    if hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
        return True
    return False

def isFullHouse(hand):
    if len(set(hand)) != 2:
        return False
    curr_card_count = 0
    for card in hand:
        if card == hand[0]:
            curr_card_count += 1
    if curr_card_count == 2 or curr_card_count == 3:
        return True
    return False

def isThreeOfAKind(hand):
    if len(set(hand)) != 3:
        return False
    for card in hand:
        if hand.count(card) == 3:
            return True
    return False

def isTwoPair(hand):
    if len(set(hand)) != 3:
        return False
    flag = False
    for card in hand:
        if hand.count(card) == 2:
            flag = True
    if flag and len(set(hand)) == 3:
        return True
    return False

def isOnePair(hand):
    if len(set(hand)) == 4:
        return True
    return False

def findDuplicateCards(hand):
    rank_count = {}
    duplicates = []
    for card in hand:
        rank = card
        if rank in rank_count:
            if rank_count[rank] == 1:
                duplicates.append(cards_dict[rank])
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1
    return duplicates

def sortDetailedHands(hands):
    for i in range(len(hands) - 1):
        for j in range(5):
            curr_hand_suit = cards_dict[hands[i][0][j]]
            next_hand_suit = cards_dict[hands[i + 1][0][j]]
            if curr_hand_suit > next_hand_suit:
                hands[i], hands[i + 1] = hands[i + 1], hands[i]
                break
            elif curr_hand_suit < next_hand_suit:
                break
        for j in range(i, 0, -1):
            for k in range(5):
                curr_hand_suit = cards_dict[hands[j][0][k]]
                prev_hand_suit = cards_dict[hands[j - 1][0][k]]
                if curr_hand_suit < prev_hand_suit:
                    hands[j], hands[j - 1] = hands[j - 1], hands[j]
                    break
                elif curr_hand_suit > prev_hand_suit:
                    break
    return hands

def countTotalWinnings(hands):
    sum = 0
    for i, hand in enumerate(hands):
        sum += int(hand[1]) * (i + 1)
    return sum

def firstHalf():
    sum = 0
    five_of_a_kinds = []
    four_of_a_kinds = []
    full_houses = []
    three_of_a_kinds = []
    two_pairs = []
    one_pairs = []
    high_cards = []
    hands = [line.split()[0] for line in lines]
    bids = [line.split()[1] for line in lines]
    while hands:
        hand = hands[-1]
        if isFiveOfAKind(hand):
            five_of_a_kinds.append([hands.pop(), bids.pop(), cards_dict[hand[0]]])
        elif isFourOfAKind(hand):
            four_of_a_kinds.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        elif isFullHouse(hand):
            full_houses.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        elif isThreeOfAKind(hand):
            three_of_a_kinds.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        elif isTwoPair(hand):
            two_pairs.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        elif isOnePair(hand):
            one_pairs.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        else:
            high_cards.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])

    five_of_a_kinds = sortDetailedHands(five_of_a_kinds)
    four_of_a_kinds = sortDetailedHands(four_of_a_kinds)
    full_houses = sortDetailedHands(full_houses)
    three_of_a_kinds = sortDetailedHands(three_of_a_kinds)
    two_pairs = sortDetailedHands(two_pairs)
    one_pairs = sortDetailedHands(one_pairs)
    high_cards = sortDetailedHands(high_cards)
    all_cards = high_cards + one_pairs + two_pairs + three_of_a_kinds + full_houses + four_of_a_kinds + five_of_a_kinds
    sum = countTotalWinnings(all_cards)
    print("sum:", sum)

def secondHalf():
    sum = 0
    five_of_a_kinds = []
    four_of_a_kinds = []
    full_houses = []
    three_of_a_kinds = []
    two_pairs = []
    one_pairs = []
    high_cards = []
    hands = [line.split()[0] for line in lines]
    bids = [line.split()[1] for line in lines]
    while hands:
        hand = hands[-1]
        hand_replaced_j = hand
        hand_mappings = {card:hand.count(card) for card in hand}
        if "J" in hand_mappings.keys() and hand_mappings["J"] != 5 and hand_mappings["J"] > 0:
            hand_mappings["J"] = 0
            most_appearing_card = max(hand_mappings, key=hand_mappings.get)
            hand_replaced_j = hand_replaced_j.replace("J", most_appearing_card)

        if isFiveOfAKind(hand_replaced_j):
            five_of_a_kinds.append([hands.pop(), bids.pop(), cards_dict[hand[0]]])
        elif isFourOfAKind(hand_replaced_j):
            four_of_a_kinds.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        elif isFullHouse(hand_replaced_j):
            full_houses.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        elif isThreeOfAKind(hand_replaced_j):
            three_of_a_kinds.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        elif isTwoPair(hand_replaced_j):
            two_pairs.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        elif isOnePair(hand_replaced_j):
            one_pairs.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])
        else:
            high_cards.append([hands.pop(), bids.pop(), findDuplicateCards(hand)])

    five_of_a_kinds = sortDetailedHands(five_of_a_kinds)
    four_of_a_kinds = sortDetailedHands(four_of_a_kinds)
    full_houses = sortDetailedHands(full_houses)
    three_of_a_kinds = sortDetailedHands(three_of_a_kinds)
    two_pairs = sortDetailedHands(two_pairs)
    one_pairs = sortDetailedHands(one_pairs)
    high_cards = sortDetailedHands(high_cards)
    all_cards = high_cards + one_pairs + two_pairs + three_of_a_kinds + full_houses + four_of_a_kinds + five_of_a_kinds
    sum = countTotalWinnings(all_cards)
    print("sum:", sum)

#firstHalf()
secondHalf()