def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        sentence = ''
        letter = []
        cnt = 1

        for j in range(0, len(s), i):
            letter.append(s[j:j + i])
        # print(letter)

        standard = letter[0]
        for k in range(1, len(letter)):
            if not standard:
                standard = letter[k]
                cnt += 1
            else:
                if letter[k] == standard:
                    cnt += 1
                else:
                    if cnt != 0 and cnt != 1:
                        sentence += str(cnt) + standard
                        cnt = 1
                        standard = letter[k]
                    else:
                        sentence += standard
                        cnt = 1
                        standard = letter[k]
        else:
            if cnt != 0 and cnt != 1:
                sentence += str(cnt) + standard

            else:
                sentence += standard

        # print(sentence)
        # print(len(sentence))
        if len(sentence) < answer:
            answer = len(sentence)

    return answer

print(solution('aabbaccc'))