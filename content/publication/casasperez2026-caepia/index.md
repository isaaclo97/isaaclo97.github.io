---
title: "Algoritmo metaheurístico para el problema de la minimización de la influencia con costes"
authors:
  - Mario Casas-Pérez
  - Isaac Lozano-Osorio
  - Óscar Cordón
date: 2026-11-15
doi: ""
publication_types: ["1"]
publication: "*XVII Congreso Español de Metaheurísticas, Algoritmos Evolutivos y Bioinspirados (MAEB 2026), XXI Conferencia de la Asociación Española para la Inteligencia Artificial*"
abstract: "Este artículo aborda el problema de minimización de influencia (IMIN) bajo restricción presupuestaria en redes sociales, donde dicha influencia está iniciada por un conjunto de actores malintencionados denominados semillas. El objetivo es minimizar esta difusión perniciosa bloqueando nodos a cambio de un coste asociado a cada nodo individual. El problema se formula como una tarea de optimización combinatoria NP-hard, para la que se propone la metaheurística Greedy Randomized Adaptive Search (GRASP) dónde la fase de mejora consiste en una búsqueda local mediante intercambio de nodos y evaluación subrogada para reducir el coste de las simulaciones Monte Carlo. Consideramos una estrategia heurística de priorización en la selección de nodos candidatos basada en el tamaño esperado de los subárboles en un árbol de dominadores calculado mediante el algoritmo de Lengauer-Tarjan sobre múltiples realizaciones de Monte Carlo, lo que permite identificar de forma precisa los cuellos de botella estructurales que controlan la difusión. La metodología se evalúa experimentalmente sobre ocho redes reales de distinta escala bajo el modelo de difusión Independent Cascade, considerando distintos presupuestos. Los resultados muestran que la variante basada en la heurística propuesta obtiene el mejor valor de la función objetivo en todas las instancias evaluadas y con una desviación porcentual promedio del 0.00 %, aunque con un coste computacional superior en la mayoría de casos. No obstante, la evidencia experimental indica que la combinación de construcción aleatorizada y refinamiento local constituye una estrategia efectiva para abordar la IMIN con presupuesto heterogéneo."
url_pdf: "/congresos/MAEB-CIMIN-Articulo-2026.pdf"
url_slides: "/congresos/MAEB-CIMIN-2026.pdf"
featured: false
tags: ["Ciencia de Redes", "Minimización de Influencia", "GRASP"]
---
