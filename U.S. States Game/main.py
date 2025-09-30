import turtle
import pandas
from state_writer import StateWriter

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

state_writer = StateWriter()
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = pandas.DataFrame([state for state in data["state"].values if state not in guessed_states])
        missing_states.to_csv("states_to_learn.csv")
        break
    if answer_state in data["state"].values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data["state"] == answer_state]
        state_x, state_y = state_data["x"].item(), state_data["y"].item()
        state_writer.write_state(state_x, state_y, state_data["state"].item())



