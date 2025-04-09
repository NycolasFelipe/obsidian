
**Requisitos:**
\- Windows 10/11 Pro, Enterprise ou Education (64-bit).    
\- **OU** Windows 10/11 Home (64-bit) com **WSL 2** (Windows Subsystem for Linux).- Virtualização habilitada no BIOS/UEFI.

**Como funciona:**
\- Docker Desktop usa o **WSL 2** (subsistema Linux integrado ao Windows) para executar containers de forma nativa e eficiente.
\- Você pode alternar entre containers Linux e Windows (mas a maioria dos projetos usa Linux).

**Passo a passo:**
\- Instale o WSL2 (no powershell):
```powershell
wsl --install
```

\- Baixe e instale o [Docker Desktop para Windows](https://www.docker.com/products/docker-desktop/).
\- Após a instalação, reinicie o computador.
\- Abra o Docker Desktop e verifique no terminal:
```bash
docker --version
```
