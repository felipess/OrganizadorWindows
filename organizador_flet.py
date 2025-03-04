import os
import shutil
from pathlib import Path
import flet as ft

def organizar_arquivos(caminho, page, log_text):
    if not os.path.exists(caminho):
        log_text.value += f"O caminho fornecido não existe: {caminho}\n"
        page.update()
        return
    
    diretorio = Path(caminho)
    
    categorias = {
        "Imagens": {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'},
        "Videos": {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'},
        "PDFs": {'.pdf'},
        "Textos": {'.txt'},
        "Documentos": {'.doc', '.docx', '.xls', '.xlsx', '.csv'},
        "Arquivos Compactados": {'.zip', '.rar', '.7z', '.tar', '.gz'},
        "Codigos": {'.py', '.java', '.cpp', '.js', '.html', '.css'},
        "Audio": {'.mp3', '.wav', '.ogg', '.flac', '.aac'}
    }
    
    for arquivo in diretorio.iterdir():
        if arquivo.is_file():
            extensao = arquivo.suffix.lower()
            nome_pasta = "Diversos"
            
            for categoria, extensoes in categorias.items():
                if extensao in extensoes:
                    nome_pasta = categoria
                    break
            
            pasta_destino = diretorio / nome_pasta
            
            try:
                if not pasta_destino.exists():
                    pasta_destino.mkdir()
                destino = pasta_destino / arquivo.name
                shutil.move(str(arquivo), str(destino))
                log_text.value += f"Movido: {arquivo.name} -> {pasta_destino}\n"
            except Exception as e:
                log_text.value += f"Erro ao processar {arquivo.name}: {str(e)}\n"
        elif arquivo.is_dir():
            log_text.value += f"Ignorando pasta: {arquivo.name}\n"
    
    log_text.value += "\nOrganização concluída!\n"
    page.update()

def main(page: ft.Page):
    page.title = "Organizador de Arquivos"
    page.window_width = 900
    page.window_height = 620
    
    # Campo de texto para o caminho
    caminho_field = ft.TextField(label="Diretório de origem", width=650)
    
    # Função para lidar com o resultado do FilePicker
    def handle_file_picker_result(e):
        if e.path:
            caminho_field.value = e.path
            page.update()
    
    # Função para abrir o seletor de diretório
    def selecionar_diretorio(e):
        file_picker = ft.FilePicker(on_result=handle_file_picker_result)
        page.overlay.append(file_picker)
        page.update()
        file_picker.get_directory_path(dialog_title="Selecione o diretório")  # Correção aqui
    
    # Botão para selecionar diretório
    btn_selecionar = ft.ElevatedButton(
        content=ft.Text("Selecionar Diretório", size=12),
        on_click=selecionar_diretorio,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
            padding=10,
        ),
        width=110,
        height=53
    )
    
    # Área de texto para log
    log_text = ft.Text("", selectable=True, size=12)
    log_container = ft.Container(content=log_text, height=450, width=870, bgcolor=ft.colors.GREY_900, padding=10)
    
    # Função para iniciar organização
    def iniciar_organizacao(e):
        caminho = caminho_field.value.strip().strip('"')
        if not caminho:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, selecione um diretório!"), open=True)
            page.update()
            return
        log_text.value = "Organizando arquivos...\n"
        page.update()
        organizar_arquivos(caminho, page, log_text)
    
    # Botão iniciar organizar
    btn_organizar = ft.ElevatedButton(
        content=ft.Text("Iniciar", size=12),
        on_click=iniciar_organizacao,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
            padding=10,
        ),
        width=80,
        height=53,
    )
    
    # Layout da interface
    page.add(
        ft.Column([
            ft.Text("Organizador de Arquivos", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([caminho_field, btn_selecionar,btn_organizar]),
            # ft.Row([btn_organizar], alignment=ft.MainAxisAlignment.CENTER),  # Centraliza o botão "Organizar Arquivos"
            log_container
        ], alignment=ft.MainAxisAlignment.START, spacing=10)
    )

if __name__ == "__main__":
    ft.app(target=main)