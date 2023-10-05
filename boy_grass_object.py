from pico2d import *

# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()


def reset_world():
    global running
    running = True


# initialization code
reset_world()


def render_world():
    clear_canvas()
    update_canvas()


# game main loop code
while running:
    handle_events()
    update_world() #객체들의 상호작용 결과 업뎃
    render_world()
    delay(0.05)
# finalization code

close_canvas()
