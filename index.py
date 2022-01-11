try:
    import pygame, sys, random
    from os import pipe
    from pygame.constants import BUTTON_RIGHT, K_SPACE
    from pygame.display import flip

    def draw_floor():
        screen.blit(floor,(floor_x_pos,550))
        screen.blit(floor,(floor_x_pos + 490,550))

    def create_pipe():
        random_pipe_pos = random.choice(pipe_height)
        bottom_pipe = pipe_surface.get_rect(midtop = (600,random_pipe_pos))
        top_pipe = pipe_surface.get_rect(midtop = (600,random_pipe_pos - 750))
        return bottom_pipe, top_pipe

    def move_pipe(pipes):
        for pipe in pipes:
            pipe.centerx -= 3.95
        return pipes

    def draw_pipe(pipes):
        for pipe in pipes:
            if pipe.bottom >= 600:
                screen.blit(pipe_surface,pipe)
            if pipe.top <= 10:
                flip_pipe = pygame.transform.flip(pipe_surface,False,True)
                screen.blit(flip_pipe,pipe)

    def check_collusion(pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                hit_sound.play()
                return False
            if bird_rect.top <= -75 or bird_rect.bottom >= 600:
                hit_sound.play()
                return False
        return True

    def rotate_bird(bird1):
        new_bird = pygame.transform.rotozoom(bird1,-bird_movement*4,1)
        return new_bird

    def score_display(game_state):
        if game_state == 'main_game':
            score_surface = game_font.render(str(int(score)),True,(255,255,255))
            score_rect = score_surface.get_rect(center = (245,100))
            screen.blit(score_surface,score_rect)
        if game_state == 'game_over':
            score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
            score_rect = score_surface.get_rect(center = (245,150))
            screen.blit(score_surface,score_rect)

            hight_score_surface = game_font.render(f'Hight Score: {int(hight_score)}',True,(255,255,255))
            hight_score_rect = hight_score_surface.get_rect(center = (245,400))
            screen.blit(hight_score_surface,hight_score_rect)


    def update_score(score,hight_score):
        if score > hight_score:
            hight_score = score
        return hight_score

    pygame.mixer.pre_init(frequency = 44100, size =- 16, channels = 2, buffer = 512)

    pygame.init()

    pygame.display.set_caption('flapy_bird_by_quang')

    screen = pygame.display.set_mode((490,600))
    clock = pygame.time.Clock()
    game_font = pygame.font.Font('04B_19.ttf',40)

    gravity = 0.25
    bird_movement = 0
    game_active = False
    score = 0
    hight_score = 0

    bg = pygame.image.load('your place to stay').convert()

    bird = pygame.image.load('your place to stay').convert_alpha()
    bird_rect = bird.get_rect(center = (245,300))

    floor = pygame.image.load('your place to stay').convert()
    floor_x_pos = 0

    pipe_surface = pygame.image.load('your place to stay').convert()
    pipe_list = []

    spawn_pipe = pygame.USEREVENT
    pygame.time.set_timer(spawn_pipe, 1500)
    pipe_height = [250,350,400]

    game_over_surface = pygame.image.load('your place to stay').convert_alpha()
    game_over_rect = game_over_surface.get_rect(center = (245,300))

    flap_sound = pygame.mixer.Sound('your place to stay')
    hit_sound = pygame.mixer.Sound('your place to stay')
    point_sound = pygame.mixer.Sound('your place to stay')
    point_sound_countdowwn = 100

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement =- 7.8
                    flap_sound.play()
                if event.key == K_SPACE and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (245,100)
                    bird_movement = 0
                    score = 0
            if event.type == spawn_pipe:
                pipe_list.extend(create_pipe())

        screen.blit(bg,(0,0))

        if game_active:
            bird_movement += gravity
            rotated_bird = rotate_bird(bird)
            bird_rect.centery += bird_movement
            screen.blit(rotated_bird,bird_rect)
            game_active = check_collusion(pipe_list)
            pipe_list = move_pipe(pipe_list)
            draw_pipe(pipe_list)
            score += 0.01
            score_display('main_game')
            point_sound_countdowwn -= 1
            if point_sound_countdowwn <= 0:
                point_sound.play()
                point_sound_countdowwn = 100
        else:
            screen.blit(game_over_surface,game_over_rect)
            hight_score = update_score(score,hight_score)
            score_display('game_over')

        floor_x_pos -= 1
        draw_floor()
        if floor_x_pos <= -490:
            floor_x_pos = 0
        
        pygame.display.update()
        clock.tick(120) 
    pygame.quit()

except Exception as bug:
    print(bug)

input()