from typing import List


class Tag:
    def __init__(self, asp, sent):
        self.aspect = asp
        self.sentiment = sent


def process_tags(tags_list: List[List[Tag]], review_list: List[str]):
    assert len(tags_list) == len(review_list)
    new_review = ''

    for ind, review in enumerate(review_list):
        tags = tags_list[ind]

        for sentence in review.replace('\n\n', '').replace('\n', '').split('. '):
            new_sentence = '<begin_a>'

            for tag in tags:
                new_sentence += '<' + tag.aspect + '::' + tag.sentiment + '>'

            new_sentence += '<end_a>'
            new_sentence += '<begin_s>' + sentence + '<end_s>'
            new_review += new_sentence
    return new_review


# example
# tag1 = Tag('food', 'pos')
# tag2 = Tag('service', 'neg')
# our_tags = [[tag1, tag2], [tag2], [tag1]]

# our_rev = ['I like fish in this restaraunt.', 'But I had been waiting for it very long.',
#            'I am sure that they need to change fix it.']

# print(' '.join(our_rev))
# print(process_tags(our_tags, our_rev))
