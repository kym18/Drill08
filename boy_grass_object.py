from pico2d import *
import random


# Game object class here
class Grass:  # 클래스이름은 대문자로 시작하는 명사
    def __init__(self):  # 생성자함수
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Ball1:  # 클래스이름은 대문자로 시작하는 명사
    def __init__(self):  # 생성자함수
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 700), 599

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y >= 30:
            self.y -= 5



class Ball2:  # 클래스이름은 대문자로 시작하는 명사
    def __init__(self):  # 생성자함수
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 599
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= 5


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
    global team1
    global team2
    global world1  # 현재 월드에 존재하는 모든객체 담은 리스트
    global world2 # 현재 월드에 존재하는 모든객체 담은 리스트

    running = True
    world1 = []
    world2 = []

    grass = Grass()  # class를 이용해서 객체를 찍어냄
    world1.append(grass)
    world2.append(grass)

    team1 = [Ball1() for i in range(10)]
    team2 = [Ball2() for i in range(10)]
    world1 += team1
    world2 += team2


def render_world():
    clear_canvas()
    # grass.draw()  # self는 클래스 안 함수정의할때만. (호출할ㄷ떈 없음)
    # for boy in team:
    #     boy.draw()
    for o in world1:
        o.draw()
    for o in world2:
        o.draw()
    update_canvas()


def update_world():
    # grass.update()
    # for boy in team:
    #     boy.update()
    for o in world1:
        o.update()
    for o in world2:
        o.update()


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
