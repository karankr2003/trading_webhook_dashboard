# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default defineConfig([
  # Frontend (React + TypeScript + Vite)

  This folder contains the React frontend for the Trading Dashboard. It is a small TypeScript + Vite app that queries the backend API to display recent trades and statistics.

  Keep this README short — the full project setup and API are documented in the top-level `README.md`.

  ## Quick Start (frontend)

  Prerequisites:
  - Node.js 18+ (includes npm)

  Install dependencies:

  ```bash
  cd frontend
  npm install
  ```

  Create environment file from the template (optional):

  ```bash
  cp .env.example .env
  # Edit VITE_API_URL in .env if backend runs on a different host/port
  ```

  Run development server (HMR):

  ```bash
  npm run dev
  ```

  Build for production:

  ```bash
  npm run build
  npm run preview
  ```

  Available scripts (from `package.json`):
  - `dev`: start Vite dev server
  - `build`: build production bundle
  - `preview`: preview production build locally
  - `lint`: run linting (if configured)

  ## Environment

  The frontend reads the backend base URL from `VITE_API_URL` (see `.env.example`). Default: `http://localhost:8000`.

  ## Notes

  - The frontend polls the backend every 5 seconds to refresh trades. For true real-time updates consider WebSockets.
  - Keep `frontend/README.md` focused on running/building the UI; project-level details (database setup, backend) are in the root `README.md`.

  ## Troubleshooting

  - If the UI cannot fetch data, confirm the backend is running and `VITE_API_URL` points to the correct address.
  - If TypeScript errors appear during build, run `npm install` and re-run the dev server.

  ---
