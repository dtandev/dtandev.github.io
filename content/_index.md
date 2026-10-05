---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      # Full biography for the homepage. The author profile (data/authors/me.yaml) keeps only the
      # first paragraph, which is what the author box under articles and projects shows.
      text: |-
        I'm Head of Science & Innovation at TerraEye, where I lead the team developing geospatial intelligence solutions for the mining industry across the whole project lifecycle — from exploration to reclamation. I have over 15 years of experience in geospatial data science, more than five of them focused specifically on Earth Observation, and my work sits where EO science meets industrial deployment.

        I've contributed to projects funded by the European Space Agency, the European Commission and Poland's National Centre for Research and Development, and worked on solutions later adopted by a major global resource group. My focus is integrating multisensor data and applying advanced geospatial analytics and machine learning to mineral exploration and geological interpretation.
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    id: recognition
    content:
      title: 'Recognition & Awards'
      subtitle: ''
      text: |-
        <div style="display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap">
          <a href="https://geospatialworld.net/rising-stars/2026/" target="_blank" rel="noopener">
            <img src="/media/badges/gw-rising-stars-2026.png" alt="Geospatial World 50 Rising Stars 2026" width="120" height="157" style="margin:0">
          </a>
          <p style="margin:0;flex:1;min-width:14rem">
            <strong>2026</strong> — named one of the <a href="https://geospatialworld.net/rising-stars/2026/" target="_blank" rel="noopener">Geospatial World 50 Rising Stars 2026</a>.
          </p>
        </div>
        <div style="display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap;margin-top:1.5rem">
          <img class="cassini-logo" src="/media/badges/cassini.svg" alt="CASSINI" style="margin:0;width:120px;height:auto">
          <p style="margin:0;flex:1;min-width:14rem">
            <strong>2023, 2024</strong> — TerraEye's team nominated in the <a href="https://www.cassini.eu/" target="_blank" rel="noopener">CASSINI Challenge</a> twice: in 2023 in the Prototype category (SAR Gate) and in 2024 in the Idea category (AIMS, Asbestos Identification and Mapping Solution).
          </p>
        </div>
        <div style="display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap;margin-top:1.5rem">
          <img src="/media/badges/bsa.svg" alt="BalticSatApps" style="margin:0;width:120px;height:auto;padding:0 20px">
          <p style="margin:0;flex:1;min-width:14rem">
            <strong>2020</strong> — member of the winning team at the <a href="https://balticsatapps.adrianwii.pl/" target="_blank" rel="noopener">BalticSatApps</a> hackathon with an application detecting unauthorised (illegal) construction.
          </p>
        </div>
        <div style="display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap;margin-top:1.5rem">
          <img class="member-logo" src="/media/badges/galileo-masters.png" alt="Galileo Masters (European Satellite Navigation Competition)" style="margin:0;width:120px;height:auto">
          <p style="margin:0;flex:1;min-width:14rem">
            <strong>2015</strong> — DLR Special Prize, awarded by the German Aerospace Center (DLR) at the European Satellite Navigation Competition (ESNC, formerly Galileo Masters) for the concept of the Mobile Underwater Positioning System (MUPS).
          </p>
        </div>
    design:
      columns: '1'
  - block: markdown
    id: memberships
    content:
      title: 'Memberships'
      subtitle: ''
      text: |-
        <div style="display:flex;align-items:center;gap:2.5rem;flex-wrap:wrap">
          <a href="https://www.grss-ieee.org/" target="_blank" rel="noopener" title="IEEE Geoscience and Remote Sensing Society">
            <img class="member-logo" src="/media/badges/grss.png" alt="IEEE Geoscience and Remote Sensing Society (GRSS)" style="margin:0;height:90px;width:auto">
          </a>
          <a href="https://pspa.pl/" target="_blank" rel="noopener" title="Polish Space Professionals Association">
            <img class="member-logo" src="/media/badges/pspa.png" alt="Polish Space Professionals Association (PSPA)" style="margin:0;height:90px;width:auto">
          </a>
          <!-- EGU is hidden until the membership is paid for 2027. Then remove the comment markers around this block.
          <a href="https://www.egu.eu/" target="_blank" rel="noopener" title="European Geosciences Union">
            <img class="egu-light" src="/media/badges/egu-blue.svg" alt="European Geosciences Union (EGU)" style="margin:0;height:90px;width:auto">
            <img class="egu-dark" src="/media/badges/egu-yellow.svg" alt="European Geosciences Union (EGU)" style="margin:0;height:90px;width:auto">
          </a>
          -->
        </div>
    design:
      columns: '1'
  - block: markdown
    content:
      title: 'About'
      subtitle: ''
      text: |-
        <!-- TODO: zastąp własnym opisem (np. z LinkedIn "About"). -->
        Remote sensing and Earth observation R&D at TerraEye — SAR/InSAR, optical and
        hyperspectral data for geology and mineral exploration, and turning research
        methods into operational EO workflows. Critical, limitations-first, practitioner view.
    design:
      columns: '1'
  - block: markdown
    id: github
    content:
      title: 'On GitHub'
      subtitle: ''
      text: |-
        <div class="gh-stats">
          <a class="gh-calendar" href="https://github.com/dtandev" target="_blank" rel="noopener">
            <img src="https://ghchart.rshah.org/3b2313/dtandev" alt="GitHub contribution calendar for dtandev" loading="lazy">
          </a>
          <div class="gh-cards">
            <img class="gh-light" loading="lazy" alt="GitHub stats for dtandev" src="https://github-readme-stats.vercel.app/api?username=dtandev&show_icons=true&include_all_commits=true&hide_rank=true&hide=contribs,issues&disable_animations=true&hide_border=true&bg_color=00000000&title_color=3b2313&text_color=5c4033&icon_color=d97706">
            <img class="gh-dark" loading="lazy" alt="GitHub stats for dtandev" src="https://github-readme-stats.vercel.app/api?username=dtandev&show_icons=true&include_all_commits=true&hide_rank=true&hide=contribs,issues&disable_animations=true&hide_border=true&bg_color=00000000&title_color=d49255&text_color=e0cab6&icon_color=d49255">
            <img class="gh-light" loading="lazy" alt="Most used languages on GitHub" src="https://github-readme-stats.vercel.app/api/top-langs/?username=dtandev&layout=compact&hide=html,just&disable_animations=true&hide_border=true&bg_color=00000000&title_color=3b2313&text_color=5c4033">
            <img class="gh-dark" loading="lazy" alt="Most used languages on GitHub" src="https://github-readme-stats.vercel.app/api/top-langs/?username=dtandev&layout=compact&hide=html,just&disable_animations=true&hide_border=true&bg_color=00000000&title_color=d49255&text_color=e0cab6">
          </div>
        </div>
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    content:
      title: More Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: true
    design:
      view: citation
  - block: cta-card
    demo: true # Only display this section in the HugoBlox Kit demo site
    content:
      title: 👉 Build your own academic website like this
      text: |-
        This site is generated by HugoBlox Kit - the FREE, Hugo-based open source website builder trusted by 250,000+ academics like you.

        <a class="github-button" href="https://github.com/HugoBlox/kit" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star HugoBlox/kit on GitHub">Star</a>

        Easily build anything with blocks - no-code required!

        From landing pages, second brains, and courses to academic resumés, conferences, and tech blogs.
      button:
        text: Get Started
        url: https://hugoblox.com/templates/
    design:
      card:
        # Card background color (CSS class)
        css_class: 'bg-gradient-to-br from-primary-500 via-primary-600 to-secondary-600 text-white shadow-2xl'
        css_style: ''
---
