# Basketball Quiz

> A short quiz to test how much you know about basketball.

## Overview

This program is a basketball knowledge quiz. It asks the user five questions about basketball and gives them three answer choices for each question. The user's answers are used in conditional statements to determine if they are correct. Each correct answer adds one point to the user's score. At the end, the program shows the user's final score out of five and gives them a message based on their score.

## Sample Questions and Responses

1. Who has the most NBA championships as a player?

   1. Bill Russell
   2. Michael Jordan
   3. LeBron James

2. How many points is a three pointer worth?

   1. 1 point
   2. 2 points
   3. 3 points

3. Which team does Stephen Curry play for?

   1. Los Angeles Lakers
   2. Golden State Warriors
   3. Boston Celtics

4. How many players from one team are on the court at one time?

   1. 5 players
   2. 6 players
   3. 7 players

5. Which position usually brings the ball up the court?

   1. Center
   2. Point guard
   3. Power forward

## Variables

* `score` (int): keeps track of the user's total score. One variable works because there is only one final score.

* `answer1` (str): stores the user's answer to the first question.

* `answer2` (str): stores the user's answer to the second question.

* `answer3` (str): stores the user's answer to the third question.

* `answer4` (str): stores the user's answer to the fourth question.

* `answer5` (str): stores the user's answer to the fifth question.

## Conditional Logic Outline

* **Conditional statement 1**: Checks the user's answer to the question about who has the most NBA championships.

  * `if` the response is 1: display a correct message and add 1 point to `score`.
  * `else`: display an incorrect message and give the correct answer.

* **Conditional statement 2**: Checks how many points a three pointer is worth.

  * `if` the response is 3: display a correct message and add 1 point to `score`.
  * `else`: display an incorrect message and give the correct answer.

* **Conditional statement 3**: Checks which team Stephen Curry plays for.

  * `if` the response is 2: display a correct message and add 1 point to `score`.
  * `else`: display an incorrect message and give the correct answer.

* **Conditional statement 4**: Checks how many players from one team are on the court.

  * `if` the response is 1: display a correct message and add 1 point to `score`.
  * `else`: display an incorrect message and give the correct answer.

* **Conditional statement 5**: Checks which position usually brings the ball up the court.

  * `if` the response is 2: display a correct message and add 1 point to `score`.
  * `else`: display an incorrect message and give the correct answer.

* **Conditional statement 6**: Determines the final message based on the user's score.

  * `if` the score is 5: display a message saying the user got a perfect score.
  * `elif` the score is greater than or equal to 3: display a message saying the user knows a lot about basketball.
  * `elif` the score is greater than or equal to 1: display a message saying the user knows some basketball.
  * `else`: display a message encouraging the user to learn more about basketball.

## How to Run

1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video

[Add your 5-minute explanation video link here]
