# We are given a ball-by-ball cricket score. Dravid and Sachin are the 2 batsmen playing. Dravid bats the first ball. We have to calculate the total score of both players.
# Note: After odd runs, strike changes, and other player gets to bat. After 6 balls also strike changes. Assume there aren’t any wide/no balls or wickets taken.
# Example Input array : [ 1, 2, 4, 1, 3, 1, 1, 4, 6, 0, 0, 1, 1, 1, 2, 1, 0, 6, 0, 0, 1, 2, 1, 0, 0, 4, 0, 1, 0 ]

def calculate_scores(input_scores):
    strike = 0
    dravid_score = 0
    sachin_score = 0

    for ball_idx, _ in enumerate(input_scores, start=0):
        if ball_idx == 0:
            dravid_score += input_scores[ball_idx]
            if input_scores[ball_idx] % 2 != 0:
                strike = 1

        if input_scores[ball_idx] % 2 == 0:
            if strike == 0:                
                dravid_score += input_scores[ball_idx]

            else :
                sachin_score += input_scores[ball_idx]

        if input_scores[ball_idx] % 2 != 0:
            if strike == 0:
                strike = 1
                dravid_score += input_scores[ball_idx]

            else :
                strike = 0
                sachin_score += input_scores[ball_idx]
                
        if ball_idx % 6 == 0:
            if strike == 0:
                strike = 1
                dravid_score += input_scores[ball_idx]

            else:
                strike = 0
                sachin_score += input_scores[ball_idx]

    return sachin_score, dravid_score

if __name__ == "__main__":
    input_scores = [ 1, 2, 4, 1, 3, 1, 1, 4, 6, 0, 0, 1, 1, 1, 2, 1, 0, 6, 0, 0, 1, 2, 1, 0, 0, 4, 0, 1, 0 ]
    sachin_score, dravid_score = calculate_scores(input_scores)
    print(f"sachin_score : {sachin_score} dravid_score : {dravid_score}")
