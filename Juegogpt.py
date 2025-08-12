#!/usr/bin/env python3
import pygame
import random
import sys
from dataclasses import dataclass, field
from typing import List
from collections import deque

# ---------------- Configuración ----------------
TILE = 24
MAP_W = 40
MAP_H = 25
SCREEN_W = TILE * MAP_W
SCREEN_H = TILE * MAP_H + 80
FPS = 30

FLOOR = 0
WALL = 1
VIS_RADIUS = 8

MAX_ENEMIES = 10
MAX_POTIONS = 6

COLOR_BG = (10, 10, 10)
COLOR_FLOOR = (50, 50, 70)
COLOR_WALL = (30, 30, 30)
COLOR_PLAYER = (200, 200, 60)
COLOR_ENEMY = (200, 80, 80)
COLOR_POTION = (80, 200, 120)
COLOR_TEXT = (230, 230, 230)
COLOR_HUD_BG = (20, 20, 30)

# ---------------- Clases ----------------
@dataclass
class Entity:
    x: int
    y: int
    char: str
    name: str
    hp: int
    max_hp: int
    atk: int
    defense: int
    alive: bool = True
    xp_value: int = 0
    def pos(self): return (self.x, self.y)

@dataclass
class Item:
    x: int
    y: int
    name: str
    effect: str
    power: int

@dataclass
class Player:
    x: int
    y: int
    hp: int = 40
    max_hp: int = 40
    atk: int = 6
    defense: int = 2
    level: int = 1
    xp: int = 0
    xp_to_next: int = 25
    inventory: List[Item] = field(default_factory=list)
    def pos(self): return (self.x, self.y)
    def gain_xp(self, amount):
        self.xp += amount
        leveled = False
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level += 1
            self.max_hp += 6
            self.hp = self.max_hp
            self.atk += 1
            self.defense += 1
            self.xp_to_next = int(self.xp_to_next * 1.6)
            leveled = True
        return leveled

# ---------------- Generación de mapa ----------------
def generate_map(w=MAP_W, h=MAP_H, walk_steps=None):
    if walk_steps is None:
        walk_steps = int(w * h * 0.45)
    grid = [[WALL for _ in range(w)] for __ in range(h)]
    x, y = w//2, h//2
    grid[y][x] = FLOOR
    for _ in range(walk_steps):
        dx, dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        x = max(1, min(w-2, x+dx))
        y = max(1, min(h-2, y+dy))
        grid[y][x] = FLOOR
    for i in range(w):
        grid[0][i] = WALL
        grid[h-1][i] = WALL
    for j in range(h):
        grid[j][0] = WALL
        grid[j][w-1] = WALL
    return grid

# ---------------- Utilidades ----------------
def find_free_tile(grid):
    h = len(grid)
    w = len(grid[0])
    for _ in range(2000):
        x = random.randrange(1, w-1)
        y = random.randrange(1, h-1)
        if grid[y][x] == FLOOR:
            return x, y
    return 1,1

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def in_bounds(x,y):
    return 0 <= x < MAP_W and 0 <= y < MAP_H

def bfs_path(grid, start, goal, max_nodes=2000):
    if start == goal:
        return []
    q = deque([start])
    came = {start: None}
    nodes = 0
    while q and nodes < max_nodes:
        nodes += 1
        cur = q.popleft()
        if cur == goal:
            break
        x,y = cur
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if not in_bounds(nx,ny): continue
            if grid[ny][nx] == WALL: continue
            if (nx,ny) in came: continue
            came[(nx,ny)] = cur
            q.append((nx,ny))
    if goal not in came:
        return []
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came[cur]
    path.reverse()
    return path

# ---------------- Spawns ----------------
def spawn_enemies(grid, player, count=MAX_ENEMIES):
    enemies: List[Entity] = []
    SAFE_DIST = 8
    for _ in range(count):
        while True:
            ex, ey = find_free_tile(grid)
            if manhattan((ex, ey), player.pos()) >= SAFE_DIST:
                break
        hp = random.randint(6, 12)
        atk = random.randint(1, 3)
        defense = random.randint(0, 1)
        xp_val = 4 + hp // 2
        enemies.append(Entity(ex, ey, 'E', "Orco", hp, hp, atk, defense, True, xp_val))
    return enemies

