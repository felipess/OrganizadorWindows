import os
import shutil
from pathlib import Path

def organizar_arquivos(caminho):
    # Verifica se o caminho existe
    if not os.path.exists(caminho):
        print("O caminho fornecido não existe!")
        return
    
    # Converte o caminho para um objeto Path
    diretorio = Path(caminho)
    
    # Itera sobre todos os arquivos no diretório
    for arquivo in diretorio.iterdir():
        # Verifica se é um arquivo (e não uma pasta)
        if arquivo.is_file():
            # Pega a extensão do arquivo (em minúsculas)
            extensao = arquivo.suffix.lower()
            
            # Se o arquivo não tiver extensão, usa "SemExtensao"
            if not extensao:
                extensao = ".SemExtensao"
            
            # Remove o ponto da extensão para usar como nome da pasta
            nome_pasta = extensao[1:] if extensao else "SemExtensao"
            
            # Define o caminho da pasta de destino
            pasta_destino = diretorio / nome_pasta
            
            try:
                # Cria a pasta se ela não existir
                if not pasta_destino.exists():
                    pasta_destino.mkdir()
                
                # Define o caminho completo do destino
                destino = pasta_destino / arquivo.name
                
                # Move o arquivo para a pasta correspondente
                shutil.move(str(arquivo), str(destino))
                print(f"Movido: {arquivo.name} -> {pasta_destino}")
                
            except Exception as e:
                print(f"Erro ao processar {arquivo.name}: {str(e)}")

def main():
    # Solicita o caminho ao usuário
    print("Digite o caminho completo do diretório que deseja organizar")
    print("Exemplo: C:\\Users\\felip\\OneDrive\\Área de Trabalho")
    
    caminho = input("Caminho: ")
    
    # Remove possíveis aspas e espaços extras
    caminho = caminho.strip().strip('"')
    
    print("\nOrganizando arquivos...")
    organizar_arquivos(caminho)
    print("\nOrganização concluída!")

if __name__ == "__main__":
    main()