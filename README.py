#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `ipe` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `ipe` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `ipe` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `ipe`
# 
# O editor de desenho extensível `ipe` é um editor de gráficos vetoriais gratuito para criar figuras em formato `.pdf` ou `.eps`. Ele pode ser usado para fazer pequenas figuras para inclusão em documentos LaTeX, bem como para fazer apresentações em `.pdf` de várias páginas. É desenvolvido por Otfried Cheong desde 1993 e inicialmente funcionava apenas em estações de trabalho SGI. O `Ipe 6` foi lançado em 2003 e mudou o formato do arquivo para código `.xml` incorporado em arquivos `.pdf` e `.eps`. O `Ipe 7` foi lançado em 2009. `O Ipe 7` pode ser compilado no `Windows`, `macOS` e `Unix`, mas os binários estão disponíveis para muitas distribuições.
# 

# ## 1. Como configurar/instalar/usar o `ipe` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `ipe` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.2 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.3 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.4 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.5 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.6 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.7 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# Para instalar o `ipe` no `Linux Ubuntu` através do `Terminal Emulator`, você pode seguir os seguintes passos:
# 
# 1. **Abrir o Terminal:** Você pode abrir o Terminal pressionando: `Ctrl + Alt + T`
# 
# 2. **Instalar o `ipe`:** Digite o comando: `flatpak install flathub org.otfried.Ipe`
# 
# 3. **Executar o `ipe`:** Digite o comando: `flatpak run org.otfried.Ipe`

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `ipe` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean                               
#     sudo apt autoclean
#     sudo apt autoremove
#     sudo apt update -y
#     sudo apt autoremove
#     sudo apt autoclean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     flatpak install flathub org.otfried.Ipe
#     flatpak run org.otfried.Ipe
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Usando o SET Toolkit.*** Disponível em: <https://chat.openai.com/c/5d399ade-1dd7-4125-9d6f-89c86b1d723c> (texto adaptado). Acessado em: 18/03/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 18/03/2024 17:10.
# 
