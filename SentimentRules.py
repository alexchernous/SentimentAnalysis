class SentimentRules:
    rules = {r'(like|love|enjoy)':'class_pos',
            r'(dislike|hate|dread)':'class_neg'}


class IntentRules:
    rules = {r'((make.+reserv.+?(?=\s))|(reserv.+make(?=\s)))|(reserve)':'class_res_make',
             r'((change|fix|augment|tweak).+?reserv.+?(?=\s)|reserv.+?(change|fix|augment|tweak)(?=\s))':'class_res_change'}