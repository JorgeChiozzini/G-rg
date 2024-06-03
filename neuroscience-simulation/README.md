### Introdução ao Modelo de Hodgkin-Huxley

O modelo de Hodgkin-Huxley é um modelo matemático que descreve como os potenciais de ação (os sinais elétricos) são iniciados e propagados nos neurônios. Este modelo foi desenvolvido por Alan Hodgkin e Andrew Huxley em 1952, e eles receberam o Prêmio Nobel de Fisiologia ou Medicina em 1963 por este trabalho.

### Estrutura Básica do Neurônio

1. **Potencial de Membrana**: A diferença de potencial elétrico entre o interior e o exterior da célula.
2. **Ions Principais**: Sódio (Na⁺), Potássio (K⁺) e Cloro (Cl⁻) são os principais íons que influenciam o potencial de membrana.
3. **Condutâncias**: As proteínas de canal que permitem a passagem de íons através da membrana celular. Elas podem ser abertas ou fechadas em resposta a mudanças no potencial de membrana.

### Constantes do Modelo de Hodgkin-Huxley

O modelo descreve a dinâmica dos canais iônicos de sódio (Na⁺) e potássio (K⁺) e uma corrente de fuga (L) através de equações diferenciais:

- **Capacitância da Membrana (C_m)**: Representa a capacidade da membrana celular de armazenar carga.
- **Condutâncias (g_Na, g_K, g_L)**: Representam a condutividade dos canais iônicos para sódio, potássio e fuga, respectivamente.
- **Potenciais de Reversão (E_Na, E_K, E_L)**: Representam o potencial em que não há fluxo líquido de íons através dos canais específicos.

### Equações de Hodgkin-Huxley

As principais variáveis são o potencial de membrana \( V \), as variáveis de ativação \( m \), \( h \) e \( n \) que representam a probabilidade de abertura dos canais de sódio e potássio.

1. **Equações das Variáveis de Estado**:
   - \( \alpha_n(V) \) e \( \beta_n(V) \): Taxas de abertura e fechamento dos canais de potássio.
   - \( \alpha_m(V) \) e \( \beta_m(V) \): Taxas de abertura e fechamento dos canais de sódio.
   - \( \alpha_h(V) \) e \( \beta_h(V) \): Taxas de abertura e fechamento dos canais de sódio inativados.

2. **Equação do Potencial de Membrana**:
   \[
   C_m \frac{dV}{dt} = I - (I_{\text{Na}} + I_{\text{K}} + I_{\text{L}})
   \]
   Onde \( I \) é a corrente externa aplicada, \( I_{\text{Na}} \), \( I_{\text{K}} \) e \( I_{\text{L}} \) são as correntes iônicas de sódio, potássio e fuga, respectivamente.

### Simulação do Neurônio

A simulação envolve a resolução das equações diferenciais do modelo ao longo do tempo. Isso é feito usando um método numérico, como o método de Euler.

1. **Correntes Iônicas**:
   - \( I_{\text{Na}} = g_{\text{Na}} m^3 h (V - E_{\text{Na}}) \)
   - \( I_{\text{K}} = g_{\text{K}} n^4 (V - E_{\text{K}}) \)
   - \( I_{\text{L}} = g_{\text{L}} (V - E_{\text{L}}) \)

2. **Atualização das Variáveis de Estado**:
   - \( V \) é atualizado com base na soma das correntes iônicas e da corrente externa.
   - As variáveis \( m \), \( h \) e \( n \) são atualizadas com base nas suas taxas de transição.

### Plotando os Resultados

Os resultados da simulação incluem o potencial de membrana ao longo do tempo e a corrente de estímulo aplicada. O gráfico resultante mostra como o neurônio responde ao estímulo externo, gerando potenciais de ação.

### Resumo

O modelo de Hodgkin-Huxley fornece uma descrição detalhada de como os neurônios geram e propagam sinais elétricos. Ele captura a complexa dinâmica dos canais iônicos de sódio e potássio, permitindo a simulação precisa dos potenciais de ação. Este projeto exemplifica como implementar e visualizar essa dinâmica usando Python e Jupyter Notebook, tornando a neurociência computacional acessível a iniciantes.