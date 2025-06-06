# T&D - Clusterização

## Visão Geral

Este projeto explora **técnicas de clusterização** para compreender quais fatores influenciam as avaliações de clientes (`review_score`) em um grande *e-commerce* brasileiro.
Os dados utilizados derivam do **Brazilian E-Commerce Public Dataset by Olist** — um conjunto com 100 mil pedidos de 2016-2018 que inclui preços, frete, atrasos de entrega, peso do produto, status do pedido e avaliações dos usuários ([kaggle.com][1]).
A pasta do repositório contém um **notebook Jupyter (`t_d_clusterization.ipynb`)** e um diretório **`/data`** para insumos em CSV ou Delta Tables ([github.com][2]).
O objetivo é aplicar **K-Means** (e variantes) para segmentar os pedidos, avaliando a relação entre clusters e satisfação do cliente ([scikit-learn.org][3]).

## Etapas Principais

1. **Coleta & Organização dos dados**

   * Download/ingestão dos 9 arquivos CSV oficiais do dataset Olist ([github.com][4]).
   * *Merge* das tabelas para formar um único *DataFrame* com as colunas-chave:
     `review_score`, `price`, `item_quantity`, `total_price`, `total_paid`,
     `delivery_delay`, `freight_value`, `product_weight`, `order_status`.

2. **Pré-Processamento**

   * Tratamento de nulos; criação de `delivery_status` categórico (adiantado, no prazo, atrasado).
   * *One-hot encoding* das variáveis categóricas e **padronização** das numéricas (Z-score).

3. **Seleção de Features & Experimentos**

   * Testes controlados variando subconjuntos de variáveis para medir impacto no *silhouette* e na **inércia** do K-Means ([medium.com][5]).
   * Uso dos métodos *Elbow* e *Silhouette* para escolher *k*.

4. **Treino & Avaliação**

   * Ajuste de **K-Means** (ou MiniBatchKMeans para grandes volumes).
   * Visualização dos clusters via **PCA** ou **t-SNE**; análise dos centróides.

5. **Interpretação de Resultados**

   * Correlação entre clusters e `review_score` para identificar perfis de experiência (p.ex. “alto preço & atraso → pontuação baixa”).

6. **Persistência & Relatório**

   * Salvamento dos modelos/artefatos em `/models`.
   * Geração de gráficos (Matplotlib/Seaborn) e métricas finais, exportados para `/reports`.

## Conclusão & Resultados

> *(Preencha aqui depois de rodar o notebook — inclua insights, números-chave, imagens dos clusters e recomendações de negócio.)*

---

### Autor

|                              |                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------- |
| **Éric Fadul Cunha Yoshida** | • [GitHub @faduzin](https://github.com/faduzin) • [LinkedIn](https://www.linkedin.com/in/ericfadul) |

[1]: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?utm_source=chatgpt.com "Brazilian E-Commerce Public Dataset by Olist | Kaggle"
[2]: https://github.com/faduzin/t-d-clusterization "GitHub - faduzin/t-d-clusterization"
[3]: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html?utm_source=chatgpt.com "KMeans — scikit-learn 1.6.1 documentation"
[4]: https://github.com/ayushic2899/Brazilian-E-Commerce-Public-Dataset-by-Olist?utm_source=chatgpt.com "ayushic2899/Brazilian-E-Commerce-Public-Dataset-by-Olist - GitHub"
[5]: https://medium.com/%40krgaurav45/customer-satisfaction-prediction-brazillian-e-commerce-public-dataset-5bb9ed841bf1?utm_source=chatgpt.com "Customer Satisfaction Prediction — Brazillian e-Commerce Public ..."
