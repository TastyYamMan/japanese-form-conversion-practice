def status_check(deck, language):
    statuses = {'in' : [0]*5, 'out': [0]*5}
    for card in deck:
        if language == '日本語':
            status_id = card['word'].j_to_e_revision_status_id
        else:
            status_id = card['word'].e_to_j_revision_status_id
        
        if status_id is None:
            statuses[card['status']][0] += 1
        else:
            statuses[card['status']][status_id + 1] += 1
    
    output = ''
    for card_status in statuses:
        output += '\n'
        status_counts = statuses[card_status]
        output += card_status + ' |'
        for status_id, status_count in enumerate(status_counts):
            if status_id == 0:
                output += f' null:{status_count} |'
            else:
                output += f' {status_id - 1}:{status_count} |'
        
    print(output)
    print(f"in_count : {sum(statuses['in'])} | out_count: {sum(statuses['out'])}")
    print()

def deck_size(deck):
    cards = 0
    for card in deck:
        if card['status'] == 'in':
            cards += 1
    return cards