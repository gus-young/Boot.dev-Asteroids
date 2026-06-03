import pygame
import sys
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import player
import asteroid
import asteroidfield
import shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #add classes to group
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    shot.Shot.containers = (shots, drawable, updatable)

    #create scene
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    user_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    live_asteroid_field = asteroidfield.AsteroidField()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_running = True

    while game_running: 
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for member in asteroids:
            if user_player.collides_with(member):
                log_event("player_hit")
                game_running = False
            for bullet in shots: 
                if bullet.collides_with(member):
                    bullet.kill()
                    member.split()
                    log_event("asteroid_shot")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    while game_running == False: 
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                return
        screen.fill("black")
        my_font = pygame.font.SysFont('Arial', 75)
        my_font_small = pygame.font.SysFont('Arial', 25)
        text_surface_one = my_font.render('Game Over', True, (255, 255, 255))
        text_rect_one = text_surface_one.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(text_surface_one, text_rect_one)
        text_surface_two = my_font_small.render('Press Any Key to Close', True, (255, 255, 255))
        text_rect_two = text_surface_two.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
        screen.blit(text_surface_two, text_rect_two)
        pygame.display.flip()


if __name__ == "__main__":
    main()
