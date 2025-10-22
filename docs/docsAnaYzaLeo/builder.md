# Builder

## Introdução

Os **padrões de projeto criacionais** têm como objetivo definir maneiras flexíveis e reutilizáveis de criar objetos e suas composições, reduzindo o acoplamento entre classes e favorecendo a extensibilidade do sistema (GAMMA et al., 1995). 

Dentre os padrões de projeto, o ***Builder*** se destaca por isolar o processo de construção de um objeto complexo, permitindo que diferentes representações possam ser geradas a partir do mesmo procedimento (REFACTORING GURU, 2023). Essa característica torna o **GoF *Builder*** uma solução ideal para sistemas que exigem a criação de objetos compostos, modulares e configuráveis (SOURCEMAKING, 2023).

## Metodologia

A construção do **GoF *Builder*** foi primeiramente construída a partir dos conhecimentos adquiridos durante as aulas ministradas pela professora Milene Serrano e seus slides **GoF Criacrionais(2025)**, além da análise da literatura do livro  **Gamma et al. (2000).**   
Porém, cada integrante dessa divisão do grupo tinha sua visão dos padrões criacionais e, por muito tempo houve diferenças de opiniões, então durante o desenvolvimento do padrão de projeto Builder, foram feitas 4 reuniões, uma no dia  15, no qual não houve nenhum acordo entre os integrantes (mas a gravação ficou muito longa o que dificultou o envio à plataforma *Youtube,* então os integrantes acharam melhor não colocar na documentação já que não houve desenvolvimento de nada), e outra reunião no dia  17/09 que durou 3 horas.  
Durante a ultima reunião foi incluido as outras duas fontes **Refactoring Guru (2023)** e **SourceMaking (2023)** que permitiram uma melhor visão sobre a modelagem e sobre o que era o padrão de projeto Builder, mesmo que durante o desenvolvimento os integrantes trocaram de ***Builder*** e ***Prototype***, no fim perceberam que para a funcionalidade do fórum, que atualmente contém publicação e comentário, seria melhor o desenvolvimento de um Builder que construi-se a publicação e o comentário separados, mas através de uma interface builder.  
Como consta na fonte Refactoring Guru(2023), o Builder é composto por:

- ***Builder**:* interface abstrata que especifica as etapas de criação;  
- ***ConcreteBuilder:*** implementação concreta dessas etapas;  
- ***Director:*** responsável por coordenar a construção;  
- ***Product:*** resultado final do processo.

 As gravações das reuniões estão a seguir: 

| Reunião | Integrantes | Data | Link |
| :---- | :---- | :---- | :---- |
| 01 | [Ana Luiza Soares](https://github.com/Ana-Luiza-SC), [Leonardo Barcelos](https://github.com/oyLeonardo) e [Yzabella Miranda](https://github.com/redjsun) | 17/10/2025 | [https://unbbr.sharepoint.com/:v:/s/arquitetos/EWNTWmyA3oFHnCVxBo3IRUYB34eILTDJXEMufMTqOOutqA?e=MjzNUR](https://unbbr.sharepoint.com/:v:/s/arquitetos/EWNTWmyA3oFHnCVxBo3IRUYB34eILTDJXEMufMTqOOutqA?e=MjzNUR) |
| 02 | [Ana Luiza Soares](https://github.com/Ana-Luiza-SC), [Leonardo Barcelos](https://github.com/oyLeonardo) e [Yzabella Miranda](https://github.com/redjsun) | 17/10/2025 | [https://unbbr.sharepoint.com/:v:/s/arquitetos/ESxJosJC2X9CmHcfShrhFNIBihOw\_bAj0QcqqFnCNWfJDA?e=EMDLLb](https://unbbr.sharepoint.com/:v:/s/arquitetos/ESxJosJC2X9CmHcfShrhFNIBihOw_bAj0QcqqFnCNWfJDA?e=EMDLLb) |
| 03 | [Ana Luiza Soares](https://github.com/Ana-Luiza-SC), [Leonardo Barcelos](https://github.com/oyLeonardo) e [Yzabella Miranda](https://github.com/redjsun) | 17/10/2025 | [https://unbbr.sharepoint.com/:v:/s/arquitetos/Eepo1sfqTUxFpFRTWQASkggBPx-dIh5HNM4s\_Gd7whT4pA?e=QOZj1u](https://unbbr.sharepoint.com/:v:/s/arquitetos/Eepo1sfqTUxFpFRTWQASkggBPx-dIh5HNM4s_Gd7whT4pA?e=QOZj1u) |

## Modelagem

A seguir, é possível visualizar a foto da modelagem gerada:
<p align="center">Imagem  1 - Modelagem do GoF Builder</p>

(adiciono as fotos)

## Implementação

Colocar a implementação

## Referências Bibliográficas

GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; et al. **Padrões de projetos: soluções reutilizáveis de software orientados a objetos**. Porto Alegre: Bookman, 2000\. *E-book.* p.99. ISBN 9788577800469\. Disponível em: [https://app.minhabiblioteca.com.br/reader/books/9788577800469/](https://app.minhabiblioteca.com.br/reader/books/9788577800469/). Acesso em: 20 out. 2025\.  
SERRANO, Milene. **AULA \- GOFS CRIACIONAIS**. 2025\. Disponível em: [https://aprender3.unb.br/pluginfile.php/3178396/mod\_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Criacionais%20-%20Profa.%20Milene.pdf](https://aprender3.unb.br/pluginfile.php/3178396/mod_page/content/1/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GoFs%20Criacionais%20-%20Profa.%20Milene.pdf). Acesso em: 21 out. 2025,   
REFACTORING GURU. *Padrão de Projeto Builder*. Disponível em: [https://refactoring.guru/pt-br/design-patterns/builder](https://refactoring.guru/pt-br/design-patterns/builder). Acesso em: 20 out. 2025\.  
SOURCEMAKING. *Builder Design Pattern*. Disponível em: [https://sourcemaking.com/design\_patterns/builder](https://sourcemaking.com/design_patterns/builder). Acesso em: 20 out. 2025\.  

## Tabela de Versionamento

| Versão | Data       | Descrição                                        | Autor(es)           | Revisor(es)         | Comentário do revisor | Data da revisão |
|--------|------------|--------------------------------------------------|---------------------|---------------------|----------------------|-----------|
| `1.0` | 17/10/2025  | Criação da Modelagem e código do padrão de projeto Builder aplicado as classes publicação e comentário | [Ana Luiza Soares](https://github.com/Ana-Luiza-SC), [Leonardo Barcelos](https://github.com/oyLeonardo) e [Yzabella Miranda](https://github.com/redjsun) | [Matheus de Alcântara](https://github.com/matheusdealcantara) | - | - |
| `1.0` | 17/10/2025  | Criação da estrutural inicial do documento, com introdução, metodologia utilizada, link para vídeos e referência bibliográfica | [Ana Luiza Soares](https://github.com/Ana-Luiza-SC) | [Matheus de Alcântara](https://github.com/matheusdealcantara) | - | - |