#### Visão Computacional

A visão computacional é um campo da ciência da computação que tem como objetivo permitir que computadores entendam e processem imagens e vídeos da mesma forma que os humanos. Ela envolve métodos para adquirir, processar, analisar e entender imagens do mundo real para produzir informações numéricas ou simbólicas.

#### Filtro de Sobel

O filtro de Sobel é uma técnica usada em processamento de imagens para detectar bordas. Ele calcula a derivada da imagem em duas direções, horizontal e vertical, para detectar mudanças rápidas na intensidade dos pixels, que são indicativas de bordas.

##### Passos do Filtro de Sobel:

1. **Aplicação de Kernels**:
   - Um kernel é uma pequena matriz usada para realizar convoluções em uma imagem. O filtro de Sobel usa dois kernels, um para detectar bordas horizontais e outro para detectar bordas verticais.
   - O kernel horizontal (sobel_x) e o kernel vertical (sobel_y) são aplicados à imagem para obter gradientes nas direções x e y.

2. **Cálculo do Gradiente**:
   - O gradiente da imagem em cada pixel é calculado combinando os gradientes horizontal e vertical.
   - A magnitude do gradiente é dada por:
     \[
     \text{Magnitude} = \sqrt{(G_x^2 + G_y^2)}
     \]
   - Onde \(G_x\) e \(G_y\) são os gradientes horizontais e verticais, respectivamente.

3. **Normalização**:
   - A magnitude do gradiente é normalizada para o intervalo de 0 a 255 para ser exibida como uma imagem de bordas.

### Resumo

Neste projeto, você aprendeu a usar GitHub Codespaces para configurar um ambiente de desenvolvimento e implementar um sistema de detecção de bordas usando o filtro de Sobel. Este projeto é uma introdução prática à visão computacional, permitindo que qualquer pessoa, mesmo sem experiência prévia, possa explorar técnicas de processamento de imagens.