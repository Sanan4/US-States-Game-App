import turtle
import pandas

# state_writer = turtle.Turtle()
# state_writer.hideturtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# new_turtle = turtle.Turtle()
# new_turtle.shape("turtle")
# new_turtle.hideturtle()
# score = 0
# is_game_on = True

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    # answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        # break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=("Arial", 6, "normal"))

# states_to_learn.csv

# for state in states:
#     if answer_state == state:
#         score += 1
#         correct_answers.append(state)
#
#
# while is_game_on:
#     answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
#     answer_state = answer_state.title()
#     for state in states:
#         if answer_state == state:
#             new_turtle.write(answer_state, move=False, align="left", font=("Arial", 8, "normal"))
#             score += 1
#             correct_answers.append(state)
#             # print(type(new_turtle.goto(data[data["state"] == state] == "x", data[data["state"] == state] == "y")))
#             # new_turtle.goto(data[data["state"] == state] == "x", data[data["state"] == state] == "y")