def ensure_safe_zone(player, enemies, grid):
    SAFE_RADIUS = 10
    for e in enemies:
        if manhattan(e.pos(), player.pos()) < SAFE_RADIUS:
            while True:
                ex, ey = find_free_tile(grid)
                if manhattan((ex, ey), player.pos()) >= SAFE_RADIUS:
                    e.x, e.y = ex, ey
                    break

def spawn_potions(grid, count=MAX_POTIONS):
    items: List[Item] = []
    for _ in range(count):
        ix, iy = find_free_tile(grid)
        pot_power = random.randint(8, 16)
        items.append(Item(ix, iy, "Poción de curación", "heal", pot_power))
    return items

# ---------------- Render ----------------
def draw_map(surface, grid, player, enemies, items):
    px, py = player.pos()
    for y in range(MAP_H):
        for x in range(MAP_W):
            visible = (x-px)**2 + (y-py)**2 <= VIS_RADIUS**2
            rect = pygame.Rect(x*TILE, y*TILE, TILE, TILE)
            if not visible:
                pygame.draw.rect(surface, (6,6,10), rect)
                continue
            if grid[y][x] == WALL:
                pygame.draw.rect(surface, COLOR_WALL, rect)
            else:
                pygame.draw.rect(surface, COLOR_FLOOR, rect)
    for it in items:
        if (it.x-px)**2 + (it.y-py)**2 <= VIS_RADIUS**2:
            r = pygame.Rect(it.x*TILE+6, it.y*TILE+6, TILE-12, TILE-12)
            pygame.draw.rect(surface, COLOR_POTION, r)
    for e in enemies:
        if not e.alive: continue
        if (e.x-px)**2 + (e.y-py)**2 <= VIS_RADIUS**2:
            r = pygame.Rect(e.x*TILE+3, e.y*TILE+3, TILE-6, TILE-6)
            pygame.draw.rect(surface, COLOR_ENEMY, r)
    r = pygame.Rect(player.x*TILE+3, player.y*TILE+3, TILE-6, TILE-6)
    pygame.draw.rect(surface, COLOR_PLAYER, r)

def draw_hud(surface, font, player, messages):
    hud_rect = pygame.Rect(0, MAP_H*TILE, SCREEN_W, SCREEN_H - MAP_H*TILE)
    pygame.draw.rect(surface, COLOR_HUD_BG, hud_rect)
    hp_text = f"HP: {player.hp}/{player.max_hp}  ATK: {player.atk}  DEF: {player.defense}  LV: {player.level}  XP: {player.xp}/{player.xp_to_next}"
    inv_text = "Inv: " + (", ".join([f"{it.name}(+{it.power})" for it in player.inventory]) if player.inventory else "(vacío)")
    tx = font.render(hp_text, True, COLOR_TEXT)
    surface.blit(tx, (8, MAP_H*TILE + 8))
    tx2 = font.render(inv_text, True, COLOR_TEXT)
    surface.blit(tx2, (8, MAP_H*TILE + 34))
    for i, m in enumerate(messages[-3:]):
        txm = font.render(m, True, COLOR_TEXT)
        surface.blit(txm, (8, MAP_H*TILE + 58 + i*18))

# ---------------- Combate y AI ----------------
def attack(attacker, defender):
    damage = max(0, attacker.atk - defender.defense + random.randint(-1,2))
    if damage <= 0:
        return 0
    defender.hp -= damage
    if defender.hp <= 0:
        defender.alive = False
    return damage

