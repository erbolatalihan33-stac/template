import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "../zz/components/App";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>
);
