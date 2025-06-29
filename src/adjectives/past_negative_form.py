from adjectives.past_form import past_form
from adjectives.negative_form import negative_form

def past_negative_form(input_adj):
    output_adj = input_adj.copy()
    output_adj = past_form(negative_form(output_adj))
    return output_adj
