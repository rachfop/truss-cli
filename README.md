# My Truss Docs

This repository hosts the Docusaurus-powered documentation site for the My Truss project. It contains the source markdown, configuration, and build tooling required to author and publish the docs.

## Getting Started

1. Install dependencies: `npm install`
2. Start the local dev server: `npm start`
3. Open the URL printed in the terminal (defaults to `http://localhost:3000`) to view and edit the docs in real time.

## Available Scripts

- `npm start` — launch the Docusaurus development server with hot reload.
- `npm run build` — generate the production static site into `build/`.
- `npm run serve` — locally serve the production build for validation.
- `npm run deploy` — deploy the site using the deployment settings configured in `docusaurus.config.js`.

## Project Structure

- `docs/` — markdown documents that feed the knowledge base.
- `src/` — React components, theme customizations, and utilities.
- `static/` — static assets copied verbatim into the final site.
- `docusaurus.config.js` — global site configuration.
- `sidebars.js` — navigation structure for the documentation sidebar.
