# Portfolio redesign — GitHub Pages

Upload the contents of this ZIP to the root of your existing GitHub Pages repository, preserving the folders.

## Updated
- `index.html`: project cards replaced with a link to the library
- `resume.html`: links to the project library
- `style.css`: adds responsive accordion and library styling

## New
- `projects.html`: expandable project library organized by discipline
- `projects/espn-academy.html`: new ESPN Academy case study (privacy-safe, no student-level data)

## Preserved
- `script.js`, existing case-study pages, `assets/`, and existing resume assets.

The ESPN case study deliberately contains no student-level data or unverified metrics. Add a sanitized Power BI screenshot later if desired. Existing internal project pages remain linked.

## Project Library CSS fix
The project library now loads `projects-library.css` after `style.css` with versioned URLs to avoid stale cached styles. Upload `projects.html` and `projects-library.css` together to the repository root. Existing detailed case-study links remain intact.
