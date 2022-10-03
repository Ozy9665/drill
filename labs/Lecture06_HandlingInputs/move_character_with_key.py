from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    # fill here
    global running
    global xdir, ydir, stop_dir, x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                xdir += 1
                stop_dir = 1
            elif event.key == SDLK_LEFT:
                xdir -= 1
                stop_dir = 0
            elif event.key == SDLK_UP:
                ydir += 1
            elif event.key == SDLK_DOWN:
                ydir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                xdir -= 1
            elif event.key == SDLK_LEFT:
                xdir += 1
            elif event.key == SDLK_UP:
                ydir -= 1
            elif event.key == SDLK_DOWN:
                ydir += 1


def draw_character():
    global xdir, ydir, x, y, stop_dir
    if xdir == 0:
        if stop_dir == 1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif stop_dir == 0:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif xdir == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif xdir == -1:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)


open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
xdir = 0
ydir = 0
stop_dir = 1


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_character()
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if x <= 1250 and x >= 30:
        x += xdir * 10
    else:
        x += (-xdir) * 25
    if y <= 1000 and y >= 30:
        y += ydir * 10
    else:
        y += (-ydir) * 25
    delay(0.01)

close_canvas()

