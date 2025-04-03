# VCPKG Root Switcher

Este é um utilitário simples em Python com interface gráfica para alternar entre diferentes diretórios de instalação do `vcpkg`. O programa permite atualizar a variável de ambiente `VCPKG_ROOT` e executar os comandos necessários para integração com o Visual Studio.

## 🚀 Funcionalidades
- Alterna rapidamente entre duas instalações do `vcpkg`.
- Atualiza a variável `VCPKG_ROOT` no sistema.
- Remove a integração anterior e aplica a nova configuração automaticamente.
- Interface gráfica intuitiva usando `tkinter`.

## 🛠️ Requisitos
- Python 3.x
- `vcpkg` instalado nas pastas desejadas
- Sistema operacional Windows

## 📦 Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/arthursdiaz/vcpkg-switcher.git
   cd vcpkg-switcher
   ```
2. Instale as dependências:
   ```sh
   pip install tk
   ```
3. Execute o script:
   ```sh
   python vcpkg_switch.py
   ```

## 🎮 Como Usar
1. Abra o programa e escolha uma das opções disponíveis:
   - **Set to D:\\vcpkg_serv** → Define `VCPKG_ROOT` para `D:\\vcpkg_serv`
   - **Set to Z:\\vcpkg** → Define `VCPKG_ROOT` para `Z:\\vcpkg`
2. O programa removerá a integração anterior e aplicará a nova automaticamente.
3. Verifique se o `vcpkg.exe` foi encontrado e integrado corretamente.

## ⚙️ Como Funciona
1. O programa altera `VCPKG_ROOT` na sessão do sistema e de forma permanente.
2. Remove qualquer integração anterior com `vcpkg integrate remove`.
3. Aplica a nova integração com `vcpkg integrate install`.

## 🔥 Exemplo de Código
```python
import os
import tkinter as tk
import subprocess

def set_vcpkg_root(path):
    os.environ["VCPKG_ROOT"] = path
    subprocess.run(f'setx VCPKG_ROOT "{path}" /M', shell=True)
    label.config(text=f"VCPKG_ROOT: {path}")
    run_vs_integration(path)

def run_vs_integration(path):
    vcpkg_exe = os.path.join(path, "vcpkg.exe")
    old_vcpkg = os.environ.get("VCPKG_ROOT", "")
    if old_vcpkg and os.path.exists(os.path.join(old_vcpkg, "vcpkg.exe")):
        subprocess.run(f"\"{os.path.join(old_vcpkg, 'vcpkg.exe')}\" integrate remove", shell=True)
    if os.path.exists(vcpkg_exe):
        subprocess.run(f"\"{vcpkg_exe}\" integrate install", shell=True)
    else:
        label.config(text=f"vcpkg.exe não encontrado em {path}")

root = tk.Tk()
root.title("VCPKG Root Switcher")
root.geometry("300x150")
label = tk.Label(root, text=f"VCPKG_ROOT: {os.environ.get('VCPKG_ROOT', 'Not Set')}")
label.pack(pady=10)
btn1 = tk.Button(root, text="Set to D:\\vcpkg_serv", command=lambda: set_vcpkg_root("D:\\vcpkg_serv"))
btn1.pack(pady=5)
btn2 = tk.Button(root, text="Set to Z:\\vcpkg", command=lambda: set_vcpkg_root("Z:\\vcpkg"))
btn2.pack(pady=5)
root.mainloop()
```

## 📜 Licença
Este projeto é de código aberto e está disponível sob a licença MIT.

---
**Autor:** [Arthur Diaz](https://github.com/arthursdiaz)

