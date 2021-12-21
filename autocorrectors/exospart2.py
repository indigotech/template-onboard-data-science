import hashlib


# user_id = salt + str(user_id)
# user_id = user_id.encode(encoding)
# user_id = sha256(user_id).digest()
# user_id = base64.b64encode(user_id).decode(encoding)

def part2exo2(rows, columns, nbresults):
    right_hashed_answer = 'caa27da5d078708b1596b44cd98a4d4aac95b0b2fbdfc98b2ce762c8024d0ed3'
    received_answer = rows + columns + nbresults
    received_answer = received_answer.encode('utf-8')
    received_answer = hashlib.sha256(received_answer).hexdigest()

    if received_answer == right_hashed_answer:
        print("Good job!")
    else:
        print("Oups, try again! Check your calculations on the dataframe size and your answer on the SQL task")

# def part2exo4(answer):
    # rightanswer = 43.90552325581396
    # if answer > rightanswer - 0.1 and answer < rightanswer + 0.1:
    #     print("Good job!")
    # else:
    #     print("Oups, try again!")
def part2exo4(answerculmen, answersql):
    right_hashed_answer = '7e9d8f203a2b39b6162dc4bea6777c5b467a4aa0d09450b8b938772b6c2b0a71'
    received_answer = answerculmen + answersql
    received_answer = received_answer.encode('utf-8')
    received_answer = hashlib.sha256(received_answer).hexdigest()

    if received_answer == right_hashed_answer:
        print("Good job!")
    else:
        print("Oups, try again! Check your calculations on the mean culmen and your answer on the SQL task")

def part2exo10(hcorr, lcorr, option):
    right_hashed_answer = '76def36b6c04b63501605a739335355070e842957c52d3796f209185183547db'
    received_answer = hcorr + lcorr + option
    received_answer = received_answer.encode('utf-8')
    received_answer = hashlib.sha256(received_answer).hexdigest()

    if received_answer == right_hashed_answer:
        print("Good job!")
    else:
        print("Oups, try again! Check your calculations on the correlation matrix and your answer on the SQL task")
