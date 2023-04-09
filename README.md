# Inteligencia Artificial 28/03/2023

Linguagem orientada a agentes

## Conceitos

### Percepção
Informação que o agente consegue pegar do ambiente
- Exemplo: vizinhança

### Ações
O que o agente faz 
- Exemplo: andar, coletar, soltar

### Desempenho
Baseado em tempo de execução

## Tipos básicos de agente
- agentes reativos simples
- agentes reativos baseados em modelos
- agentes baseados em objetivos
- agentes baseados na utilidade

### Agente reativo simples
- Só toma decisão baseadas apenas nas percepções atuais do ambiente
- Não leva em consideração o histórico de ações ou o estado futuro do ambiente. 
- Eles respondem automaticamente a estímulos do ambiente, sem ter uma representação interna do mundo.

### Agente reativo com modelos
- Mantem históricos
- Esses agentes também tomam decisões com base nas percepções atuais do ambiente
- Têm uma representação interna do ambiente que lhes permite construir modelos internos do mundo. 
- Eles usam esses modelos para prever o efeito de suas ações antes de agir, permitindo-lhes fazer escolhas mais informadas.

### Agente baseado em objetivos
- Inicia execução com uma lista de objetivos
- Eles usam informações sobre o ambiente.
- Seu estado interno e seus objetivos para planejar e executar ações que os levem mais perto de seus objetivos.

### Agente baseado em utilizade
- Tem felicidade 
- Esses agentes atribuem valores de utilidade a diferentes ações e escolhem a ação que maximiza a utilidade esperada. Eles podem levar em consideração não apenas os objetivos imediatos, mas também as consequências de longo prazo de suas ações.
- exemplo items que valem mais pontos, etc...