def enemy_turns(grid, player, enemies, messages):
    for e in enemies:
        if not e.alive: continue
        if manhattan(e.pos(), player.pos()) > VIS_RADIUS:
            continue
        if manhattan(e.pos(), player.pos()) == 1:
            dmg = max(0, e.atk - player.defense + random.randint(-1,1))
            dmg = max(dmg, 0)
            player.hp -= dmg
            messages.append(f"{e.name} te golpea por {dmg} dmg.")
            if player.hp <= 0:
                player.hp = 0
                messages.append("Has muerto...")
                return
            continue
        path = bfs_path(grid, e.pos(), player.pos(), max_nodes=1500)
        if path:
            nx, ny = path[0]
            if (nx,ny) != player.pos() and all((other.x,other.y) != (nx,ny) for other in enemies if other is not e and other.alive):
                e.x, e.y = nx, ny

# ---------------- Items ----------------
def use_item(player, index, messages):
    if index < 0 or index >= len(player.inventory):
        messages.append("Índice de item inválido.")
        return
    it = player.inventory.pop(index)
    if it.effect == "heal":
        old = player.hp
        player.hp = min(player.max_hp, player.hp + it.power)
        messages.append(f"Usaste {it.name}: +{player.hp-old} HP.")

# ---------------- Main ----------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Roguelike de peleas - Pygame")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 16)

    grid = generate_map()
    px, py = find_free_tile(grid)
    player = Player(px, py)
    player.inventory.append(Item(player.x, player.y, "Poción de curación", "heal", 15))

    enemies = spawn_enemies(grid, player)
    ensure_safe_zone(player, enemies, grid)
    items = spawn_potions(grid)

    messages: List[str] = ["¡Entra en la mazmorra!"]
    running = True
    game_over = False

    while running:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_ESCAPE:
                    running = False
                dx = dy = 0
                if event.key in (pygame.K_w, pygame.K_UP): dy = -1
                elif event.key in (pygame.K_s, pygame.K_DOWN): dy = 1
                elif event.key in (pygame.K_a, pygame.K_LEFT): dx = -1
                elif event.key in (pygame.K_d, pygame.K_RIGHT): dx = 1
                if dx != 0 or dy != 0:
                    nx, ny = player.x + dx, player.y + dy
                    if not in_bounds(nx, ny) or grid[ny][nx] == WALL:
                        messages.append("Un muro bloquea el paso.")
                    else:
                        target = next((e for e in enemies if e.alive and (e.x, e.y) == (nx, ny)), None)
                        if target:
                            dmg = attack(player, target)
                            if dmg <= 0:
                                messages.append(f"Atacas a {target.name} pero no haces daño.")
                            else:
                                messages.append(f"Atacas a {target.name} por {dmg} dmg.")
                                if not target.alive:
                                    messages.append(f"Has matado a {target.name}! Ganas {target.xp_value} XP.")
                                    leveled = player.gain_xp(target.xp_value)
                                    if leveled:
                                        messages.append(f"Subiste a nivel {player.level}! HP restaurada.")
                        else:
                            player.x, player.y = nx, ny
                    enemy_turns(grid, player, enemies, messages)
                if event.key == pygame.K_e:
                    found = next((it for it in items if (it.x, it.y) == player.pos()), None)
                    if found:
                        player.inventory.append(found)
                        items.remove(found)
                        messages.append(f"Recogiste {found.name}.")
                    else:
                        messages.append("No hay nada aquí para recoger.")
                    enemy_turns(grid, player, enemies, messages)
                if event.key == pygame.K_i:
                    if player.inventory:
                        use_item(player, 0, messages)
                    else:
                        messages.append("Inventario vacío.")
                    enemy_turns(grid, player, enemies, messages)
        if not game_over and player.hp <= 0:
            game_over = True
            messages.append("PERMADEATH: Has muerto.")
        screen.fill(COLOR_BG)
        draw_map(screen, grid, player, enemies, items)
        draw_hud(screen, font, player, messages)
        if game_over:
            s = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
            s.fill((0,0,0,160))
            screen.blit(s, (0,0))
            t = font.render("GAME OVER - Cierra la ventana para salir.", True, (255,200,200))
            screen.blit(t, (SCREEN_W//2 - t.get_width()//2, SCREEN_H//2 - t.get_height()//2))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
        pygame.quit()
        raise