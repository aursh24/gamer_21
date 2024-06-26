from typing import Self
import pygame

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300
CELL_SIZE = 40
PADDING = 20
ROWS = COLS = (SCREEN_WIDTH - 4 * PADDING) // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)
DARK_GRAY = (30, 30, 30)
LIGHT_GRAY = (100, 100, 100)

# Constants defining various properties of the game window and cells
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300
CELL_SIZE = 40
PADDING = 20
ROWS = COLS = (SCREEN_WIDTH - 4 * PADDING) // CELL_SIZE

# Initialize Pygame
pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('cursive', 25)

class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.index = self.r * ROWS + self.c
        self.rect = pygame.Rect((self.c * CELL_SIZE + 2 * PADDING, self.r * CELL_SIZE + 3 * PADDING, CELL_SIZE, CELL_SIZE))

win = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.SysFont('cursive', 25)

WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
BLACK = (12, 12, 12)

# Define the Cell class to represent each cell in the grid
class Cell:
    def __init__(self, row, col):
        """
        Initialize a cell with its row and column coordinates.
        """
        self.row = row
        self.col = col
        self.index = self.row * ROWS + self.col
        # Create a rectangle representing the cell's area on the game window
        self.rect = pygame.Rect((self.col * CELL_SIZE + 2 * PADDING,
                                 self.row * CELL_SIZE + 3 * PADDING,
                                 CELL_SIZE, CELL_SIZE))
        # Define the edges of the cell for drawing lines around it
        self.edges = [
            [(self.rect.left, self.rect.top), (self.rect.right, self.rect.top)],
            [(self.rect.right, self.rect.top), (self.rect.right, self.rect.bottom)],
            [(self.rect.right, self.rect.bottom), (self.rect.left, self.rect.bottom)],
            [(self.rect.left, self.rect.bottom), (self.rect.left, self.rect.top)]
        ]

        self.sides = [False] * 4
        self.winner = None

    def check_win(self, winner):
        if not self.winner and all(self.sides):
            self.winner = winner
            self.color = GREEN if winner == 'X' else RED
            self.text = font.render(self.winner, True, WHITE)
            return 1
        return 0

    def update(self, win):
        if self.winner:
            pygame.draw.rect(win, self.color, self.rect)
            win.blit(self.text, (self.rect.centerx - 5, self.rect.centery - 7))

        for index, side in enumerate(self.sides):
            if side:
                pygame.draw.line(win, WHITE, self.edges[index][0], self.edges[index][1], 2)

def create_cells():
    cells = []
    for r in range(ROWS):
        for c in range(COLS):
            cell = Cell(r, c)
            cells.append(cell)
    return cells

def reset_cells():
    return None, None, False, False, False, False

def reset_score():
    return 0, 0, 0

def reset_player():
    return 0, ['X', 'O'], 'X', False

# Game variables initialization
game_over = False
cells = create_cells()
pos, current_cell, up, right, bottom, left = reset_cells()
fill_count, p1_score, p2_score = reset_score()
turn, players, current_player, next_turn = reset_player()

Self.sides = [False, False, False, False]  # Tracks whether each side of the cell is filled
Self.winner = None  # Stores the winner of the cell (if any)

def check_win(self, winner):
    """
    Check if a player has won by filling all four sides of the cell.
    """
    if not self.winner:
        if self.sides == [True]*4:
            self.winner = winner
            return 1  # Indicate that the cell has been won
    return 0  # Indicate that the cell has not been won

def update(self, surface):
    """
    Update the visual representation of the cell on the game window.
    """
    if self.winner:
        # Draw the cell with the winning player's color
        pygame.draw.rect(surface, GREEN if self.winner == 'X' else RED, self.rect)
    for index, side in enumerate(self.sides):
        if side:
            # Draw filled sides of the cell
            pygame.draw.line(surface, WHITE, self.edges[index][0], self.edges[index][1], 2)

# Initialize game variables
cells = []
game_over = False
turn = 0
players = ['X', 'O']
player = players[turn]
next_turn = False
fill_count = 0
p1_score = 0
p2_score = 0
ccell = None
up = right = bottom = left = False

# Create the game grid
for r in range(ROWS):
    for c in range(COLS):
        cell = Cell(r, c)
        cells.append(cell)

