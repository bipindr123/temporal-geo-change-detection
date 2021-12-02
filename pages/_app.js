import '../styles/globals.css'
import 'bootstrap/dist/css/bootstrap.css'; // Add this line
import { useEffect } from "react";

function MyApp({ Component, pageProps }) {
  // Place this in the pages/_app.js file
  useEffect(() => {
    import("bootstrap/dist/js/bootstrap");
  }, []);
  return <Component {...pageProps} />
}

export default MyApp
