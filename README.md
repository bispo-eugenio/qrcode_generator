# QR Code Generator
A aplicação tem o intuito de gerar QR Code a partir de URL fornecida pelo usuário.

## Objetivo
Usar as ferramentas do PyQt/PySide6 para desenvolver um gerator de QR Code.

## Pré-requisitos

- Python 3.13 ou superior
- [uv](https://github.com/astral-sh/uv) (opcional, para instalação mais rápida)
- PySide6 (definido no `requirements.txt`)

## Como executar o programa (Padrão do Python):
```bash
git clone https://github.com/bispo-eugenio/qrcode_generator.git

#Faça os passos daqui em diante caso tenha o Visual Studio Code (VS Code) na máquina. Caso não tenha o VS Code, abra manualmente com seu editor de código.

cd qrcode_generator

code .
```

### Crie um ambiente virtual (Recomendação):
```bash
python -m venv venv
source venv/bin/activate #Linux/Mac
venv\Scripts\activate #Windows
```

### Instale as dependências do requeriments.txt
```bash
pip install -r requirements.txt
```

### Execute o programa:
```bash
py main.py #Use o jeito mais confortável para chamar o python
```

## Como executar o programa (com uv):
```bash
git clone https://github.com/bispo-eugenio/qrcode_generator.git

cd qrcode_gerator 
```

### Builde o projeto:
```bash
uv pip install -e .

code . #Só use se tiver Visual Studio Code (VS Code). Caso não tenha, vá até a pasta manualmente e abra com seu editor de código.
```

## Como baixar o projeto como .exe:
Primeiramente, certifique-se de ter realizado o processo acima para ter o projeto em mãos e editável.

### Baixando o PyInstaller:
```bash
#Usando pip (Padrão)
pip install pyinstaller
#Usando uv
uv add pyinstaller
```
### Fazendo o .exe:
```bash
pyinstaller --name="QRCODE GENERATOR" --noconfirm --onefile --icon="src\\my_package\\assets\\icon\\qrcode-generator.ico" --noconsole --clean src/main.py
#Usando uv
uv run pyinstaller --name="QRCODE GENERATOR" --noconfirm --onefile --icon="src\\my_package\\assets\\icon\\qrcode-generator.ico" --noconsole --clean src/main.py
```
O PyInstaller vai gerar o .exe dentro do projeto na pasta dist, mas caso queira editar alguma coisa recomendo dar uma olhada na própria documentação do PyInstaller

Documentação PyInstaller: https://pyinstaller.org/en/stable/usage.html

## Testes

Ainda não há testes automatizados.

## Funcionalidades

- Geração de QR Code a partir de qualquer URL válida 
- Interface gráfica simples e intuitiva
- Exportação do QR Code como imagem (opcional)

> ⚠️ **Observação:** A validação da URL ainda não está totalmente refinada, podendo permitir entradas incorretas em alguns casos.

## Contribuindo

Contribuições são bem-vindas!  
Sinta-se à vontade para abrir _issues_ ou enviar _pull requests_.

1. Fork este repositório
2. Crie uma branch com sua feature: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'Adiciona nova feature'`
4. Push para a branch: `git push origin minha-feature`
5. Abra um Pull Request