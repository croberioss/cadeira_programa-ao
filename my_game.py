import pygame

def _posicao_pecas(linha, coluna, SQUARE_SIZE):
    x = coluna * SQUARE_SIZE + SQUARE_SIZE//2
    y = linha * SQUARE_SIZE + SQUARE_SIZE//2
    return (x, y)

def _pecas(linha, coluna, cor_peca, cores, TAMANHO_QUADRADO) -> dict:
    simbolo = 'x' if cor_peca == cores['BLACK'] else 'o'
    damas = False
    direçao = 1 if cor_peca == cores['WHITE'] else -1
    posicao = _posicao_pecas(linha, coluna, TAMANHO_QUADRADO)
    
    dict_peca = {'simbolo': simbolo, 'posicao_peca': posicao, 'cor_peca': cor_peca, 'damas': damas, 'direção': direçao}
    
    return dict_peca

def _preencher_tabuleiro(tabuleiro:list[list], cores:dict, LINHAS:int, TAMANHO_QUADRADO:int) -> None:
        
    for linha in range(LINHAS):
        tabuleiro.append([])
        for coluna in range(LINHAS):
            if coluna % 2 == ((linha + 1) % 2): #Parte do tabuleiro que devem ser colocado as peças
                if linha < 3: 
                    tabuleiro[linha].append(_pecas(linha, coluna, cores['BLACK'], cores, TAMANHO_QUADRADO))
                elif linha > 4:
                    tabuleiro[linha].append(_pecas(linha, coluna, cores['WHITE'], cores, TAMANHO_QUADRADO))
                else:
                    tabuleiro[linha].append({'simbolo': None}) 
            else:
                tabuleiro[linha].append({'simbolo': None})

def _desenhar_peca(display:pygame.display, posicao_tabuleiro, cores, TAMANHO_QUADRADO):
    radius = TAMANHO_QUADRADO//2 - 10
    
    pygame.draw.circle(display, cores['GREY'], posicao_tabuleiro['posicao_peca'], radius + 2)
    pygame.draw.circle(display, posicao_tabuleiro['cor_peca'], posicao_tabuleiro['posicao_peca'], radius)
    # if damas:
    #     display.blit(CROWN, (x - CROWN.get_width()//2, y - CROWN.get_height()//2))


def tabuleiro(display:pygame.display, cores:dict, LINHAS:int, COLUNAS:int, TAMANHO_QUADRADO:int) -> pygame.display:
    tabuleiro = []
    peca_selecionada = None
    pretos_restantes = brancos_restantes = 12
    damas_pretas = damas_brancas = 0
    
    cor_tabuleiro = cores['BLACK']
    cor_quadrados = cores['WHITE']
    
    display.fill(cor_tabuleiro)
    for linha in range(LINHAS):
        for coluna in range(linha % 2, LINHAS, 2):
            pygame.draw.rect(surface=display,
                            color= cor_quadrados,
                            rect=(linha*TAMANHO_QUADRADO, coluna*TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
    
    _preencher_tabuleiro(tabuleiro, cores, LINHAS, TAMANHO_QUADRADO)
        
    for row in range(LINHAS):
        for col in range(COLUNAS):
            piece = tabuleiro[row][col]['simbolo']
            if piece != None:
                _desenhar_peca(display, tabuleiro[row][col], cores, TAMANHO_QUADRADO)
    
    
    return display


    
                
def selectionar_peca():
    pass        

def movimentacao(posicao_tabuleiro:dict, linha, coluna):
    posicao_tabuleiro['posicao_peca'] = (linha, coluna)
    
    if linha == 8 or linha == 0:
        posicao_tabuleiro['damas'] = True
        #Se quiser implementar contador de damas
        #Aprox 22 min do 2º video


def move(self, piece, row, col):
    self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
    piece.move(row, col)



    # PADDING = 10
    # OUTLINE = 2
    # radiano = TAMANHO_QUADRADO // 2 - 10
    # pygame.draw.circle(display, cores['GREY'], (x, y), radiano)
    # pygame.draw.circle(display, cor_peca, (x, y), radiano + 2)
    


def _damas(damas):
    damas = True
    return damas
    
    
    
def main():
    #Constants  for the game
    LARGURA = 800
    ALTURA = 800

    LINHAS, COLUNAS = 8, 8
    SQUARE_SIZE = LARGURA // COLUNAS

    cores = {'BLACK': (0, 0, 0),
             'WHITE': (255, 255, 255),
             'YELLOW': (255, 255, 0),
             'DARK_BROWN': (43, 29, 20),
             'LIGHT_BROWN': (208, 187, 148),
             'GREY': (128, 128, 128)}
    
    # BLACK = (0, 0, 0)
    # WHITE = (255, 255, 255)
    # YELLOW = (255, 255, 0)
    
    display = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Jogo de Damas')
    
    clock = pygame.time.Clock()
    run = True
    while run:
        
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
        
        tabuleiro(display, cores, LINHAS, COLUNAS, SQUARE_SIZE)
        pygame.display.update()
        break
    
    pygame.quit()
    
    
if __name__ == '__main__':
    main()
    
