import collections
import re


def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
             if word not in banned]

    #print(words)

    counts = collections.Counter(words)

    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))