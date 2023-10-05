from pico2d import *


# Game object class here
class Grass: #클래스이름은 대문자로 시작하는 명사
    def __init__(self): #생성자함수
        self.image = load_image('grass.png')


    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass

    running = True
    grass = Grass()  # class를 이용해서 객체를 찍어냄

def render_world():
    clear_canvas()
    grass.draw() #self는 클래스 안 함수정의할때만. (호출할ㄷ떈 없음)
    update_canvas()


def update_world():
    grass.update()
    pass


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # 객체들의 상호작용 결과 업뎃
    render_world()
    delay(0.05)
# finalization code

close_canvas()