# Main game loop
running = True
while running:

    win.fill(DARK_GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                game_over = False
                cells = create_cells()
                pos, current_cell, up, right, bottom, left = reset_cells()
                fill_count, p1_score, p2_score = reset_score()
                turn, players, current_player, next_turn = reset_player()
            elif not game_over:
                if event.key == pygame.K_UP:
                    up = True
                elif event.key == pygame.K_RIGHT:
                    right = True
                elif event.key == pygame.K_DOWN:
                    bottom = True
                elif event.key == pygame.K_LEFT:
                    left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            elif event.key == pygame.K_RIGHT:
                right = False
            elif event.key == pygame.K_DOWN:
                bottom = False
            elif event.key == pygame.K_LEFT:
                left = False

    # Drawing grid
    for r in range(ROWS + 1):
        for c in range(COLS + 1):
            pygame.draw.circle(win, WHITE, (c * CELL_SIZE + 2 * PADDING, r * CELL_SIZE + 3 * PADDING), 2)

    # Update and draw cells
    for cell in cells:
        cell.update(win)
        if pos and cell.rect.collidepoint(pos):
            current_cell = cell

    # Drawing current selection
    if current_cell:
        index = current_cell.index
        if not current_cell.winner:
            pygame.draw.circle(win, RED, current_cell.rect.center, 2)

        if up and not current_cell.sides[0]:
            current_cell.sides[0] = True
            if index - ROWS >= 0:
                cells[index - ROWS].sides[2] = True
                next_turn = True
        if right and not current_cell.sides[1]:
            current_cell.sides[1] = True
            if (index + 1) % COLS > 0:
                cells[index + 1].sides[3] = True
                next_turn = True
        if bottom and not current_cell.sides[2]:
            current_cell.sides[2] = True
            if index + ROWS < len(cells):
                cells[index + ROWS].sides[0] = True
                next_turn = True
        if left and not current_cell.sides[3]:
            current_cell.sides[3] = True
            if (index % COLS) > 0:
                cells[index - 1].sides[1] = True
                next_turn = True

        # Check for win condition
        res = current_cell.check_win(current_player)
        if res:
            fill_count += res
            if current_player == 'X':
                p1_score += 1
            else:
                p2_score += 1
            if fill_count == ROWS * COLS:
                game_over = True

        # Switch players
        if next_turn:
            turn = (turn + 1) % len(players)
            current_player = players[turn]
            next_turn = False

        # Display scores and current player
        p1_img = font.render(f'{p1_score}', True, BLUE)
        p2_img = font.render(f'{p2_score}', True, BLUE)

        # Render player texts with appropriate positions    
        p1_text = font.render('Player 1:', True, BLUE)
        p2_text = font.render('Player 2:', True, BLUE)

        # Calculate positions for player texts and scores
        p1_text_pos = (2 * PADDING, 15)
        p1_img_pos = (p1_text_pos[0] + p1_text.get_width() + 5, 15)
        p2_img_pos = (SCREEN_WIDTH - 2 * PADDING - p2_img.get_width(), 15)
        p2_text_pos = (p2_img_pos[0] - p2_text.get_width() - 5, 15)

        # Blit the player texts and scores
        win.blit(p1_text, p1_text_pos)
        win.blit(p1_img, p1_img_pos)
        win.blit(p2_text, p2_text_pos)
        win.blit(p2_img, p2_img_pos)

        # Switch players
        if next_turn:
            turn = (turn + 1) % len(players)
            current_player = players[turn]
            next_turn = False

        # Highlight current player's turn
        if not game_over:
            if turn == 0:  # Player 1's turn
                pygame.draw.rect(win, BLUE, (p1_text_pos[0], p1_text_pos[1] + font.get_height() + 2, p1_text.get_width() + p1_img.get_width() + 5, 2), 0)
            else:  # Player 2's turn
                pygame.draw.rect(win, BLUE, (p2_text_pos[0], p2_text_pos[1] + font.get_height() + 2, p2_text.get_width() + p2_img.get_width() + 5, 2), 0)


    if game_over:
        # Display game over message
        over_img = font.render('Game Over', True, WHITE)
        winner_img = font.render(f'Player {1 if p1_score > p2_score else 2} Won', True, GREEN)
        msg_img = font.render('Press R to restart, Q or ESC to quit', True, RED)
        win.blit(over_img, ((SCREEN_WIDTH - over_img.get_width()) / 2, 100))
        win.blit(winner_img, ((SCREEN_WIDTH - winner_img.get_width()) / 2, 150))
        win.blit(msg_img, ((SCREEN_WIDTH - msg_img.get_width()) / 2, 200))

    # Draw border
    pygame.draw.rect(win, LIGHT_GRAY, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2, border_radius=10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    win.fill(BLACK)

    # Draw the grid lines
    for r in range(ROWS + 1):
        for c in range(COLS + 1):
            pygame.draw.circle(win, WHITE, (c * CELL_SIZE + 2 * PADDING, r * CELL_SIZE + 3 * PADDING), 2)

    # Update and draw each cell in the grid
    for cell in cells:
        cell.update(win)

    pygame.display.update()

pygame.quit()
