import pygame
import sys

# No necesitas duplicar el tamaño de la ventana ni redefinir WIDTH y HEIGHT aquí.
pygame.init()
WIDTH, HEIGHT = 1280, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juegitungis")
font = pygame.font.SysFont("arial", 32)

# Carga de imágenes de jugador y enemigo (puedes reemplazar por tus propias imágenes)
player_img = pygame.Surface((80, 80))
player_img.fill((100, 200, 100))
enemy_img = pygame.Surface((80, 80))
enemy_img.fill((200, 100, 100))

class Enemy:
    def __init__(self, level):
        self.hp = 10 + level * 5
        self.attack = 3 + level
        self.defense = 1 + level // 2

def battle(player, enemy):
            battle_running = True
            message = ""
            action_selected = 0  # 0: atacar, 1: magia
            while battle_running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            action_selected = 1 - action_selected
                        if event.key == pygame.K_SPACE:
                            if action_selected == 0:
                                # Player attacks
                                damage = max(0, player.attack - enemy.defense)
                                enemy.hp -= damage
                                message = f"Le haces {damage} de daño."
                            elif action_selected == 1:
                                # Magia: Bola de fuego (cuesta 5 maná, hace 10 daño)
                                if player.mana >= 5:
                                    player.mana -= 5
                                    damage = 10
                                    enemy.hp -= damage
                                    message = f"Lanzas Bola de Fuego y haces {damage} de daño."
                                else:
                                    message = "¡No tienes suficiente maná!"
                                    continue
                            if enemy.hp <= 0:
                                message = "¡Enemigo derrotado!"
                                pygame.time.wait(700)
                                return True
                            # Enemy attacks
                            damage = max(0, enemy.attack - player.defense)
                            player.hp -= damage
                            message += f" El enemigo te hace {damage} de daño."
                            if player.hp <= 0:
                                pygame.time.wait(700)
                                return False

                screen.fill((50, 50, 80))
                player_x = WIDTH // 4 - player_img.get_width() // 2
                enemy_x = WIDTH * 3 // 4 - enemy_img.get_width() // 2
                y_img = HEIGHT // 2 - player_img.get_height() // 2

                screen.blit(player_img, (player_x, y_img))
                screen.blit(enemy_img, (enemy_x, y_img))

                # Stats
                draw_text(f"Jugador HP: {player.hp}", player_x, y_img - 80)
                draw_text(f"Maná: {player.mana}/{player.max_mana}", player_x, y_img - 50)
                draw_text(f"Nivel: {player.level}", player_x, y_img - 20)
                draw_text(f"Enemigo HP: {max(0, enemy.hp)}", enemy_x, y_img - 60)

                # Opciones de acción
                color_attack = (255, 255, 0) if action_selected == 0 else (255, 255, 255)
                color_magic = (255, 255, 0) if action_selected == 1 else (255, 255, 255)
                draw_text("Atacar (ESPACIO)", WIDTH // 2 - 180, HEIGHT - 160, color_attack)
                draw_text("Magia: Bola de Fuego (5 maná)", WIDTH // 2 - 180, HEIGHT - 120, color_magic)
                if message:
                    draw_text(message, WIDTH // 2 - 200, HEIGHT // 2 + player_img.get_height() // 2 + 30, (255,220,100))
                pygame.display.flip()


class Player:
    def __init__(self):
        self.hp = 30
        self.attack = 5
        self.defense = 2
        self.level = 1
        self.mana = 10
        self.max_mana = 10

    def upgrade(self):
        upgrading = True
        while upgrading:
            screen.fill((30, 30, 30))
            draw_text("Elige una mejora:", WIDTH // 2 - 120, HEIGHT // 2 - 80)
            draw_text("1. +5 HP", WIDTH // 2 - 120, HEIGHT // 2 - 40)
            draw_text("2. +2 Ataque", WIDTH // 2 - 120, HEIGHT // 2)
            draw_text("3. +1 Defensa", WIDTH // 2 - 120, HEIGHT // 2 + 40)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.hp += 5
                        upgrading = False
                    elif event.key == pygame.K_2:
                        self.attack += 2
                        upgrading = False
                    elif event.key == pygame.K_3:
                        self.defense += 1
                        upgrading = False

def main():
    player = Player()
    level = 1
    running = True
    while running and player.hp > 0:
        enemy = Enemy(level)
        # Pantalla de nivel
        screen.fill((30,30,30))
        draw_text(f"--- Nivel {level} ---", WIDTH // 2 - 100, HEIGHT // 2 - 40)
        pygame.display.flip()
        pygame.time.wait(1000)
        if battle(player, enemy):
            player.level += 1
            player.upgrade()
            level += 1
        else:
            screen.fill((30,30,30))
            draw_text("¡Has sido derrotado!", WIDTH // 2 - 120, HEIGHT // 2 - 40, (255,80,80))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False
    screen.fill((30,30,30))
    draw_text(f"Llegaste al nivel {level}", WIDTH // 2 - 120, HEIGHT // 2, (200,255,200))
    pygame.display.flip()
    pygame.time.wait(2500)
    pygame.quit()

# También ajusta la función upgrade para centrar los textos:
def draw_text(text, x, y, color=(255,255,255)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

class Player:
    def __init__(self):
        self.hp = 30
        self.attack = 5
        self.defense = 2
        self.level = 1

    def upgrade(self):
        upgrading = True
        while upgrading:
            screen.fill((30, 30, 30))
            draw_text("Elige una mejora:", WIDTH // 2 - 120, HEIGHT // 2 - 80)
            draw_text("1. +5 HP", WIDTH // 2 - 120, HEIGHT // 2 - 40)
            draw_text("2. +2 Ataque", WIDTH // 2 - 120, HEIGHT // 2)
            draw_text("3. +1 Defensa", WIDTH // 2 - 120, HEIGHT // 2 + 40)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_1:
                                            self.hp += 5
                                            upgrading = False
                                        elif event.key == pygame.K_2:
                                            self.attack += 2
                                            upgrading = False
                                        elif event.key == pygame.K_3:
                                            self.defense += 1
                                            upgrading = False
                    
                # Move the main entry point outside the class
    if __name__ == "__main__":
        main()
        # Añadir sistema de maná y opciones de magia

        # Modifica la clase Player para agregar maná
        class Player:
            def __init__(self):
                self.hp = 30
                self.attack = 5
                self.defense = 2
                self.level = 1
                self.mana = 10
                self.max_mana = 10

            def upgrade(self):
                upgrading = True
                while upgrading:
                    screen.fill((30, 30, 30))
                    draw_text("Elige una mejora:", WIDTH // 2 - 120, HEIGHT // 2 - 120)
                    draw_text("1. +5 HP", WIDTH // 2 - 120, HEIGHT // 2 - 80)
                    draw_text("2. +2 Ataque", WIDTH // 2 - 120, HEIGHT // 2 - 40)
                    draw_text("3. +1 Defensa", WIDTH // 2 - 120, HEIGHT // 2)
                    draw_text("4. +5 Maná máximo", WIDTH // 2 - 120, HEIGHT // 2 + 40)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                self.hp += 5
                                upgrading = False
                            elif event.key == pygame.K_2:
                                self.attack += 2
                                upgrading = False
                            elif event.key == pygame.K_3:
                                self.defense += 1
                                upgrading = False
                            elif event.key == pygame.K_4:
                                self.max_mana += 5
                                self.mana = self.max_mana
                                upgrading = False

        # Modifica la función battle para agregar opciones de magia
        def battle(player, enemy):
            battle_running = True
            message = ""
            action_selected = 0  # 0: atacar, 1: magia
            while battle_running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            action_selected = 1 - action_selected
                        if event.key == pygame.K_SPACE:
                            if action_selected == 0:
                                # Player attacks
                                damage = max(0, player.attack - enemy.defense)
                                enemy.hp -= damage
                                message = f"Le haces {damage} de daño."
                            elif action_selected == 1:
                                # Magia: Bola de fuego (cuesta 5 maná, hace 10 daño)
                                if player.mana >= 5:
                                    player.mana -= 5
                                    damage = 10
                                    enemy.hp -= damage
                                    message = f"Lanzas Bola de Fuego y haces {damage} de daño."
                                else:
                                    message = "¡No tienes suficiente maná!"
                                    continue
                            if enemy.hp <= 0:
                                message = "¡Enemigo derrotado!"
                                pygame.time.wait(700)
                                return True
                            # Enemy attacks
                            damage = max(0, enemy.attack - player.defense)
                            player.hp -= damage
                            message += f" El enemigo te hace {damage} de daño."
                            if player.hp <= 0:
                                pygame.time.wait(700)
                                return False

                screen.fill((50, 50, 80))
                player_x = WIDTH // 4 - player_img.get_width() // 2
                enemy_x = WIDTH * 3 // 4 - enemy_img.get_width() // 2
                y_img = HEIGHT // 2 - player_img.get_height() // 2

                screen.blit(player_img, (player_x, y_img))
                screen.blit(enemy_img, (enemy_x, y_img))

                # Stats
                draw_text(f"Jugador HP: {player.hp}", player_x, y_img - 80)
                draw_text(f"Maná: {player.mana}/{player.max_mana}", player_x, y_img - 50)
                draw_text(f"Nivel: {player.level}", player_x, y_img - 20)
                draw_text(f"Enemigo HP: {max(0, enemy.hp)}", enemy_x, y_img - 60)

                # Opciones de acción
                color_attack = (255, 255, 0) if action_selected == 0 else (255, 255, 255)
                color_magic = (255, 255, 0) if action_selected == 1 else (255, 255, 255)
                draw_text("Atacar (ESPACIO)", WIDTH // 2 - 180, HEIGHT - 160, color_attack)
                draw_text("Magia: Bola de Fuego (5 maná)", WIDTH // 2 - 180, HEIGHT - 120, color_magic)
                if message:
                    draw_text(message, WIDTH // 2 - 200, HEIGHT // 2 + player_img.get_height() // 2 + 30, (255,220,100))
                pygame.display.flip()

        # Elimina la definición duplicada de Player y battle si existe arriba.