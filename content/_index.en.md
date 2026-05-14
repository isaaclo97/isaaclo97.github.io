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
        I have supervised **17 Bachelor's Final Projects (TFG)** and **3 Master's Final Projects (TFM)**, and have participated in more than **40 evaluation committees**. In total, I have taught **581 hours** of university teaching, equivalent to **58.1 credits**.

        <style>.yr-btn{padding:5px 16px;border:1px solid #ccc;border-radius:20px;cursor:pointer;background:#f5f5f5;font-size:.875rem;margin:2px;transition:background .2s,color .2s}.yr-btn.yr-active{background:#1565c0;color:#fff;border-color:#1565c0}.yr-pane{display:none}.yr-pane.yr-show{display:block}</style>
        <div style="display:flex;gap:4px;flex-wrap:wrap;margin-bottom:.75rem">
        <button class="yr-btn yr-active" onclick="yrTab(this,'yr2526')">2025-2026</button>
        <button class="yr-btn" onclick="yrTab(this,'yr2425')">2024-2025</button>
        <button class="yr-btn" onclick="yrTab(this,'yr2324')">2023-2024</button>
        <button class="yr-btn" onclick="yrTab(this,'yr2223')">2022-2023</button>
        <button class="yr-btn" onclick="yrTab(this,'yr2122')">2021-2022</button>
        </div>
        <div id="yr2526" class="yr-pane yr-show"><table><thead><tr><th>Subject</th><th>Hours</th><th>Rating</th><th>Role</th></tr></thead><tbody>
        <tr><td>Algorithm Design and Development</td><td>60h</td><td>4.55/5.0</td><td>Lecturer</td></tr>
        <tr><td>Computer Security</td><td>26h</td><td>—</td><td>Lecturer</td></tr>
        <tr><td>Secure Development Methodologies</td><td>20h</td><td>—</td><td>Lecturer</td></tr>
        <tr><td>Programming 1</td><td>30h</td><td>4.24/5.0</td><td>Lab sessions</td></tr>
        <tr><td>Hacking Techniques</td><td>30h</td><td>3.92/5.0</td><td>Lab sessions</td></tr>
        </tbody></table></div>
        <div id="yr2425" class="yr-pane"><table><thead><tr><th>Subject</th><th>Hours</th><th>Rating</th><th>Role</th></tr></thead><tbody>
        <tr><td>Algorithm Design and Development</td><td>75h</td><td>4.80 / 4.24 /5.0</td><td>Lecturer</td></tr>
        <tr><td>Computer Security</td><td>60h</td><td>4.45/5.0</td><td>Lecturer</td></tr>
        <tr><td>Secure Development Methodologies</td><td>50h</td><td>4.46/5.0</td><td>Lecturer</td></tr>
        <tr><td>Programming 1</td><td>30h</td><td>3.94/5.0</td><td>Lab sessions</td></tr>
        </tbody></table></div>
        <div id="yr2324" class="yr-pane"><table><thead><tr><th>Subject</th><th>Hours</th><th>Rating</th><th>Role</th></tr></thead><tbody>
        <tr><td>Computer Security</td><td>40h</td><td>4.74/5.0</td><td>Lecturer</td></tr>
        <tr><td>Secure Development Methodologies</td><td>20h</td><td>4.18/5.0</td><td>Lecturer</td></tr>
        <tr><td>Algorithm Design and Development</td><td>10h</td><td>—</td><td>Lecturer</td></tr>
        <tr><td>Information Systems</td><td>10h</td><td>—</td><td>Lecturer</td></tr>
        </tbody></table></div>
        <div id="yr2223" class="yr-pane"><table><thead><tr><th>Subject</th><th>Hours</th><th>Rating</th><th>Role</th></tr></thead><tbody>
        <tr><td>Computer Security</td><td>40h</td><td>4.4/5.0</td><td>Lecturer</td></tr>
        <tr><td>Secure Development Methodologies</td><td>20h</td><td>4.4/5.0</td><td>Lecturer</td></tr>
        </tbody></table></div>
        <div id="yr2122" class="yr-pane"><table><thead><tr><th>Subject</th><th>Hours</th><th>Rating</th><th>Role</th></tr></thead><tbody>
        <tr><td>Computer Security</td><td>20h</td><td>4.4/5.0</td><td>Lecturer</td></tr>
        <tr><td>Secure Development Methodologies</td><td>20h</td><td>4.4/5.0</td><td>Lecturer</td></tr>
        <tr><td>Information Systems</td><td>20h</td><td>4.4/5.0</td><td>Lecturer</td></tr>
        </tbody></table></div>
        <script>function yrTab(b,id){document.querySelectorAll('.yr-btn').forEach(x=>x.classList.remove('yr-active'));b.classList.add('yr-active');document.querySelectorAll('.yr-pane').forEach(p=>p.classList.remove('yr-show'));document.getElementById(id).classList.add('yr-show');}</script>

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
        | 2026 | [Winner — XI JNIC 2022](/premios/2026%20-%20Certificado%20-%20Premio%20JNIC%202026.pdf) | Spanish National Conference on Cybersecurity Research |
        | 2025 | [Extraordinary Doctoral Award](/premios/2025%20-%20Premio%20Extraordinario%20Tesis.pdf) | Universidad Rey Juan Carlos |
        | 2025 | [Thesis Award for Greatest Impact on SDGs](/premios/2025%20-%20Premio%20ODS%20Tesis.pdf) | Universidad Rey Juan Carlos |
        | 2024 | [Best Student Paper — MAEB 2024](/premios/2024%20-%20Certificado%20-%20Premio%20MAEB%202024.pdf) | XV Spanish Congress on Metaheuristics, Evolutionary and Bio-inspired Algorithms |
        | 2024 | [Award — IX JNIC 2024](/premios/2024%20-%20Certificado%20-%20Premio%20JNIC%202024.pdf) | Spanish National Conference on Cybersecurity Research |
        | 2023 | Huawei Training Camp — Shenzhen, China | Huawei |
        | 2023 | [3rd place — VIII JNIC 2023](/premios/2023%20-%20Certificado%20-%20Premio%20JNIC%202023.pdf) | Spanish National Conference on Cybersecurity Research |
        | 2023 | [Finalist — National Cyber Challenge League 2023](/premios/2023%20-%20Certificado%20-%20Finalista%20NCL%202023.pdf) | National Cyber Challenge League |
        | 2022 | [Winner — VII JNIC 2022](/premios/2022%20-%20Certificado%20-%20Premio%20JNIC%202022.png) | Spanish National Conference on Cybersecurity Research |
        | 2021 | 2nd place — BitUp 2021 | BitUp Hackathon |
        | 2020 | [Winner — II National Cyber Challenge League](/premios/2020%20-%20Certificado%20-%20Finalista%20NCL%202020.pdf) | National Cyber Challenge League |
        | 2020 | [Las12Uvas 2020](/premios/2020%20-%20Certificado%20-%20Las12Uvas%202020.pdf) | Year-End Programming Contest |
        | 2019 | [Winner — II Social Council Award for Young Researchers](/uploads/Resolucion.pdf) | Universidad Rey Juan Carlos |
        | 2019 | [Special Mention — E-Madrid Congress (BlueThinking)](/premios/2020%20-%20Certificado%20-%20Menci%C3%B3n%20TFG%20Emadrid.pdf) | eMadrid Excellence Network |
        | 2019 | Honours — Computer Engineering Final Project | Universidad Rey Juan Carlos |
        | 2019 | Honours — Computer Systems Engineering Final Project | Universidad Rey Juan Carlos |
        | 2019 | [Ada Byron Award 2019](/premios/2019%20-%20Certificado%20-%20AdaByron%202019%20Premio.pdf) | RITSI |
        | 2019 | [Las12Uvas 2019](/premios/2019%20-%20Certificado%20-%20Las12Uvas%202019.pdf) | Year-End Programming Contest |
        | 2019 | [T3chFest Award 2019](/premios/2019%20-%20Certificado%20-%20Premio%20T3chfest%202019.pdf) | T3chFest |
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
