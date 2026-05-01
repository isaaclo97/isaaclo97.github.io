---
title: ""
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      username: admin

  - block: skills
    id: skills
    content:
      title: Skills
      text: ''
      username: admin
    design:
      columns: '1'

  - block: experience
    id: experience
    content:
      title: Experience
      date_format: Jan 2006
      items:
        - title: Assistant Doctor Professor
          company: Universidad Rey Juan Carlos
          company_url: 'https://www.urjc.es'
          location: Móstoles, Madrid
          date_start: '2023-09-01'
          date_end: ''
          description: Teaching and research in Computer Science.
        - title: Predoctoral Researcher
          company: Universidad Rey Juan Carlos
          company_url: 'https://www.urjc.es'
          location: Móstoles, Madrid
          date_start: '2020-01-01'
          date_end: '2023-08-31'
          description: Research in combinatorial optimization and metaheuristics. GRAFO Group.
        - title: Technical Support Staff — GRAFO Group
          company: Universidad Rey Juan Carlos
          company_url: 'https://www.urjc.es'
          location: Móstoles, Madrid
          date_start: '2019-11-01'
          date_end: '2019-12-31'
          description: Technical support on research projects of the GRAFO Group.
        - title: Technical Staff — BlueThinking Project
          company: Universidad Rey Juan Carlos
          company_url: 'https://www.urjc.es'
          location: Móstoles, Madrid
          date_start: '2018-10-01'
          date_end: '2019-01-31'
          description: Development of an educational programming app for children.
        - title: Frontend/Backend Developer
          company: World Dukes SL
          company_url: ''
          location: Madrid
          date_start: '2017-05-01'
          date_end: '2017-11-30'
          description: Frontend and backend web development.
    design:
      columns: '2'

  - block: markdown
    id: docencia
    content:
      title: Teaching
      text: |
        | Subject | Year | Hours | Rating | Role |
        |---------|------|------:|-------|------|
        | Algorithm Design and Development | 2025-2026 | 60h | 4.55/5.0 | Lecturer |
        | Computer Security | 2025-2026 | 26h | — | Lecturer |
        | Secure Development Methodologies | 2025-2026 | 20h | — | Lecturer |
        | Programming 1 | 2025-2026 | 30h | 4.24/5.0 | Lab sessions |
        | Hacking Techniques | 2025-2026 | 30h | 3.92/5.0 | Lab sessions |
        | Algorithm Design and Development | 2024-2025 | 75h | 4.80 / 4.24 /5.0 | Lecturer |
        | Computer Security | 2024-2025 | 60h | 4.45/5.0 | Lecturer |
        | Secure Development Methodologies | 2024-2025 | 50h | 4.46/5.0 | Lecturer |
        | Programming 1 | 2024-2025 | 30h | 3.94/5.0 | Lab sessions |
        | Computer Security | 2023-2024 | 40h | 4.74/5.0 | Lecturer |
        | Secure Development Methodologies | 2023-2024 | 20h | 4.18/5.0 | Lecturer |
        | Algorithm Design and Development | 2023-2024 | 10h | — | Lecturer |
        | Information Systems | 2023-2024 | 10h | — | Lecturer |
        | Computer Security | 2022-2023 | 40h | 4.4/5.0 | Lecturer |
        | Secure Development Methodologies | 2022-2023 | 20h | 4.4/5.0 | Lecturer |
        | Computer Security | 2021-2022 | 20h | 4.4/5.0 | Lecturer |
        | Secure Development Methodologies | 2021-2022 | 20h | 4.4/5.0 | Lecturer |
        | Information Systems | 2021-2022 | 20h | 4.4/5.0 | Lecturer |
    design:
      columns: '1'

  - block: markdown
    id: teaching
    content:
      title: Courses Taught
      text: |
        | Date | Course | Event |
        |------|--------|-------|
        | Nov 2020 | Competitive Programming in Python · 3h · [Slides](/uploads/slides.pdf) | Night of Researchers |
        | Nov 2020 | Android App Development with App Inventor · 2h | Night of Researchers |
        | Nov 2020 | Competitive Programming in Python · 3h · [Slides](/uploads/diapositivas_SemanaDeLaCiencia2020.pdf) | Science Week |
        | Nov 2020 | Augmented Reality with Unity and Vuforia · 2h | Science Week |
        | Nov 2020 | Visual Programming with Minecraft · 2h | Science Week |
        | Mar 2020 | Competitive Programming in Python · 2h · [Slides](/uploads/AULA.pdf) | AULA 2020 |
        | Feb–Apr 2020 | [Competitive Programming Course](https://urjc-cp.github.io/urjc-cp/) · 3 months | URJC |
        | Nov 2019 | Competitive Programming in Python · 2h | URJC |
        | Apr 2019 | How Public is Your Private Information? · 2h | URJC |
        | Apr 2019 | Competitive Programming · 4h | URJC |
        | Apr 2019 | Webworld — Web Development · 4h | URJC |
        | Jan–Apr 2019 | [Competitive Programming Course](https://urjc-cp.github.io/urjc-cp/) · 4 months | URJC |
    design:
      columns: '1'

  - block: collection
    id: featured
    content:
      title: Publications
      text: ''
      filters:
        folders:
          - publication
    design:
      columns: '2'
      view: citation

  - block: markdown
    id: awards
    content:
      title: Awards & Recognition
      text: |
        | Year | Award | Organisation |
        |------|-------|-------------|
        | 2024 | Best Student Paper — MAEB 2024 | XV Spanish Congress on Metaheuristics, Evolutionary and Bio-inspired Algorithms |
        | 2023 | Huawei Training Camp — Shenzhen, China | Huawei |
        | 2019 | [Winner — II Social Council Award for Young Researchers](/uploads/Resolucion.pdf) | Universidad Rey Juan Carlos |
        | 2019 | [Special Mention — E-Madrid Congress (BlueThinking)](http://www.emadridnet.org/) | eMadrid Excellence Network |
        | 2019 | Honours — Computer Engineering Final Project | Universidad Rey Juan Carlos |
        | 2019 | Honours — Computer Systems Engineering Final Project | Universidad Rey Juan Carlos |
    design:
      columns: '1'

  - block: collection
    id: posts
    content:
      title: Blog
      subtitle: ''
      text: ''
      filters:
        folders:
          - post
    design:
      columns: '2'
      view: compact

  - block: contact
    id: contact
    content:
      title: Contact
      email: isaac.lozano@urjc.es
      address:
        street: Edificio Departamental 2, Despacho 128
        city: Móstoles
        region: Madrid
        postcode: '28933'
        country: Spain
      contact_links:
        - icon: github
          icon_pack: fab
          name: GitHub
          link: 'https://github.com/isaaclo97'
        - icon: linkedin
          icon_pack: fab
          name: LinkedIn
          link: 'https://www.linkedin.com/in/isaaclozanoosorio/'
---
