import os
import tkinter as tk
import subprocess

def set_vcpkg_root(path):
    # Muda a variável no ambiente do programa
    os.environ["VCPKG_ROOT"] = path
    
    # Atualiza globalmente no sistema
    subprocess.run(f'setx VCPKG_ROOT "{path}" /M', shell=True)
    
    # Atualiza a label na interface
    label.config(text=f"VCPKG_ROOT: {path}")
    
    run_vs_integration(path)

def run_vs_integration(path):
    vcpkg_exe = os.path.join(path, "vcpkg.exe")
    
    # Remover a integração antiga
    old_vcpkg = os.environ.get("VCPKG_ROOT", "")
    if old_vcpkg and os.path.exists(os.path.join(old_vcpkg, "vcpkg.exe")):
        subprocess.run(f"\"{os.path.join(old_vcpkg, 'vcpkg.exe')}\" integrate remove", shell=True)

    # Integrar a nova pasta
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
